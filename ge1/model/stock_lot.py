from odoo import models, api, fields


class StockLot(models.Model):
    _inherit = "stock.lot"

    name = fields.Char('Lot/Serial Number', compute='_compute_name')

    @api.depends("product_id")
    def _compute_name(self):
        if self.product_id.product_tmpl_id.detailed_type == 'motorcycle':
            tmpl = self.product_id.product_tmpl_id
            
            # TODO: Make this readable
            self.name = f"{tmpl.make[:2].upper()}{tmpl.model[:2].upper()}{tmpl.year%100}{tmpl.battery_capacity.upper()}{self.env['ir.sequence'].next_by_code('motorcycle_register.id')}"
            print("Motorcycle: " + self.name)
        else:
            # TODO: Look into repeated increment :D
            self.name = self.env['ir.sequence'].next_by_code('stock.lot.serial')
            print("Non-motorcycle: " + self.name)
