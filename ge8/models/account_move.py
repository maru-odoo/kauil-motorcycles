from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move.line"

    # vin = fields.Char(comodel="motorcycle.registry",related="lot_id.name",string='VIN')
    vin = fields.Char(string='VIN')
    #many2one