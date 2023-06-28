from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"
    invoice_ids= fields.Char(comodel_name="account.move.line",inverse_name="lot_id")