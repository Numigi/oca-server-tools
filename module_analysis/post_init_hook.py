# Copyright (C) 2019-Today: GRAP (<http://www.grap.coop/>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import SUPERUSER_ID, api, tools


def analyse_installed_modules(cr, registry):
    if tools.config["test_enable"]:
        return
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        installed_modules = env["ir.module.module"].search(
            ["|", ("state", "=", "installed"), ("name", "=", "module_analysis")]
        )
        installed_modules.button_analyse_code()
