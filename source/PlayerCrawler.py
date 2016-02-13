#jianmin for IS5126 Project 1
#output active NBA player stats infor into csv files
#each player outputs a file
#logic: 
# 1. from all players Index page to get each player URL
# 2. from each URL page get the season stas 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv
import os
import time
import CompareMethods
import PlayerInfo
import PlayerSalary
import PlayerStats
#urls 
mainurl = 'http://www.basketball-reference.com'
currentpath = os.path.dirname(os.path.abspath(__file__))

#enable paths for active players
#playerprofilepath = currentpath + '/data/active_players_profile.csv'
#playersalarypath = currentpath + '/data/active_players_salary.csv'
activeplayerprofilepath = currentpath + '/data/active_player_urls.csv'
#playerstatspath = currentpath + '/data/active_player_stats.csv'

playerprofilepath = currentpath + '/data/player_since_2000_profile.csv'
playersalarypath = currentpath + '/data/player_since_2000_salary.csv'
playerurlspath = currentpath + '/data/player_since_2000_urls.csv'
playerstatspath = currentpath + '/data/player_since_2000_stats.csv'

year = 2000

def writePlayerInfo():
	#create csv file with prefixed header tags
	out = open(playerprofilepath,'a')
	tags = 'Player,From,To,Pos,Ht,Wt,DOB,College\n'
	out.write(tags)
	out.close()
	print("starting to get all players information...")
	urls = CompareMethods.getPlayersIndexUrls(True)
	for url in urls:
   		href = mainurl + url
		#active players
   		#PlayerInfo.getPlayerInfo(True, href, activeplayerprofilepath)
		#players since 2000
		PlayerInfo.getPlayerInfoSinceYear(href,playerprofilepath,year)
   	print ('Player Info All Done!')
	return;

def writePlayerSalary():
	salaryout = open(playersalarypath,'a')
	salarytags = 'Name,Season,Team,Lg,Salary\n';
	salaryout.write(salarytags)
	salaryout.close()
	print("starting to get all players salary...")
	infile=csv.reader(open(playerurlspath,'rb'), delimiter=',')
	urls = []
	if infile:
	   infile.next()
	   for row in infile:
		urls.extend(row)
	   for url in urls:
   		href = mainurl + url
		PlayerSalary.getPlayerSalary(href, playersalarypath)
	else:
	   urls = CompareMethods.getPlayerUrls(True)
	   for url in urls:
   		href = mainurl + url
		PlayerSalary.getPlayerSalary(href, playersalarypath)
	print ('Salary All Done!')
	return;

def writePlayerStats():
	out = open(playerstatspath,'a')
	tags = 'Name,Season,Age,Tm,Lg,Pos,G,GS,MP,FG,FGA,FG%,3P,3PA,3P%,2P,2PA,2P%,eFG%,FT,FTA,FT%,ORB,DRB,TRB,AST,STL,BLK,TOV,PF,PTS\n';
	out.write(tags)
	out.close()
	print("starting to get all players stats...")
	infile=csv.reader(open(playerurlspath,'rb'), delimiter=',')
	urls = []
	if infile:
	   infile.next()
	   for row in infile:
		urls.extend(row)
	   for url in urls:
   		href = mainurl + url
		PlayerStats.getPlayerStats(href, playerstatspath)
	else:
	   urls = CompareMethods.getPlayerUrls(True)
	   for url in urls:
   		href = mainurl + url
		PlayerStats.getPlayerStats(href, playerstatspath)
	print ('Stats All Done!')
	return;

writePlayerInfo()
writePlayerSalary()
writePlayerStats()
