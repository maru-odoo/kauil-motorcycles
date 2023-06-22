from odoo import models


class Picking(models.Model):
    _inherit = "stock.picking"

    def button_validate(self):
        if not super(Picking, self).button_validate():
            return False

        if self.product_id.product_tmpl_id.detailed_type == 'motorcycle':
            # TODO: Acquire VIN from stock lot
            self.env['motorcycle.registry'].create({"vin": ""})

        return True
