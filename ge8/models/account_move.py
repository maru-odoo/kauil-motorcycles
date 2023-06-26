from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move.line"
    vin = fields.Char(string='VIN')

