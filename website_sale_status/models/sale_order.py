# -*- coding: utf-8 -*-
from odoo import api, fields, models


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    active = fields.Boolean(
        string="Active",
        default=True,
        copy=False,
    )