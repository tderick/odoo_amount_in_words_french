# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo_amount_in_words_french(models.Model):
#     _name = 'odoo_amount_in_words_french.odoo_amount_in_words_french'
#     _description = 'odoo_amount_in_words_french.odoo_amount_in_words_french'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
