from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    warehouse_id = fields.Many2one(compute='_compute_warehouse_id', required=True, store = True, readonly=False)    

    @api.depends('partner_id')
    def _compute_warehouse_id(self):
        west_states = ["ND","SD","NE","KS","OK","TX","MT","WY","CO","NM","ID","UT","AZ","NV","WA","OR","CA"]
        east_states = ["ME","VT","NH","MA","CT","RI","NJ","MD","DE","NY","PA","OH","MI","IN","IL","WI","VA","WV","NC","KY","TN","SC","GA","AL","MS","FL","MN","IA","MO","AR", "LA"]

        for order in self:
            #print(order.partner_id.read())
            if order.partner_id.country_id.code == "US":
                #print(order.partner_id.state_id.read())
                print(order.partner_id.state_id.code)

                if order.partner_id.state_id.code in west_states:
                    #print("SF warehouse")
                    warehouse = self.env["stock.warehouse"].search([('name','=','San Francisco Dealership')])
                    #print(warehouse.read())
                    order.warehouse_id = warehouse
                elif order.partner_id.state_id.code in east_states:
                    warehouse = self.env["stock.warehouse"].search([('name','=','Buffalo Dealership')])
                    #print(warehouse.read())
                    #print("BU warehouse")
                    order.warehouse_id = warehouse
                
                print(order.warehouse_id)
            else:
                #print(order.warehouse_id.read())
                order.warehouse_id = order.warehouse_id
        