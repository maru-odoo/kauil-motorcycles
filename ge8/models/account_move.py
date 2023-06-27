from odoo import models, fields


class AccountMove(models.Model):
    _inherit = "account.move.line"
    vin = fields.Char(string='VIN',compute="_compute_vin")
    # lot_id=fields.Char(related="motorcycle_registry.lot_id")

    def _compute_vin(self):
        self.vin='000'
        # for product in self:
        #     self.vin = '000'
