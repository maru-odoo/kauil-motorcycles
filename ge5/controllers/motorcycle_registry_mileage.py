from odoo import http
from odoo.http import request


class MotorcycleRegistryMileage(http.Controller):
    @http.route(["/mileage"], type="json", auth="public")
    def mileage(self):
        registries = request.env['motorcycle.registry'].search([])
        mileage = sum(registries.mapped('current_mileage'))
        return str(mileage)
