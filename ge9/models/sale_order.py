from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_new_customer = fields.Boolean("New Customer", default=False, compute="_compute_if_new_customer")

    @api.onchange('partner_id')
    def _compute_if_new_customer(self):
        for customer in self:
            # Iterating through the sale orders related to a customer
            for order in customer.partner_id.sale_order_ids:
                # Get the order -> order.line
                # -> Get the product id from the order.line
                # -> Get the detailed type from the product id
                # Check if the detailed type is motorcycle
                for order_line in order.order_line:
                    if order_line.product_template_id and  order_line.product_template_id.detailed_type == "motorcycle":
                        self.is_new_customer = False
                        self.env.ref('ge9.new_customer_pricelist').active = False
                        return
        if self.partner_id:
            self.env.ref('ge9.new_customer_pricelist').active = True
            self.is_new_customer = True

    @api.depends('pricelist_id')
    def motorcycle_apply_discount_button(self):
        self.pricelist_id = self.env.ref('ge9.new_customer_pricelist')
        super().action_update_prices()