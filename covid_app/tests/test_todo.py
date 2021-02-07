# -*- coding: utf-8 -*-
from openerp.tests.common import TransactionCase
class TestCovid(TransactionCase):
    def test_create(self):
        "Registro de prueba"
        Todo = self.env['covid.app']
        task = Todo.create({'name': 'Empleado Prueba'})
        self.assertEqual(task.positive, True)
	self.assertEqual(task.department, 'Prueba')

