#jianmin
import sqlite3
import os

currentpath = os.path.dirname(os.path.abspath(__file__))
dbpath = currentpath + '/data/nba.db'

def getConnection():
	connection = sqlite3.connect(dbpath)
	if connection:
	    print("Connection is ready...")
	return connection;


#getConnection()
