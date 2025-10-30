# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
import calendar
import dateutil

from pprint import pprint

class HealthAppointment(models.Model):
    _name = 'health.appointment'
    _description = 'Health Appointment'
    _sql_constraints = [
#        ('unique_name', 'UNIQUE(name) ', 'The name of the property must be unique')
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
    last_date = fields.Date('Last date', default=datetime.datetime.today())
    next_date = fields.Date('Next date')
    type = fields.Selection([
        ('dental', 'Dentiste'),
        ('foot', 'Podologue'),
        ('other', 'Autre'),
    ], string='type')

    next_appointment = fields.Date(compute="_compute_next_appointment")
    email = fields.Char(string='Email')
    # email = fields.Char(string='Email', required=True)

    @api.depends("last_date")
    def _compute_next_appointment(self):
        for record in self:
             sourcedate=record.last_date
             #if not sourcedate:
               #pprint(vars())
             #  record.next_appointment=datetime.datetime.today()
             #else:  
             months=record.period
             month = sourcedate.month - 1 + months
             year = sourcedate.year + month // 12
             month = month % 12 + 1
             day = min(sourcedate.day, calendar.monthrange(year,month)[1])
             #pprint(vars())
             record.next_appointment=datetime.date(year, month, day)

    def action_send_email(self):
      # OK template = self.env.ref('auth_signup.mail_template_user_signup_account_created')
      #raise UserError("FIXME")
      template = self.env.ref('health_appointment.mail_template_health_appointment')
      if template:
            # Send the email using the template
        template.send_mail(self.id, force_send=True)
      else:
        raise UserError("Mail Template not found. Please check the template.")
