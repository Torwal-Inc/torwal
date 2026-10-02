# __manifest__.py

{
    'name': 'Torwal Support',
    'version': '1.0',
    'summary': 'Quick access to the Torwal support page',
    'description': """
        Adds a "Torwal Support" entry to the Apps drawer.

        Clicking it reads the `torwal_support.url` system parameter
        (Settings > Technical > Parameters > System Parameters) and
        redirects the user to that URL (the Torwal support page by default).
    """,
    'author': 'kevin@torwal.com',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'data/torwal_support_data.xml',
        'views/torwal_support_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

