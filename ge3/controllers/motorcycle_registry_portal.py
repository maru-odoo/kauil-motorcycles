from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal


class MotorcycleRegistryPortal(portal.CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        values['registration_count'] = request.env['motorcycle.registry'].search_count([])

        return values

    def _get_registry_searchbar_sortings(self):
        return {
            'registry_number': {'label': _('Registry #'), 'order': 'registry_number'},
            'vin': {'label': _('VIN'), 'order': 'vin'},
            'make': {'label': _('Make'), 'order': 'make'},
            'model': {'model': _('Model'), 'order': 'model'},
        }

    @http.route('/my/registrations/<int:id>/update', type='http', auth='user', website=True)
    def portal_my_registrations_update(self, **kwargs):
        try:
            current_mileage = float(kwargs.get("current_mileage", 0))
            public = True if kwargs.get("public") == "on" else False
        except ValueError:
            # An invalid value was received in the request, so exit early
            return request.redirect(f"/my/registrations/{id}")

        id = kwargs.get('id')
        values = {"current_mileage": current_mileage, "public": public}
        request.env['motorcycle.registry'].browse(id).write(values)

        return request.redirect(f"/my/registrations/{id}")

    @http.route(['/my/registrations', '/my/registrations/<int:id>'], type='http', auth='user', website=True)
    def portal_my_registrations(self, **kwargs):
        registration_id = kwargs.get("id")
        if registration_id:
            registration = request.env['motorcycle.registry'].browse([registration_id])
            if not registration.read():
                registration = False

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
