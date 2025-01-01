# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Invocing And Delivery Auto Validating When Sale Order is Confirmed',
    'version': '1.1',
    'author': 'Pann Phyu',
    'category': 'Invoicing and Delivery',
    'summary': 'Invoicing and Delivery Management',
    'description': """
	This module contains the modification about invoicing and delivery.
    """,
    'depends':  ['base','account','stock','base_setup','sale'],
    'data': [

        'views/res_config_view_inherit.xml',

    ],

    'installable': True,
    'auto_install': False
}
