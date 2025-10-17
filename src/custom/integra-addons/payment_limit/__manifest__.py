{
    'name': 'payment limit',
    'version': '1.0',
    'description': 'define payment limit for company',
    'summary': '',
    'author': 'REDT',
    'website': '',
    'license': 'LGPL-3',
    'category': '',
    'depends': [
        'account', 'stock'
    ],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/res_config_settings_views.xml',
        'views/account_payment_views.xml',
    ],
    'auto_install': False,
    'application': True,
}