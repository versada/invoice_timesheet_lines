# -*- coding: utf-8 -*-
{
    'name': "Invoice Timesheet Lines",
    'summary': '',
    'description': 'Invoice Timesheet Lines',
    'author': "Viktoras",
    'website': "",
    'category': 'Uncategorized',
    'version': '10.0.0.1.0',
    # any module necessary for this one to work correctly
    'depends': [
        'hr_timesheet',
    ],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_analytic.xml',
        'wizards/analytic_view.xml',
    ],
}
