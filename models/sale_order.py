from odoo import api, fields, models

# Display amount in words in Sale order


class SaleOrder(models.Model):

    _inherit = 'sale.order'

    def _compute_amount2words(self):
        for rec in self:
            rec.amount_words = str(
                rec.currency_id.amount_to_text(rec.amount_total))

    amount_words = fields.Char(string="Montant total en lettres: ",
                               help="Le montant total en lettres est généré automatiquement par le système")
