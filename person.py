#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time 
import random
import function

class person:
	'所有员工的基类'
	Population = 0
 
	def __init__(self, name = "null", cash = 200,age = 10):
		self.name = name
		self.cash = cash
		self.age = age 
		self.sex = "male"     
		person.Population += 1
		self.SN=person.Population
		self.live =1

		self.workday=0

		self.hunger =50
		self.energy =50
		self.happiness =50
		self.sleepy =50
		self.healthy =100

		self.skill = ["breath","drink"]
		self.bestskill="banzhuan"
		self.roll = "null"

		self.volition ="null"

	def display(self):
		print "Name : ", self.name,  "\tcash: ", self.cash,
		print "\tSN=",self.SN


x  = person("Zara", 100)
x.display()

def life(joblist,x):
	
	function.healthyCheck(x)
	function.hunger(x)
	function.cashCheck(joblist,x)
	pass

#背景时间记录类
#time_count()计时
#time_display()显示时间
class date(object):
	"time counts"
	def __init__(self, arg):
		self.arg = arg
		self.year=0
		self.month=1
		self.day=1
		self.hours=0
		self.minutes=0
		self.second=0

	def time_count(self):
 		self.minutes+=1	
		
		if self.minutes==60:
			self.minutes=0
			self.hours+=1
			pass
		
		if self.hours==24:
			self.hours=0
			self.day+=1			
			pass

		if self.day==31:
			self.day=0
			self.month+=1
			self.time_display()

		if self.month==12:
			self.month=0
			self.year+=1
			pass

	def time_display(self):
		print "year",self.year,
		print "month",self.month,
		print "day",self.day,
		print "hours",self.hours,
		print "minutes",self.minutes
		pass

runningtime=date(1)
joblist = function.joblist(123)
joblist.add("EA","banzhuan")
joblist.add("TI","eee")
joblist.show()

company_EA = company("EA")
company_EA.add_jobkind("banzhuan",joblist)

while 1:
#	time.sleep(0.001)
	runningtime.time_count()

	if x.live==1:
		life(joblist,x)
#		print x.hunger,x.cash,x.healthy
		pass
	else:
		print "dead",x.roll,x.workday,
		runningtime.time_display()
		break;
   
