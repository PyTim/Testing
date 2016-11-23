#coding: utf-8

class test_person(object):
	def __init__(self):
		self.name = 'case'
		
	def setUp(self):
		print self.name + " will start"
	def tearDown(self):
		print self.name + " completed"

	def test_fun1(self):
		print "fun1 is running"
	def test_fun2(self):
		print "fun2 is running"

