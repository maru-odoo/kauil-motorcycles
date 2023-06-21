from odoo import models, fields


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    lot_ids = fields.One2many("stock.lot", inverse_name="registry")
