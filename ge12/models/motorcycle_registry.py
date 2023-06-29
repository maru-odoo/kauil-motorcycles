from odoo import models, fields, api


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    def _has_registered_bike(self, owner_id):
        registries_count = self.env['motorcycle.registry'].search_count([('owner_id', '=', owner_id)])
        print("registries", registries_count)
        return registries_count != 0
    
    def _create_portal_account(self, owner_id):
        pass

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            sale_order_id = vals.get("sale_order_id")
            sale_order = self.env["sale.order"].browse([sale_order_id])
            owner_id = sale_order.partner_id.id

            if owner_id and not self._has_registered_bike(owner_id):
                self._create_portal_account(owner_id)

            super(MotorcycleRegistry, self).create(vals)
