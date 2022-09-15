from odoo import models, fields, api

class KategoriObat(models.Model):
    _name = 'apotek.kategoriobat'
    _description = 'New Description'

    name = fields.Char('Nama Katagori Obat')
    kode_kateg = fields.Char(string='Kode Kategori')
    obat_ids = fields.One2many(comodel_name='apotek.obat', inverse_name='kategoriobat_id', string='Obat')

    