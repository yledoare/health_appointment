# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import *
from dateutil.relativedelta import *
import datetime
import dateutil

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
        string='Contact',
        required=False
    )
    period = fields.Integer('Period (month)', default="12")
    last_date = fields.Date('Last date')
    next_date = fields.Date('Next date')
    type = fields.Selection([
        ('dental', 'Dentiste'),
        ('foot', 'Podologue'),
        ('other', 'Autre'),
    ], string='type')

    next_appointment = fields.Date(compute="_compute_next_appointment")

    @api.depends("last_date")
    def _compute_next_appointment(self):
        for record in self:
            #record.total = record.last_date + dateutil.relativedelta.relativedelta(days=1)
            #record.total = date.today() + dateutil.relativedelta.relativedelta(days=1)
            #record.total =  last_date + dateutil.relativedelta.relativedelta(month=12)
            record.next_appointment = date.today() + dateutil.relativedelta.relativedelta(month=12)
