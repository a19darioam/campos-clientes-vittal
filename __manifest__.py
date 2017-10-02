# -*- coding: utf-8 -*-
{
    'name': "Campos de Clientes",

    'summary': """Campos personalizados para clientes de Vittal.""",

    'description': """
        Campos personalizados para clientes de Vittal. Depende del modulo de ventas.
    """,

    'author': "Prescrypto",
    'website': "http://www.prescrypto.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Specific Industry Applications',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm',
        'sale',
        'account',
        'account_accountant',
        'board',
        'contacts'
    ],

    # not a module
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/view_partner_form.xml',
        'views/view_partner_filter.xml',
        'views/view_product_filter.xml',
        'views/sale_order_form.xml',
        'views/sale_order_filter.xml',
        'views/quotation_filter.xml',
        'views/subscription_filter.xml',
        'views/subscription_menu.xml',
        'views/templates.xml',
    ],
    # styles
    'css': [
        'static/src/css/custom.css'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
