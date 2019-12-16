# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Notes(models.Model):
    _name = 'notulensi.notes'
    STATE = (
        ("draft", "Draft"),
        ("accept", "Accept"),
    )

    state = fields.Selection(STATE, required=True, readonly=True, copy=False, default='draft' )
    name = fields.Char()
    description = fields.Text()
    task_ids =  fields.One2many('notulensi.assignment', 'notes_id', string="Assignment")

    @api.multi
    def action_accept(self):
        self.state = "accept"

class NotesTask(models.Model):
    _name = "notulensi.task"

    name = fields.Char(string="Task")

class NotesAssignment(models.Model):
    _name = "notulensi.assignment"

    task_id = fields.Many2one('notulensi.task', string='Task',)
    user = fields.Many2one('res.users', string='User',)
    notes_id = fields.Many2one('notulensi.notes', string='Notes',)
