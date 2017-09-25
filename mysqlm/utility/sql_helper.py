# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:41:46 2017

@author: kuoncat
"""
import pymysql

class MySqlhelper(object):
    def __init__(self):
        pass
    def Get_dic(self,sql,params):
        conn = pymysql.connect(host='127.0.0.1',user='kuon',password='340881',db='admins')
        cur = conn.cursor()
        CountNum = cur.execute(sql,params)
        data = cur.fetchall()
        
        cur.close()
        conn.close()
        return data
    
    def Get_one(self,sql,params):
        conn = pymysql.connect(host='127.0.0.1',user='kuon',password='340881',db='admins')
        cur = conn.cursor()
        CountNum = cur.execute(sql,params)
        data = cur.fetchone()
        
        cur.close()
        conn.close()
        return data
'''
helper = MySqlhelper()
sql = 'select * from adm where id = %s'
parms =(2,)

sample = helper.Get_one(sql,parms)
print (sample)
'''