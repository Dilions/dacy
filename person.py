# -*- coding: UTF-8 -*-

#就对于一个人 以及行为的定义

class person:
	'所有人的基类'
	Population = 0
	def __init__(self):
		self.live =1
		self.SN=person.Population

		self.name = name
		self.age = age 
		self.sex = "male"     
		person.Population += 1

		self.status=personal_status()
		# self.hunger =50
		# self.energy =50
		# self.happiness =50
		# self.sleepy =50
		# self.healthy =100

		self.skill = skills()
		self.money

		self.spirits =spirits()
		self.stuff = stuff()
		# self.workday=0


class personal_status:
	def __init__(self):
		self.hunger
		self.happiness
		self.energy
		self.healthy
		self.sleepy
		
class spirits:
	"""docstring for skill"""
	def __init__(self, arg):
		self.arg = 0
		self.positive
		self.aggressive
		self.brave
		self.active

		self.fallen
		self.coward
		self.degenerate #堕落
		self.shy
		

class skills:
	"""docstring for skill"""
	def __init__(self, arg):
		self.arg = arg

		self.math
		self.speech
		self.code
		self.manage
		self.sport
		self.language
		self.farm
		self.cook
		self.clothjob
		self.drive
		self.cleanjob

class stuff:
	"""docstring for stuff"""
	def __init__(self, arg):
		self.arg = arg

		self.food = food()
		self.cloth= cloth()
		self.house

		

class relationship:
	"""docstring for relationship"""
	def __init__(self, arg):
		self.arg = arg
		
		self.father
		self.mother
		self.children
		self.fere
		self.friends[]
