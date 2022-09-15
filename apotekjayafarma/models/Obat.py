from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Obat(models.Model):
    _name = 'apotek.obat'
    _description = 'New Description'

    name = fields.Char('Nama Obat')
    id_obat = fields.Char(string='ID Obat', required=True)
    harga = fields.Integer(string='Harga Obat')
    stok = fields.Integer(string='Stok')
    kategoriobat_id = fields.Many2one(comodel_name='apotek.kategoriobat', string='Kategori Obat', ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='apotek.supplier', string='Supplier')

    
    

    