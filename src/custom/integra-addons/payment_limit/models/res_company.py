from odoo import models, fields


class ResCompany(models.Model):
    _inherit = 'res.company'

    payment_limit_enabled = fields.Boolean(
        string='Enable Payment Limit',
        default=False,
        help='Enable or disable the payment limit feature for this company.'
    )
    payment_limit_amount = fields.Float(
        string='Payment Limit Amount',
        default=0.0,
        help='Set the maximum payment amount allowed for this company.'
    )
