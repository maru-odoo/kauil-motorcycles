from odoo import models


class StockLot(models.Model):
    _inherit = "stock.lot"

    def _get_next_serial(self, company, product):
        tmpl = product.product_tmpl_id

        if tmpl.detailed_type == 'motorcycle' and product.tracking != "none":
            make = tmpl.make[:2].upper() if tmpl.make else 'XX'
            model = tmpl.model[:2].upper() if tmpl.model else 'XX'
            year = tmpl.year%100 if tmpl.year else 'XX'
            battery_capacity = tmpl.battery_capacity[:2].upper() if tmpl.battery_capacity else 'XX'
            serial_number = self.env["ir.sequence"].next_by_code("stock.lot.serial")

            return f"{make}{model}{year}{battery_capacity}{serial_number}"
        else:
            return super(StockLot, self)._get_next_serial(company, product)
