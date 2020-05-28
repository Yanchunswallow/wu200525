# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class Course(models.Model):
    _name = 'openacademy.course'
    _description ='科目'
    
    name = fields.Char(String='标题', required=True)
    description = fields.Text(String='描述')
    
    responsible_id = fields.Many2one('openacademy.partner', ondelete='set null', string='负责人')
    session_ids = fields.One2many('openacademy.session', 'course_id', string='课程')
    
    
    level = fields.Selection([('easy',"简单"),('medium','中等'),('hard','困难')], string="难度系数")
    
    #responsible_id = fields.Many2one('openacnademy.parter', ondelete='set null', string='')
    
class Sessioin(models.Model):
    _name = 'openacademy.session'
    _description ='课程'
    
    name = fields.Char(String='课程名称', required=True)
    description = fields.Text(String='描述')
    
    
    start_date = fields.Date(default=fields.Date.context_today, string='开始日期')
    end_date = fields.Date(default=fields.Date.today, string='结束日期')
    
    duration = fields.Float(digits=(6,2), help='持续时间（日）', default=1)
    
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string='负责人', required=True)
    
#     attendess_count = fileds.Integer(compute='get_attendees_count', store=True)
    attendess_count = fields.Integer(string="参与人数")


    
class Parter(models.Model):
    _name = 'openacademy.partner'
    _description ='老师'
    
    name = fields.Char(String='老师姓名', required=True)
   
    
    