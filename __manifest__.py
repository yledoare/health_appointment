# -*- coding: utf-8 -*-
{
    'name': "Health appointment",
    'summary': "Manage you health appointment ",
    'description': """
Long description of module's purpose
    """,
    'author': "OS4B",
    'website': "https://www.os4b.bzh",

    'category': 'Appointment',
    'version': '0.5',

    'depends': [
        'base',
        'contacts',
    ],

    'data': [
        # SECURITY
        'security/ir.model.access.csv',
        # VIEWS
        'views/health_appointment_views.xml',
        # MENU
        'views/menu.xml',
        # Mail 
        'data/health_appointment_email.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',

}

