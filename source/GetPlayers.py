#jianmin for IS5126 Project 1
#output NBA players stats who played all seasons from 2005 to 2015 into csv files

from urllib2 import urlopen 
import csv
import os
import time

#urls 
currentpath = os.path.dirname(os.path.abspath(__file__))

playerprofilepath = currentpath + '/data/active_players_profile.csv'
out = currentpath + '/data/active_players_from_2006.csv'

def writePlayers():
	playerout = open(out,'a')
        playerouttags = 'URL,Player,From,To,Pos,Ht,Wt,DOB,College\n';
	playerout.write(playerouttags)
	playerout.close()
	infile=csv.reader(open(playerprofilepath,'rb'), delimiter=',')
	records = []
	if infile:
	   infile.next()
	   for row in infile:
                fromYear = int(row[2])
                toYear = int(row[3])
                if (fromYear <= 2006 and toYear >= 2016):
                   #print(row)
		   height = (float(str(row[5]).replace('-','.'))) * 1.0
                   row[5] =  str(height)
	           records.append(','.join(row) + '\n')

	out2 = open(out,'a+')
	out2.write(''.join(records)) 
	out2.close()

	print ('Players All Done!')
	return;


#writePlayers()

