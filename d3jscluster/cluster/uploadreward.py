#!usr/bin/env python
#-*- coding:utf8 -*-
from cluster.models import Rward
import xlrd
import os
import re
import datetime
import sys
# Create your models here.
excle_path = "./static/"
province_addr = [u"北京",u"上海" ,u"天津", u"重庆",u"广东",u"黑龙江",u"辽宁",u"吉林",u"河北",u"山西",u"宁夏",
                 u"山东",u"内蒙古",u"新疆",u"甘肃",u"陕西",u"河南",u"河北",u"江苏",u"浙江",u"福建",u"青海",
                 u"湖北",u"湖南",u"江西",u"安徽",u"广西",u"云南",u"四川",u"贵州",u"云南",u"西藏",u"海南",u"台湾"]


def upload_table(file):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    xlrd_object = xlrd.open_workbook('1.xlsx')
    #table_object = xlrd_object.sheets()[0]
    table_object = xlrd_object.sheets()[0]
    row_nums = table_object.nrows
    for rownum in range(1, row_nums):
        row_data = table_object.row_values(rownum)
        reward_object = new_object(row_data)
        reward_object.save()



def new_object(row_data):
    reward_item = Rward()
    reward_item.used_time = xlrd.xldate.xldate_as_datetime(row_data[0],0)
    reward_item.host_name = row_data[1]
    reward_item.user_num = row_data[2]
    reward_item.item_name = row_data[4]
    reward_item.item_gbl_key  = row_data[5]
    reward_item.item_itype = row_data[6]
    reward_item.user_real_name = row_data[7]
    reward_item.user_telephone = row_data[8]
    addr_list = addr_parse(row_data[9])
    reward_item.user_address_provience = addr_list["province"]
    reward_item.user_address_city = addr_list["city"]
    reward_item.user_address_detail = addr_list["detail"]
    reward_item.item_cmake = row_data[10]
    return reward_item



def addr_parse(addr_str):
    addr_arr = addr_str.split(u"省")
    if len(addr_arr) <= 1:
        for item in province_addr:
            if re.match(item, addr_str):
                addr_arr = [item, addr_str[len(item):]]
    city_str = addr_arr[-1]
    print city_str
    del addr_arr[-1]
    city_arr = city_str.split(u"市")
    print city_arr
    if len(city_arr) <=1:
        city_arr = city_str.split(u"地区")
    if len(city_arr) <=1:
        city_arr = [city_str[0:2], city_str[2:]]
    addr_arr = addr_arr + city_arr
    return {"province":addr_arr[0], "city":addr_arr[1], "detail":addr_arr[2]}

if __name__ == '__main__':
	print addr_parse(u"广西玉林市博白县博白县博白镇、欧洲城")
