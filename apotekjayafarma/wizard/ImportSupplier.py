from asyncore import write
from odoo import models, fields, api

class Supplier(models.TransientModel):
    _name = 'apotek.importsupplier'
    
    namasupplier = fields.Char(string='Nama Supplier')
    no_hp = fields.Char(string='No. Hp')
    alamatsupplier = fields.Char(string='Alamat')
    supplyobat_ids = fields.Many2many(comodel_name='apotek.obat', string='Supply Obat')
    
    
    
    #function to create new suuplier form wizard import supplier
    def btn_import_supplier(self):
        vals = {
            'name': self.namasupplier,
            'alamat': self.alamatsupplier,
            'no_hp': self.no_hp,
            'obat_id' : self.supplyobat_ids
        }
        self.env['apotek.supplier'].create(vals)