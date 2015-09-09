# -*- coding: utf-8 -*-

from openerp import models, fields, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do task'
    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
