# Copyright 2013-2020 Camptocamp SA
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html)

import logging

from odoo import fields, models


class QueueJobTransaction(models.Model):

    _name = "queue.job.transaction"
    _description = "Queue Job Database Transaction IDs for running jobs"
    _rec_name = "db_txid"

    queue_job_id = fields.Many2one(comodel_name="queue.job")
    db_txid = fields.Char(string="Database transaction ID")
