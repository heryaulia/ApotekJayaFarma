# -*- coding: utf-8 -*-
{
    'name': "apotekjayafarma",

    'summary': """
        odoo module for pharmacy store""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/kategori_obat_view.xml',
        'views/obat_view.xml',
        'views/supplier_view.xml',
        'views/penjualan_view.xml',
        'views/person_view.xml',
        'views/dokter_view.xml',
        'views/apoteker_view.xml',
        'views/pelanggan_view.xml',
        'report/report.xml',
        'report/print_faktur_penjualan.xml',
        'wizard/import_obat_wizard_view.xml',
        'wizard/import_supplier_wizard_view.xml',
        
        
        
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
