#jianmin for IS5126 Project 1
#output active NBA teams season stas infor into csv files
#logic: 
# 1. from Team Index page to get each team URL
# 2. from each URL page get the season stats 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv
import os
import time
import CompareMethods
import TeamInfo
import TeamStats
#urls 
mainurl = 'http://www.basketball-reference.com'
currentpath = os.path.dirname(os.path.abspath(__file__))

#paths
teamurlspath =  currentpath + '/data/team_urls.csv'
teamseasonpath =  currentpath + '/data/team_season_stats.csv'

def writeTeamBasicInfo():
	TeamInfo.writeTeamInfoByBS()
	return;

def writeTeamSeasonStats():
	print("starting to get all teams season stats...")
        #write headers
        out = open(teamseasonpath,'a')
	tags = 'Name,Season,Lg,Team,W,L,W/L%,Finish,SRS,Pace,Rel_Pace,ORtg,Rel_ORtg,DRtg,Rel_DRtg,Playoffs,Coaches,Top WS\n'
	out.write(tags)
	out.close()
 	infile=csv.reader(open(teamurlspath,'rb'), delimiter=',')
	if infile:
	   infile.next()
	   for row in infile:
		name = row[0]
    		href = mainurl + row[1]
		TeamStats.getTeamSeasonStats(href, name, teamseasonpath)
	print ('All Done!')
 	return;

writeTeamBasicInfo()
writeTeamSeasonStats()
