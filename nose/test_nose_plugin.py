
from nose.tools import eq_
from nose.tools import ok_
from nose.tools import assert_in
from nose.tools import timed
import time
from nose.plugins.skip import SkipTest

def setUp():
	print "module will start"

def tearDown():
	print "module already completed"

def test_fun1():
	print "fun1 is running"
	a='123'
	b='123'
	eq_(a,b,msg='error happened')

def test_fun2():
	print "fun2 is running"
	a='123'
	b='123'
	assert_in(a,b,msg='error happened')

@timed(2)
def test_fun3():
	print "fun3 is running"
	time.sleep(1)

def test_fun4():
	print "fun4 is running"
	a='123'
	b='123'
	assert a==b

@attr(mode=1)
def test_fun5():
	raise SkipTest
	print "fun5 is running"
	a='123'
	b='123'
	ok_(a==b,msg='error happ')

