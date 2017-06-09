#!/usr/bin/python2.7
# -*- coding: utf-8 -*-  

from __future__ import unicode_literals

from django.db import models

# Create your models here.
#手机归属地库
class Tel2Addr(models.Model):
	telnum = models.CharField(max_length=7, primary_key = True)
	addrprov = models.CharField(max_length=20)
	addrcity = models.CharField(max_length=20)
	teloperator = models.CharField(max_length=20)
	areacode = models.CharField(max_length=5)
	postcode = models.CharField(max_length=6)

	def __unicode__(self):
		return self.telnum
	

	#-----------------------------
	#checkflag为记录check标志,其意义为：
	#1.有效
	#2.地址无效
	#3.手机号无效
	#4.手机号与地址不统一
	#........待补充
	#-----------------------------
#活动奖励发放结果
class RewardRecord(models.Model):
	usernum = models.CharField(max_length=10)
	username = models.CharField(max_length=18)
	telnum = models.CharField(max_length=11)
	usedtime = models.DateField()
	hostname = models.CharField(max_length=16)
	itemnam = models.CharField(max_length = 50)
	gbkey = models.CharField(max_length=12)
	itemitype = models.CharField(max_length=6)
	addrprov = models.CharField(max_length = 20)
	addrcity = models.CharField(max_length=20)
	addrdetail = models.CharField(max_length=200)
	cmake = models.CharField(max_length = 50)
	checkflag = models.IntegerField()

	def __unicode__(self):
		return self.usernum

#奖励方法设定

class RewardActivity(models.Model):
	actname = models.CharField(max_length = 50)
	actcmake = models.CharField(max_length=50,primary_key=True)
	logfile = models.CharField(max_length=50)
	
