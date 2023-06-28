from odoo import models, fields,api


class AccountMoveLine(models.Model):
    _inherit = "account.move.line"
    vin = fields.Char(string='VIN',compute="_compute_vin")
    lot_ids=fields.Many2one(related="sale_line_ids.move_ids.lot_ids.registry_id")

    @api.depends('lot_ids')
    def _compute_vin(self):
        for product in self:
            product.vin=product.lot_ids.vin
