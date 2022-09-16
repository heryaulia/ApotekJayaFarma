# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request
import json


class Apotekjayafarma(http.Controller):
    @http.route('/apotekjayafarma/getobat', auth='public', method=['GET'])
    def index(self, **kw):
        obat = request.env['apotek.obat'].search([])
        isi = []
        for bb in obat:
            isi.append({
                'id_obat' : bb.id_obat,
                'nama_obat' : bb.name,
                # 'kategori_obat' : bb.kategoriobat_id,
                'harga_obat' : bb.harga,
                'stok' : bb.stok,
                # 'stok' : bb.supplier_id
            })
        return json.dumps(isi)

    @http.route('/apotekjayafarma/getsupplier', auth='public', method=['GET'])
    def index(self, **kw):
        supplier = request.env['apotek.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_supplier' : s.name,
                'alamat' : s.alamat,
                'nomor_hp' : s.no_hp,
                # 'obat' : s.obat_id,
            })
        return json.dumps(sup)

    @http.route('/apotekjayafarma/apotekjayafarma/objects/<model("apotekjayafarma.apotekjayafarma"):obj>', auth='public')
    def object(self, obj, **kw):
        return http.request.render('apotekjayafarma.object', {
            'object': obj
        })
