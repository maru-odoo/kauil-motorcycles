from odoo import models, fields, api
from odoo.exceptions import ValidationError


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    lot_ids = fields.One2many("stock.lot", inverse_name="registry_id")
    lot_id = fields.Many2one("stock.lot", compute="_compute_lot_id")

    @api.constrains("lot_ids")
    def _check_lot_ids(self):
        lots = [x for x in self if x.lot_ids]
        if len(lots) > 1:
            raise ValidationError('Odoopsie! A registered motorcycle can only belong to one lot.')

    def _compute_lot_id(self):
        if len(self.lot_ids) > 0:
            self.lot_id = self.lot_ids[0]
        else:
            self.lot_id = False
