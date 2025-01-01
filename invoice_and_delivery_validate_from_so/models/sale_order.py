from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def validate_deliver_order(self, picking_ids):
        if picking_ids:
            picking = picking_ids[0]
            for move_line in picking.move_ids_without_package:
                move_line.quantity_done = move_line.product_uom_qty
            picking.action_assign()
            picking.button_validate()

    def check_product_stock(self, order_line):
        for line in order_line:
            quant = self.env['stock.quant'].search([
                ('product_id', '=', line.product_id.id),
                ('location_id', '=', line.order_id.warehouse_id.lot_stock_id.id)
            ])
            total_quantity = sum(quant.mapped('quantity'))
            desired_quantity = line.product_uom_qty
            if total_quantity < desired_quantity and line.product_id.type == 'product':
                return False
            else:
                return True
                

    def action_confirm(self):
        opt_invoice = self.env['ir.config_parameter'].sudo().get_param(
            'invoicing_and_delivery_auto_validating.enable_invoice_only_id')
        opt_delivery = self.env['ir.config_parameter'].sudo().get_param(
            'invoicing_and_delivery_auto_validating.enable_delivery_only_id')

        res = super(SaleOrder, self).action_confirm()
        if opt_delivery:

            check_status = self.check_product_stock(self.order_line)
            if check_status == True:
                self.validate_deliver_order(self.picking_ids)

        if opt_invoice:
            invoice = self._create_invoices()
            invoice.action_post()

        return res
