
from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = 'account.move'

    amount_words = fields.Char(string="Montant total en lettres: ",
                               help="Le montant total en lettres est généré automatiquement par le système")
