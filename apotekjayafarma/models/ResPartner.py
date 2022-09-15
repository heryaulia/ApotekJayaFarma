from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    
    is_pelanggan = fields.Boolean(string='is_Pelanggan')
    
    