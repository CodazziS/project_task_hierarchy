from openerp.osv import fields, osv
import openerp.addons.decimal_precision as dp
from lxml import etree as ET


class project_task_hierarchy(osv.osv):
    _inherit = 'project.task'

    _columns = {
        'previous_tasks_hierarchy': fields.many2many(
            'project.task',
            'rel_task_hierarchy',
            'previous_tasks_hierarchy_id',
            'following_tasks_hierarchy_id',
            'Previous tasks'),

        'following_tasks_hierarchy': fields.many2many(
            'project.task',
            'rel_task_hierarchy',
            'following_tasks_hierarchy_id',
            'previous_tasks_hierarchy_id',
            'Following tasks'),
    }