# -*- coding: utf-8 -*-
# from odoo import http


# class Apotekjayafarma(http.Controller):
#     @http.route('/apotekjayafarma/apotekjayafarma', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apotekjayafarma/apotekjayafarma/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('apotekjayafarma.listing', {
#             'root': '/apotekjayafarma/apotekjayafarma',
#             'objects': http.request.env['apotekjayafarma.apotekjayafarma'].search([]),
#         })

#     @http.route('/apotekjayafarma/apotekjayafarma/objects/<model("apotekjayafarma.apotekjayafarma"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apotekjayafarma.object', {
#             'object': obj
#         })
