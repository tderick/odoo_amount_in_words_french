# -*- coding: utf-8 -*-
{
    'name': "odoo_amount_in_words_french",

    'summary': """Traduit *Total amount in words:* présent dans le module *odoo_amount_in_words* in français""",


    'author': "Derick TEMFACK",
    'website': "https://github.com/tderick/odoo_amount_in_words_french",
    'category': 'Uncategorized',
    'application': False,
    'version': '0.1',
    'licence': 'AGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['odoo_amount_in_words'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

}
