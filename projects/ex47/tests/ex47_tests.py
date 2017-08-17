from nose.tools import *
from ex47 import Room

def test_room():
	gold = Room("GoldRoom",
		"""This room has gold in it)

def teardown():
	print "Tear Down!!"

def test_basic():
	print "I ran!" 