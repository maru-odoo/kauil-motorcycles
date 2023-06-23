from odoo import api, fields, models

class Product_ABC(models.Model):
    _inherit = 'product.template'
    

    """
    name = fields.Char("Name", index='trigram', translate=True, compute="_compute_motorcycle_name", required=True, store 
    
    
    
    = True, readonly=False)   # , compute="_compute_name",


    @api.depends('year','make','model')
    def _compute_motorcycle_name(self):
        print("Method Entered")
        for product in self:
            print("before, the product name is", product.name)
            if product.detailed_type == "motorcycle":
                product.name = f"{product.year} {product.make} {product.model}"
            else:
                product.name = product.name
    
    """
    name = fields.Char("Name", index='trigram', translate=True, compute="_compute_motorcycle_name", required=True, store = True, readonly=False)   # , compute="_compute_name",
    # Store = True, going to be stored in the database as a value

    @api.depends('year','make','model')
    def _compute_motorcycle_name(self):
        print("Method Entered")
        for product in self:
            print("before, the product name is", product.name)
            if product.detailed_type == "motorcycle":
                product.name = f"{product.year} {product.make} {product.model}"
            else:
                product.name = product.name