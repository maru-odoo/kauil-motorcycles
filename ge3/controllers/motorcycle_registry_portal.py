from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal


class MotorcycleRegistryPortal(portal.CustomerPortal):

    def _get_registry_searchbar_sortings(self):
        return {
            'registry_number': {'label': _('Registry #'), 'order': 'registry_number'},
            'vin': {'label': _('VIN'), 'order': 'vin'},
            'make': {'label': _('Make'), 'order': 'make'},
            'model': {'model': _('Model'), 'order': 'model'},
        }

    @http.route(['/my/registrations', '/my/registrations/<int:id>'], type='http', auth='user', website=True)
    def portal_my_registrations(self, **kwargs):
        registration_id = kwargs.get("id")
        if registration_id:
            registration = request.env['motorcycle.registry'].browse([registration_id])

            values = {
                "registration": registration,
                "default_url": "/my/registrations",
            }

            return request.render("ge3.portal_my_registration", values)
        else:
            registrations = request.env['motorcycle.registry'].search([])
            searchbar_sortings = self._get_registry_searchbar_sortings()
            sortby = kwargs.get("sortby", "registry_number")

            values = {
                "registrations": registrations,
                "default_url": "/my/registrations",
                "searchbar_sortings": searchbar_sortings,
                "sortby": sortby,
            }

            return request.render("ge3.portal_my_registrations", values)
