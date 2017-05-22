#!usr/bin/env python
#-*- coding:utf8 -*-

import xlrd
import sys

reward_count = {}
reward_itemName = {}


def get_xlrd(file_name):
    data = xlrd.open_workbook(file_name)
    table = data.sheets()[0]
    n_rows = table.nrows 
    for items in table.col_values(4):
        if items in reward_count:
            reward_count[items] +=1
        else:
            reward_count[items] = 1
    #print reward_count
    for reward_item in reward_count:
        print reward_item , reward_count[reward_item]

def changeCodes(str):
    print type(str)
    print sys.getdefaultencoding()
    str = str.decode('utf-8')
    str = str.encode('gb2312')
    return str

def show_excle(file_name):
    print "open xlsx"
    data = xlrd.open_workbook(file_name)
    print data
    table = data.sheets()[0]
    
    count = 0
    row_data = table.row_values(3)
    #print xlrd.xldate.xldate_as_datetime(row_data[0],0)
    for item in row_data:
        print item


if __name__ == "__main__":
    file_name = "1.xlsx"
    #get_xlrd(file_name)
    show_excle(file_name)
    
