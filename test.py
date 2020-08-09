# -*- coding: utf-8 -*-
''' Unittest '''

import time
from io import StringIO
import requests
import pandas as pd
import pickle
import twstock
import os
#import grs
#import unittest
#from datetime import datetime
#from types import BooleanType
#from types import NoneType

def Update_codes():
    twstock.__update_codes()

def DownloadTWSE_day():

    stock = twstock.Stock(list)
    return 1


def DownloadOTC_day():
    
    return 1

if __name__ == '__main__':

    #twstock.__update_codes()  #Update stock list per month.
    #f = open('./code.csv', 'w') #r:read only  / w:write / a:continue writing
    #f.close()
    tStart = time.time()#計時開始

    
    #Update_codes()

    #To do...
    #CodesRefine() #從TWSE&TPEX篩道只剩'股票'
    #DownloadTWSE_day()
    #DownloadOTC_day()
    
    stock = twstock.Stock('2330')
    #stock.fetch_from(2010, 1)#證交所最舊的資料
    
    year = time.localtime(time.time()).tm_year
    month = time.localtime(time.time()).tm_mon
    stock.fetch(year, month) #Cost too much time
    #stock.fetch_31()
    
    #trasfer_to_csv = pd.DataFrame(stock.data)
    

    #Read file and concat missing data
    #trasfer_to_csv.to_csv('2330.csv', mode='w')  #To check time stamp
    
    #pd.read_csv('2330.csv')
    #f.write(str(trasfer_to_csv))
    tEnd = time.time()#計時開始
    print('Cost time: %f' %(tEnd-tStart))

#To-do
"""

    https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=TAI&n=100

    t = 漲幅/跌幅 (up/down)
    e = 上市/上櫃 (TAI/TWO)
    n = 前n (30/50/100)
    
"""

    
    