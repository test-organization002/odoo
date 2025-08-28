{
    'name': 'Terminal Yönetim Sistemi',
    'version': '16.0.1',
    'category': 'Sales',
    'summary': 'Terminal kayıtlarını yönetmek için modül',
    'description': """
        Bu modül terminal kayıtlarını görüntüleme, düzenleme ve silme işlemlerini sağlar.
        Özellikler:
        - Terminal kayıtlarını listeleme
        - Yeni terminal ekleme
        - Terminal bilgilerini düzenleme
        - Terminal kayıtlarını silme
        - Terminal durumu takibi
        - Banka bilgileri yönetimi
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/terminal_views.xml',
        'views/menu_views.xml',
        'data/demo_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'terminal_management/static/src/css/terminal.css',
        ],
    },
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
