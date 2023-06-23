from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers import portal


class MotorcycleRegistryPortal(portal.CustomerPortal):

    @http.route(['/my/registrations', '/my/registrations/<string:id>'], type='http', auth='user', website=True)
    def portal_my_registrations(self, **kwargs):
        registration_id = kwargs.get("id")
        if registration_id:
            registration = request.env['motorcycle.registry'].browse(registration_id)
            values = {"registration": registration}

            return request.render("ge3.portal_my_registration", values)
        else:
            return request.render("ge3.portal_my_registrations")
