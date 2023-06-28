from odoo import models, fields


class MotorcycleRegistry(models.Model):
    _inherit = "motorcycle.registry"

    public = fields.Boolean(default=False)

    # Make these fields stored so we can search on them
    brand = fields.Char(store=True)
    make = fields.Char(store=True)
    rider_country_name = fields.Char(related="owner_id.country_id.name", store=True)
    rider_state_name = fields.Char(related="owner_id.state_id.name", store=True)

    def get_portal_url(self, suffix=None, report_type=None, download=None, query_string=None, anchor=None):
        self.ensure_one()
        url = f"/my/registrations/{self.id}"
        return url
