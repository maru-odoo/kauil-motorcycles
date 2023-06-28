from odoo import api, models, fields

class RepairOrder(models.Model):
    _inherit = "repair.order"

    vin = fields.Char(string="VIN")
    mileage = fields.Float(string="Mileage")
    registry_id = fields.Many2one(comodel_name="motorcycle.registry", compute="_compute_from_vin", store=True)
    partner_id = fields.Many2one(relation="registry_id")
    sale_order_id = fields.Many2one(relation="registry_id")
    product_id = fields.Many2one(relation="registry_id")
    

    @api.depends('vin')
    def _compute_from_vin(self):
        for registry in self:
            registry_id = self.env['motorcycle.registry'].search([('vin', '=', registry.vin)])
            if registry_id:
                registry.registry_id = registry_id
            else:
                registry.registry_id = False

            