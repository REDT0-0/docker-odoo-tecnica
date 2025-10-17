from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)


class AccountPayment(models.Model):
    _inherit = "account.payment"

    validated_by_finance = fields.Boolean(
        string="Validated by Finance",
        default=False,
        help="Indicates whether the payment has been validated by the finance department.",
    )

    required_finance_approval = fields.Boolean(
        string="Requires Finance Approval",
        compute="_compute_required_finance_approval",
        store=True,
        help="Indicates whether the payment requires approval from the finance department.",
    )

    @api.depends("amount")
    def _compute_required_finance_approval(self):
        for payment in self:
            company = payment.company_id
            payment.required_finance_approval = (
                company.payment_limit_enabled
                and payment.amount > company.payment_limit_amount
            )

    def action_post(self):
        for pay in self:
            if pay.required_finance_approval and not pay.validated_by_finance:
                return {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "title": _("Finance approval required"),
                        "message": _(
                            "The payment exceeds the limit and must be validated by Finance before it can be posted."
                        ),
                        "type": "warning",
                        "sticky": False,
                    },
                }
            else:
                pay.validated_by_finance = True
        return super(AccountPayment, self).action_post()

    def action_draft(self):
        for pay in self:
            pay.validated_by_finance = False
        return super(AccountPayment, self).action_draft()

    def action_validate_by_finance(self):
        for pay in self:
            pay.validated_by_finance = True
            pay.action_post()
