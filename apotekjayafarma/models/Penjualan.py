from decimal import DefaultContext
from unicodedata import name
from odoo import api, fields, models 
from odoo.exceptions import UserError, ValidationError


class Penjualan(models.Model):
    _name = 'apotek.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota', default=1, required=True)
    pelanggan_id = fields.Many2one(comodel_name='res.partner', string='Nama Pembeli')
    # pelanggan_id = fields.Char(string='Nama Pembeli')
    apoteker_id = fields.Many2one(comodel_name='apotek.apoteker', string='Nama Apoteker')
    tgl_penjualan = fields.Datetime(string='Tgl. Transaksi', default = fields.Datetime.now) 
    total_bayar = fields.Integer(compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(comodel_name='apotek.detailpenjualan', inverse_name='penjualan_id', string='Detail Penjualan')
    
    # No. Nota harus unik / tidak boleh sama
    @api.constrains('name')
    def _check_name_unique(self):
        name_counts = self.search_count([('name', '=', self.name), ('id', '!=', self.id)])
        print(name_counts)
        if name_counts > 0:
            raise ValidationError("No. Nota Telah ada")
    
    #untuk mengambil subtotal detail pembayaran ke form Total Pembayaran
    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['apotek.detailpenjualan'].search([('penjualan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a
    
    # # kembalikan stok apabila penjualan dibatalkan dengan method ondelete 14
    # @api.ondelete(at_uninstall=False)
    # def __ondelete_penjualan(self):
    #     if self.detailpenjualan_ids:
    #         a=[]
    #         for rec in self:
    #             a = self.env['apotek.detailpenjualan'].search([('penjualan_id','=',rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.obat_id.name) + ' ' + str(ob.qty))
    #             ob.obat_id.stok += ob.qty
    
    #kembalikan stok apabila penjualan dibatalkan dengan method unlink 
    def unlink(self):
        if self.detailpenjualan_ids:
            a=[]
            for rec in self:
                a = self.env['apotek.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.obat_id.name) + ' ' + str(ob.qty))
                ob.obat_id.stok += ob.qty
        record = super(Penjualan,self).unlink()


class DetailPenjualan(models.Model):
    _name = 'apotek.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(comodel_name='apotek.penjualan', string='Detail Penjualan')
    obat_id = fields.Many2one(comodel_name='apotek.obat', string='List Obat')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Jumlah', default=1)
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')
    
    #menampilkan hasil subtotal pada detail penjualan dari sebuah barang
    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan
            
    #ambil value harga dari model obat ke detail penjualan
    @api.onchange('obat_id')
    def _onchange_barang_id(self):
        if (self.obat_id.harga):
            self.harga_satuan = self.obat_id.harga
    
    
    #untuk mengurangi stok apabila terjadi penjualan
    @api.model
    def create(self,vals):
        record = super(DetailPenjualan,self).create(vals)
        if record.qty:
            self.env['apotek.obat'].search([('id','=',record.obat_id.id)]).write({'stok' : record.obat_id.stok - record.qty})
        return record
    
    
    #constraint pada detail penjualan 
    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
             #constraint apabila quantity tidak diisi atau kurang dari 1
            if rec.qty <1:
                raise ValidationError("Jumlah Belanja {} tidak boleh kosong".format(rec.obat_id.name))
            #constraint apabila quantity pada detail penjualan lebih dari stok
            elif (rec.obat_id.stok < rec.qty):
                raise ValidationError('Stok {} tidak mencukupi, hanya tersedia {}'.format(rec.obat_id.name,rec.obat_id.stok))
            
    
    
    
