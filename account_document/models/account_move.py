# -*- coding: utf-8 -*-
from openerp import fields, models, api
# from openerp.exceptions import UserError


class account_move(models.Model):
    _inherit = "account.move"

    document_type_id = fields.Many2one(
        'account.document.type',
        'Document Type',
        copy=False,
        states={'posted': [('readonly', True)]}
        )
    document_number = fields.Char(
        string='Document Number',
        copy=False,
        states={'posted': [('readonly', True)]}
        )
    display_name = fields.Char(
        compute='_get_display_name',
        store=True
    )

    @api.one
    @api.depends(
        'document_number',
        'name',
        'document_type_id',
        # we disable this depnd because it makes update module performance low
        # 'document_type_id.doc_code_prefix',
    )
    def _get_display_name(self):
        if self.document_number and self.document_type_id:
            display_name = (
                self.document_type_id.doc_code_prefix or '') + \
                self.document_number
        else:
            display_name = self.name
        self.display_name = display_name
