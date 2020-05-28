# -*- coding: utf-8 -*-
from odoo import http

# class Myapp(http.Controller):
#     @http.route('/myapp/myapp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myapp/myapp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('myapp.listing', {
#             'root': '/myapp/myapp',
#             'objects': http.request.env['myapp.myapp'].search([]),
#         })

#     @http.route('/myapp/myapp/objects/<model("myapp.myapp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myapp.object', {
#             'object': obj
#         })