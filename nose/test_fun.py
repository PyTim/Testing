
from nose.tools import with_setup

def setup_fun1():
	print "fun1 will start"

def teardown_fun1():
	print "fun1 completed"

def setup_fun2():
	print "fun2 will start"

def teardown_fun2():
	print "fun2 completed"

@with_setup(setup_fun2,teardown_fun2)
def test_fun2():
	print "fun2 is running"

@with_setup(setup_fun1,teardown_fun1)
def test_fun1():
	print "fun1 is running"








