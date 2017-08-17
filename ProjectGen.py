"""Project generator, 
a project project actually setup other projects for you instead of going to edit files manually
"""

#Get project name

#Check if the folder exists, 
#if folder exists stop and tell user the folder exists
#else create the folder and files

from sys import argv
import os

script, projectName = argv
#directory of this file
currentdirectory = os.path.dirname(os.path.realpath(__file__))
#current working directory
cwd = os.getcwd()

projectDirectory = cwd + "\\" + projectName

if os.path.exists(projectDirectory):
	exit("The Project name already exists")
else:
	os.makedirs(projectDirectory)
	os.makedirs(projectDirectory + "\\bin")
	os.makedirs(projectDirectory + "\\tests")
	open(projectDirectory + "\\tests\\__init__.py","w+")
	testsFile = open(projectDirectory + "\\tests\\"+projectName+"_tests.py","w+")
	os.makedirs(projectDirectory + "\\docs")
	os.makedirs(projectDirectory + "\\"+projectName)
	open(projectDirectory+"\\"+projectName+"\\__init__.py","w+")
	setupFile = open(projectDirectory+"\\setup.py","w+")

setupFileText = """
try:
	from setuptools import setup 
except ImportError:
	from distutils.core import setup

config = [
'description': 'My Project',
'author': 'My Name',
'url': 'URL to get it at.',
'download_url': 'Where to download it.',
'author_email': 'My email',
'version': '0.1',
'install_requires': ['nose'],
'packages': ['""" + projectName + """'],
'scripts': [],
'name': '"""+projectName+"""'
]

setup(**config)
"""

setupFile.write(setupFileText)
setupFile.close()

testfileText = """from nose.tools import *
import """+projectName+"""

def setup():
	print "SETUP!!!"

def teardown():
	print "Tear Down!!"

def test_basic():
	print "I ran!" """

testsFile.write(testfileText)

exit("should have all the files and directories setup")