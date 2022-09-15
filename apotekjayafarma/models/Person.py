from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Person(models.Model):
    _name = 'apotek.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    no_hp = fields.Char(string='No Hp')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Date(string='Tanggal Lahir')


class Dokter(models.Model):
    _name = 'apotek.dokter'
    _inherit = 'apotek.person'
    _description = 'New Description'
    id_dokter = fields.Char(string='Dokter ID')

class Apoteker(models.Model):
    _name = 'apotek.apoteker'
    _inherit = 'apotek.person'
    _description = 'New Description'
    id_apoteker = fields.Char(string='Apoteker ID')
    
    # apoteker id to be unique
    @api.constrains('id_apoteker')
    def _check_name_unique(self):
        id_apoteker_counts = self.search_count([('id_apoteker', '=', self.id_apoteker), ('id', '!=', self.id)])
        if id_apoteker_counts > 0:
            raise ValidationError("Id Apoteker tidak boleh sama")