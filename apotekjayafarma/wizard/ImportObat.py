from asyncore import write
from odoo import models, fields, api

class Obat(models.TransientModel):
    _name = 'apotek.importobat'
    
    obat_id = fields.Many2one(comodel_name='apotek.obat', string='Import Obat')
    jumlah = fields.Integer(string='Jumlah', required=True)
    
    
    # function for add stock in obat_id with wizard import obat
    def btn_import_obat(self):
        for rec in self:
            self.env['apotek.obat'].search([('id', '=', rec.obat_id.id)]).write({'stok': rec.obat_id.stok + rec.jumlah})
            