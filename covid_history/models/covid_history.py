#-*- coding: utf-8 -*-
from odoo import models, fields, api
class CovidHistory(models.Model):
    _name = 'covid.app'
    _inherit = ['covid.app']
    contacts = fields.Many2one('res.users', 'Contacto')
    symptom = fields.Selection([('leve', 'Leve'),('moderado', 'Moderado'),('grave', 'Grave')], 'Sintomas')
    name = fields.Char(help="Empleado Covid")

    def do_marcar(self):
      self.positive = True
      self.negative = False
      self.countP=1
      self.countN=0
      return True

    def do_limpiar(self):
      self.positive = False
      self.negative = True
      self.countP=0
      self.countN=1
      return True

    countP = fields.Integer('Contador Positivos', default=1)
    countN = fields.Integer('Contador Negativos', default=0)
