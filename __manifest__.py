{
    'name': 'Desarrollo Yodeco',
    'version': '1.0',
    'summary': 'Desarrollos basicos de Yodeco',
    'description': """Modulo para agregar cambios de Yodeco""",
    'category': 'Uncategory',
    'author': 'I-SUMIT',
    'website': 'www.isumit.odoo.com',
    'depends': ['base', 'account'],
    'data': [
            "views/account_invoice_view.xml",
             ],
    'installable': True,
    'application': True,
}
