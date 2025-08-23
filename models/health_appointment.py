# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HealthAppointment(models.Model):
    _name = 'health.appointment'
    _description = 'Health Appointment'
    _sql_constraints = [
        ('unique_name', 'UNIQUE(name) ', 'The name of the property must be unique')
    ]

    name = fields.Char(string='Name', required=True)
    description = fields.Text(
        string='Description',
        translate=True,
    )
    contact_id = fields.Many2one(
        'res.partner',
        string='Owner',
        required=False
    )
    period = fields.Float('Period')
    type = fields.Selection([
        ('dental', 'Dentiste'),
        ('foot', 'Podologue'),
        ('other', 'Autre'),
    ], string='type')
