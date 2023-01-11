from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    ultima_vendita = fields.Float(
        string="Ultima vendita"
    )

