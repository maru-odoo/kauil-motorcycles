from odoo import api, models, fields

class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    repair_ids = fields.One2many(comodel_name="repair.order", inverse_name="registry_id")