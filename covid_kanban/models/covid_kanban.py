from odoo import models, fields
class CovidKanban(models.Model):
    _inherit = 'covid.app'
    priority = fields.Selection([
                                ('0','Leve'),
                                ('1','Moderado'),
                                ('2','Grave')],
                                'Sintomas',default='1')
    kanban_state = fields.Selection([
                                ('normal', 'Positivo'),
                                ('blocked', 'Cuarentena'),
                                ('done', 'Negativo')],
                                'Estado Empleado', default='normal')
