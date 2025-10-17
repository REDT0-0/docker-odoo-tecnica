from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    payment_limit_enabled = fields.Boolean(
        related='company_id.payment_limit_enabled',
        string='Enable Payment Limit',
        readonly=False,
        help='Enable or disable the payment limit feature for the current company.'
    )
    payment_limit_amount = fields.Float(
        related='company_id.payment_limit_amount',
        string='Payment Limit Amount',
        readonly=False,
        help='Set the maximum payment amount allowed for the current company.'
    )

    @api.constrains('payment_limit_amount')
    def _check_payment_limit_amount(self):
        for rec in self:
            if rec.payment_limit_amount < 0:
                raise UserError(_('Payment limit amount cannot be negative.'))
