# -*- coding: utf-8 -*-
# from odoo import http


# class Webshop01(http.Controller):
#     @http.route('/webshop01/webshop01', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/webshop01/webshop01/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('webshop01.listing', {
#             'root': '/webshop01/webshop01',
#             'objects': http.request.env['webshop01.webshop01'].search([]),
#         })

#     @http.route('/webshop01/webshop01/objects/<model("webshop01.webshop01"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('webshop01.object', {
#             'object': obj
#         })
