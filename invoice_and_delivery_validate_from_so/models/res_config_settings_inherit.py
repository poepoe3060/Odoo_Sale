from odoo import api, fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    enable_invoice_only = fields.Boolean('Auto Validate Invoice',config_parameter='invoicing_and_delivery_auto_validating.enable_invoice_only_id')
    enable_delivery_only = fields.Boolean('Auto Validate Delivery',config_parameter='invoicing_and_delivery_auto_validating.enable_delivery_only_id')

