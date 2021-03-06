# -*- coding: utf-8 -*-
{
    'name': "Inovice and Payments",

    'summary': """Inovice and Payments""",

    'description': """
        CS Invoice Number module for managing:
            - CS number on the invoice
            - CS number on the invoice print
            - Phone number on Invoice
            - Phone number on Print
            - Mobile number on Invoice
            - Mobile number on Print
            - NTN number on Invoice
            - NTN number on Print
            - GST number on Invoice
            - GST number on Print
    """,

    'author': "Team Emotive Labs",
    'website': "www.emotivelabs.ca",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Mutual',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'mutual_invoice_view.xml',
        'journal_entry_view.xml'
    ],

}