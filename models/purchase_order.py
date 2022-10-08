from odoo import api, fields, models

# Display amount in words in Sale order


class PurchaseOrder(models.Model):

    _inherit = 'purchase.order'

    amount_words = fields.Char(string="Montant total en lettres: ",
                               help="Le montant total en lettres est généré automatiquement par le système")
