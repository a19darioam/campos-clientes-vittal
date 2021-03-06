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
    'version': '0.34',

    #Comentario de prueba
    
    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'crm',
        'l10n_mx',
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
        'data/sat.colonia.csv',
        'data/sat.municipio.csv',
        'data/sat.estado.csv',
        'data/sat.pais.csv',
        'data/sat.uso.csv',
        'data/sat.pagos.csv',
        'views/sat_colonia_form.xml',
        'views/sat_municipio_form.xml',
        'views/sat_estado_form.xml',
        'views/sat_pais_form.xml',
        'views/sat_uso_form.xml',
        'views/sat_pagos_form.xml',
        'views/business_type_view.xml',
        'views/account_invoice_form.xml',
        'views/partner_member_form.xml',
        'views/family_member_tree.xml',
        'views/family_member_action.xml',
        'views/company_member_tree.xml',
        'views/company_member_action.xml',
        'views/product_template_form.xml',
        'views/partner_address_form.xml',
        'views/view_partner_form.xml',
        'views/view_product_filter.xml',
        'views/sale_order_form.xml',
        'views/sale_order_filter.xml',
        'views/client_tree.xml',
        'views/client_action.xml',
        'views/client_filter.xml',
        'views/sales_menu.xml',
        'views/static_assets.xml',
    ],
    # styles
    'css': [
        'static/src/css/custom.css'
    ],
}
