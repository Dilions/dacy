# -*- coding: UTF-8 -*-
import time 
import random

#饥饿进程 1
def hunger(x):
	if x.hunger <= 1:
		x.healthy-=1
		return 0
		pass

	if x.hunger <=20:
		if x.cash>1:
			rate = random.randint(0,100)
			if rate>x.hunger:
				x.cash -=1
				x.hunger +=48
				pass
			pass
#			print rate,x.hunger,x.cash,x.healthy
#			time.sleep(1)
		pass
#		else:

	if x.roll != "null":
		x.hunger -= 0.15
		pass
	else:
		x.hunger -= 0.1
	pass

#存活检测
def healthyCheck(x):
	if x.healthy<=0:
		x.live=0
		pass
	pass

#钱少了找工作
def cashCheck(joblist,x):

	if x.cash<=100 and x.roll=="null":
		joblist.searchjob(x)
#		x.roll="worker"
#		print "get a job"
		pass
	elif x.roll!="null":
#payment system
		x.workday+=1
		if x.workday==10080: #7天发薪水
			x.workday=0
			x.cash+=35			#收入35
			print "income 200 from work and now have ",x.cash

#			time.sleep(1)
   
			pass
	pass

#工作发布平台
class joblist:
	"发布平台"
	def __init__(self, arg):
		self.arg = arg
		self.list = {}

	def sort(self):

		pass

	def add(self,company,job):
#		print company,job
		self.list[company] = job
#		print self.list[company]
		pass

	def cancel(self,company,job):
		del self.list[company]
		pass

	def show(self):
		print self.list
		pass

	def searchjob(self,man):
		for key,value in self.list.items():
			if value==man.bestskill:

				man.roll=value
				print "get a",value ,"job in",key

		pass

	def searchcompany(self,company):
		pass



job = joblist(123)
#job.show()
job.add("ca","eee")
job.show()


class company:
	"公司测试样例"
	def __init__(self, name):
#		super(company, self).__init__()
		self.name = name
		self.father = "null"
		self.child = "null"
		self.juridical_person = "null"
		# self.worker =workers('a')
		self.worklist=worklist(123)
	def search_jobkind(self,jobkind):
		i=0
		for value in self.worklist.kind:
			if value==jobkind:
			return i
			i+=1
		return -1
		pass

	def add_jobkind(self,jobkind,joblist,number=1,hard=5,dirt=5,salary=50):
		n=search_jobkind(jobkind)
		if n>=0:
			self.worklist.numneed[n]	+=	number
			self.worklist.hard[n]		=	hard
			self.worklist.dirt[n]		=	dirt
			self.worklist.salary[n]		=	salary
			send_worker_require(jobkind=jobkind,hard=hard,dirt=dirt,salary=salary)
			pass
		else:
			self.worklist.kind.append(jobkind)
			self.worklist.number.append(number)
			self.worklist.hard.append(hard)
			self.worklist.dirt.append(dirt)
			self.worklist.salary.append(salary)
		pass

	def del_jobkind(self,jobkind):
		pass

	def getResume(man):
		pass

	def show_worklist():
		pass

	def send_worker_require():
		pass

class worklist:
	"工种测试用例表单"
	def __init__(self, arg):
		self.arg 	= 	arg
		self.kind 	=	[]		#["banzhuan","ee","eee"]
		self.kinda	=	[]		#["a","b","c"]
		self.numneed=	[]		#[0,0,0]
		self.numget =  []
		self.hard 	=	[]		#[0,5,7]
		self.dirt 	=	[]		#[10,2,1]
		self.salary = 	[]
		
comp =company("EA")
print comp.worker.hard

def seekcomp(x):
	job.searchjob(x)
	pass