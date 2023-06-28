from odoo import api, models, fields

class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    repair_ids = fields.One2many(comodel_name="repair.order", inverse_name="registry_id")

    def action_view_repairs(self):
        if self.repair_ids:
            action = {
                'res_model': 'repair.order',
                'type': 'ir.actions.act_window',
            }
            if len(self.repair_ids) == 1:
                action.update({
                    'view_mode': 'form',
                    'res_id': self.repair_ids[0].id,
                })
            else:
                action.update({
                    'name': ('Repair Orders'),
                    'view_mode': 'tree,form',
                    'domain': [('id', 'in', self.repair_ids.ids)],
                })
            return action