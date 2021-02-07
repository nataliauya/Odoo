# -*- coding: utf-8 -*-
from odoo import models, fields

class CovidApp(models.Model):
   _name = 'covid.app'
   _description = 'Covid App'
   name = fields.Char('Empleado', required=True)
   department = fields.Char('Departamento', required=True)
   positive = fields.Boolean('Positivo')
   negative = fields.Boolean('Negativo', default=True)
   date_test = fields.Date('Fecha del test', required=True)

   def do_marcar(self):
      self.positive = True
      self.negative = False
      return True

   def do_limpiar(self):
      self.positive = False
      self.negative = True
      return True
