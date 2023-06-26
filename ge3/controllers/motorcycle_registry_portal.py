from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal


class MotorcycleRegistryPortal(portal.CustomerPortal):

    @http.route(['/my/registrations', '/my/registrations/<int:id>'], type='http', auth='user', website=True)
    def portal_my_registrations(self, **kwargs):
        registration_id = kwargs.get("id")
        if registration_id:
            registration = request.env['motorcycle.registry'].browse([registration_id])
            return request.render("ge3.portal_my_registration", {"registration": registration})
        else:
            registrations = request.env['motorcycle.registry'].search([])
            return request.render("ge3.portal_my_registrations", {"registrations": registrations})
