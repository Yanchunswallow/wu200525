# -*- coding: utf-8 -*-
from odoo import http

# class Testacademy(http.Controller):
#     @http.route('/testacademy/testacademy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testacademy/testacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testacademy.listing', {
#             'root': '/testacademy/testacademy',
#             'objects': http.request.env['testacademy.testacademy'].search([]),
#         })

#     @http.route('/testacademy/testacademy/objects/<model("testacademy.testacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testacademy.object', {
#             'object': obj
#         })