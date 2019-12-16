# -*- coding: utf-8 -*-
from odoo import http

# class Notulensi(http.Controller):
#     @http.route('/notulensi/notulensi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/notulensi/notulensi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('notulensi.listing', {
#             'root': '/notulensi/notulensi',
#             'objects': http.request.env['notulensi.notulensi'].search([]),
#         })

#     @http.route('/notulensi/notulensi/objects/<model("notulensi.notulensi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('notulensi.object', {
#             'object': obj
#         })