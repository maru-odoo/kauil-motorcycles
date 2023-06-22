from odoo import models


class Picking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        if not super(Picking, self).button_validate():
            return False

        for move in self.move_ids:
            for lot in move.lot_ids:
                if lot.product_id.product_tmpl_id.detailed_type == 'motorcycle':
                    self.env['motorcycle.registry'].create({"vin": lot.name})

        return True
