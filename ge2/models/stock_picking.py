from odoo import models


class Picking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        res = super(Picking, self).button_validate()
        if not res:
            return False

        for move in self.move_ids:
            for line in move.move_line_ids:
                lot = line.lot_id

                if lot.product_id.product_tmpl_id.detailed_type == 'motorcycle' and self.location_dest_id == self.env.ref("stock.stock_location_customers"):
                    if self.origin:
                        records = self.env['sale.order'].search([('name', '=', self.origin)], limit=1)
                        sale_order = records[0].id if len(records) > 0 else False
                    else:
                        sale_order = False

                    self.env['motorcycle.registry'].create({"lot_ids": lot, "vin": lot.name, "sale_order_id": sale_order})

        return res
