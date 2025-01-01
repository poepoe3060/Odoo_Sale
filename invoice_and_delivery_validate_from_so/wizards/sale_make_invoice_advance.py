from odoo import api, fields, models, _
from odoo.exceptions import UserError,ValidationError


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = "sale.advance.payment.inv"

    def create_invoices(self):
        if self.env['ir.config_parameter'].sudo().get_param('invoicing_and_delivery_auto_validating.enable_delivery_only_id'):
            sale_orders = self.env['sale.order'].browse(self._context.get('active_ids', []))
            result = True
            for line in sale_orders.order_line:
                if line.qty_delivered != line.product_uom_qty:
                    result = False
                    break
            if not result:
                raise ValidationError(_("Not enough product quantity available in the warehouse."))
        res = super(SaleAdvancePaymentInv, self).create_invoices()
        return res





