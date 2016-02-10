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
import Player
#urls 
mainurl = 'http://www.basketball-reference.com'
currentpath = os.path.dirname(os.path.abspath(__file__))
playersindexurl = mainurl + '/players/'

#paths
allplayerspath = currentpath + '/data/all_players.csv';
#create csv file with prefixed header tags
out = open(allplayerspath,'a')
tags = 'Name,Position,Shoots,Height,Weight,Born,High School,College,Draft,NBA Debut,Experience,D-League\n';
out.write(tags)
out.close()

 

#global function
def writePlayerStats(url):
	playerurl = mainurl + url
	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
	players = soup.find("table",{"id":"players"}).findAll("strong")
        for i in players:
             href = mainurl + i.find("a").get("href")
	     #call each player page
	     Player.getPlayerInfo(href, allplayerspath)
    
	return;

webpage = urlopen(playersindexurl).read()
soup = BeautifulSoup(webpage,  "html.parser")

#get each player index page url a-z
index = soup.find("div",{"id":"page_content"}).find("p")
for i in index.findAll('a'):
	href = i.get('href')
	#print(href)
	print("starting to get player information...")
	writePlayerStats(href)

print ('All Done!')
