from odoo import models, fields, api, tools


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.model
    def _get_default_category_id(self):
        if self.detailed_type == "motorcycle":
            return self.env.ref('product.product_category_motorcycles')
        return super()._get_default_category_id