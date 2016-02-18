# -*- coding: utf-8 -*-
from openerp import models, fields, api
# from openerp.exceptions import UserError


class AccountConfigSettings(models.TransientModel):
    _inherit = 'account.config.settings'

    sale_use_documents = fields.Boolean(
        'Sale Use Documents'
        )
    purchase_use_documents = fields.Boolean(
        'Purchase Use Documents'
        )
    localization = fields.Selection(
        related='chart_template_id.localization'
        )

    @api.onchange('chart_template_id')
    def account_documentonchange_chart_template(self):
        if self.chart_template_id.localization:
            self.sale_use_documents = True
            self.purchase_use_documents = True

    @api.multi
    def set_chart_of_accounts(self):
        """
        We send this value in context because to use them on journals creation
        """
        return super(AccountConfigSettings, self.with_context(
            sale_use_documents=self.sale_use_documents,
            purchase_use_documents=self.purchase_use_documents,
            )).set_chart_of_accounts()
