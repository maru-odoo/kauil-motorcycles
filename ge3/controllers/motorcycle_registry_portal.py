from odoo import http, _
from odoo.http import request
from odoo.addons.portal.controllers import portal
from odoo.osv.expression import OR, AND


class MotorcycleRegistryPortal(portal.CustomerPortal):

    def _get_partner_id(self):
        user_id = request.env.context.get("uid")
        partner_id = request.env["res.users"].browse([user_id]).partner_id

        return partner_id.id

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)

        visible_domain = self._get_visible_domain()
        values['registration_count'] = request.env['motorcycle.registry'].search_count(visible_domain)

        return values

    def _get_registry_searchbar_inputs(self):
        return {
            'all': {'input': 'all', 'label': _('Search in All')},
            'name': {'input': 'name', 'label': _('Search in Rider Name')},
            'state': {'input': 'state', 'label': _('Search in Rider State')},
            'country': {'input': 'country', 'label': _('Search in Rider Country')},
            'make': {'input': 'make', 'label': _('Search in Motorcycle Make')},
            'model': {'input': 'model', 'label': _('Search in Motorcycle Model')},
        }

    def _get_visible_domain(self):
        partner_id = self._get_partner_id()
        visible_domain = ['|', ('public', '=', 'True'), ('owner_id', '=', partner_id)]

        return visible_domain

    def _get_search_domain(self, search_in, search):
        search_domain = []
        if search_in in ('name', 'all'):
            search_domain = OR([search_domain, [('owner_id.display_name', 'ilike', search)]])
        if search_in in ('state', 'all'):
            search_domain = OR([search_domain, [('rider_state_name', 'ilike', search)]])
        if search_in in ('country', 'all'):
            search_domain = OR([search_domain, [('rider_country_name', 'ilike', search)]])
        if search_in in ('make', 'all'):
            search_domain = OR([search_domain, [('brand', 'ilike', search)]])
        if search_in in ('model', 'all'):
            search_domain = OR([search_domain, [('make', 'ilike', search)]])
        return search_domain

    def _get_registry_searchbar_sortings(self):
        return {
            'registry_number': {'label': _('Registry #'), 'order': 'registry_number'},
            'vin': {'label': _('VIN'), 'order': 'vin'},
            'make': {'label': _('Make'), 'order': 'make'},
            'model': {'model': _('Model'), 'order': 'model'},
        }

    @http.route('/my/registrations/<int:id>/update', type='http', auth='user', website=True)
    def portal_my_registrations_update(self, **kwargs):
        registration_id = kwargs.get("id")
        partner_id = self._get_partner_id()

        registration = request.env['motorcycle.registry'].browse([registration_id])
        if not registration.read() or registration.owner_id.id != partner_id:
            # Invalid resource
            return request.redirect(f"/my/registrations/{id}")

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
        partner_id = self._get_partner_id()

        if registration_id:
            registration = request.env['motorcycle.registry'].browse([registration_id])
            if not registration.read() or (not registration.public and registration.owner_id.id != partner_id):
                # Invalid resource
                registration = False
                owner = False
            else:
                owner = registration.owner_id.id == partner_id

            values = {
                "registration": registration,
                "default_url": "/my/registrations",
                "page_name": "registration",
                "owner": owner,
            }

            return request.render("ge3.portal_my_registration", values)
        else:
            searchbar_sortings = self._get_registry_searchbar_sortings()
            searchbar_inputs = self._get_registry_searchbar_inputs()
            sortby = kwargs.get("sortby", "registry_number")
            search_in = kwargs.get("search_in", "all")
            search = kwargs.get("search", "")

            search_domain = self._get_search_domain(search_in, search)
            visible_domain = self._get_visible_domain()
            domain = AND([search_domain, visible_domain])
            registrations = request.env['motorcycle.registry'].search(domain)

            values = {
                "registrations": registrations,
                "default_url": "/my/registrations",
                "searchbar_sortings": searchbar_sortings,
                "searchbar_inputs": searchbar_inputs,
                "sortby": sortby,
                "search": search,
                "search_in": search_in,
                "page_name": "registrations",
            }

            return request.render("ge3.portal_my_registrations", values)
