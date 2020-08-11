# -*- coding: utf-8 -*-
''' Unittest '''

import time
import random
from io import StringIO
from collections import namedtuple

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
    df = pd.read_csv('twstock_list.csv')
    
    stock_list = df.code
    stock_market = df.market
    count = 0

    year = time.localtime(time.time()).tm_year
    month = time.localtime(time.time()).tm_mon
    print(type(stock_list[0]))
    #for i in range(len(stock_list)):
    for i in range(3):
        if stock_market[i] == '上市':    
            
            print(stock_list[i])
            stock = twstock.Stock(str(stock_list[i]))
            stock.fetch_today()
            df = pd.DataFrame(stock.data)
            #df.columns = str(stock_list[i])
            df.T.to_csv('today.csv', mode='a', header=False, index_label=str(stock_list[i]))   
            time.sleep(randon.randint(5,8))
    return 1


def DownloadOTC_day():
    return 1

def test_func():
    stock = twstock.Stock('6215')
    year = time.localtime(time.time()).tm_year
    month = time.localtime(time.time()).tm_mon
    stock.fetch_today()
    
    
    NEW_DATATUPLE = namedtuple('Data', ['codes', 'date', 'capacity', 'turnover', 'open',
                                'high', 'low', 'close', 'change', 'transaction'])
    new_data = NEW_DATATUPLE(stock.sid, stock.data[0], stock.data[1], stock.data[2], stock.data[3], stock.data[4], stock.data[5], stock.data[6], stock.data[7], stock.data[8])
    df = pd.DataFrame(new_data)
    
    print(df)
    df.T.to_csv('2330.csv', mode='a', header=False)
    #print(type(stock.data))
    #Read file and concat missing data
    #Check missing days
    #Insert missing days' data to csv
    #trasfer_to_csv.to_csv('2330.csv', mode='a')  #To check time stamp
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
    test_func()
    
    #DownloadOTC_day()
    
    
    #stock.fetch_from(2010, 1)#證交所最舊的資料
    #stock.fetch(year, month) #Cost too much time
    
#    stock.fetch_31()
#    trasfer_to_csv = pd.DataFrame(stock.data)
#    trasfer_to_csv.to_csv('2330.csv', mode='w')

#Good
    
    #df = df.DataFrame.append()
    
    #cs = pd.read_csv('%d.csv',%sotck_num)
    #cs = cs.DataFrame.append(stock.data)
    #cs.insert(stock.data[0], stock.data[1], stock.data[2], stock.data[3], stock.data[4], stock.data[5], stock.data[6], stock.data[7], stock.data[8])
    #cs.to_csv('2330.csv', mode='w')
    

    
    tEnd = time.time()#計時開始
    print('Cost time: %f' %(tEnd-tStart))

#To-do
"""

    https://tw.stock.yahoo.com/d/i/rank.php?t=up&e=TAI&n=100

    t = 漲幅/跌幅 (up/down)
    e = 上市/上櫃 (TAI/TWO)
    n = 前n (30/50/100)
    
"""

    
    