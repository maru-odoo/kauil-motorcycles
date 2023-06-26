from odoo import models


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    def get_portal_url(self, suffix=None, report_type=None, download=None, query_string=None, anchor=None):
        self.ensure_one()
        url = f"/my/registrations/{self.id}"
        return url
