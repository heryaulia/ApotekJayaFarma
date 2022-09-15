from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'apotek.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Supplier', required=True)
    alamat = fields.Char(string='Alamat')
    no_hp = fields.Char(string='No. Hp')
    obat_id = fields.Many2many(comodel_name='apotek.obat', string='Obat')
    
    
    