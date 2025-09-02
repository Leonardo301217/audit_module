{
    'name': 'Módulo de Auditoría Automática',
    'version': '1.0',
    'category': 'Accounting',
    'summary': 'Auditoría automática de procesos críticos, financieros y logísticos',
    'description': """
        Este módulo registra automáticamente las acciones en ventas, finanzas e inventario.
    """,
    'depends': ['base', 'sale', 'account', 'stock'],
    'data': [
        'views/audit_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}