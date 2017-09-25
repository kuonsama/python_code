# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:08:51 2017

@author: kuoncat
"""

from utility import sql_helper

class Adm(object):
    def __init__(self):
        self.__help = sql_helper.MySqlhelper()
    def get_name(self,id):
        sql = 'select * from adm where name =%s'
        params = (id,)
        return self.__help.Get_one(sql,params)
    
    def Check_log(self,id,pwd):
        sql ='select * from adm where (name =%s and pwd =%s)'
        params = (id,pwd,)
        return self.__help.Get_one(sql,params)