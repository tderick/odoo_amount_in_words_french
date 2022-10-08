# -*- coding: utf-8 -*-
# from odoo import http


# class OdooAmountInWordsFrench(http.Controller):
#     @http.route('/odoo_amount_in_words_french/odoo_amount_in_words_french/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_amount_in_words_french/odoo_amount_in_words_french/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_amount_in_words_french.listing', {
#             'root': '/odoo_amount_in_words_french/odoo_amount_in_words_french',
#             'objects': http.request.env['odoo_amount_in_words_french.odoo_amount_in_words_french'].search([]),
#         })

#     @http.route('/odoo_amount_in_words_french/odoo_amount_in_words_french/objects/<model("odoo_amount_in_words_french.odoo_amount_in_words_french"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_amount_in_words_french.object', {
#             'object': obj
#         })
