__author__ = 'pragungoyal'

import re,sys
from data_objects import *
from config import dburl
from sqlalchemy import create_engine

usage_string = """
1: python dbsetup.py create
	to create the database
2: python dbsetup.py destroy
	to empty the database
	"""

if len(sys.argv) != 2:
	print usage_string
	sys.exit(-1)

if sys.argv[1] == 'destroy':
	print 'So you want me to create a fresh database, alright alright!'


if sys.argv[1] == 'create':
	print 'So you want me to create a database from scracth, alright alright!'
	engine = create_engine(dburl)
	Base.metadata.bind = engine
	Base.metadata.create_all(engine)



