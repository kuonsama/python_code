# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 19:40:32 2017

@author: kuoncat
"""
from model.adm import Adm

def main():
    user = input('USER: ')
    password = int(input('PASSWORD: '))
    adm_o=Adm()
    res = adm_o.Check_log(user,password)
    
    if res :
        print('welcome')
    else:
        print('get out')
if __name__=='__main__':
    main()