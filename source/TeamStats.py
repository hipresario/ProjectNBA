#jianmin for IS5126 Project 1
#output active NBA teams season stas infor into csv files
#each team outputs a file
#logic: 
# 1. from Team Index page to get each team URL
# 2. from each URL page get the season stas 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv
import os
import time

#urls 
mainurl = 'http://www.basketball-reference.com'
currentpath = os.path.dirname(os.path.abspath(__file__))
teamindexurl = mainurl + '/teams/'

#paths
allteampath = currentpath + '/data/all_teams.csv';

#global vars
teams = []

webpage = urlopen(teamindexurl).read()
soup = BeautifulSoup(webpage,  "html.parser")

header = soup.find("table",{"id":"active"}).find("thead")
table = soup.find("table",{"id":"active"}).findAll("tr",{"class":"full_table"})

#begin all teams file
allteamout = open(allteampath,'w')

#all teams header infor
#write out table header
for j in header.find_all("th"):
	    allteamout.write(j.get_text()+",")
allteamout.write("\n")

#write out each team basic info
for i in table:
	for j in i.find_all("td"):
		 allteamout.write(j.get_text().replace('*','')+",")
	allteamout.write("\n")
	
allteamout.close()

#delay
time.sleep(1)

def writeTeamSeasonStats(url):
        teamurl = mainurl + url
        #print(teamurl) 	
	teamname = url.split('/')[2]
        #print(teamname)
        outpath = currentpath + '/data/team_' + teamname + '.csv'
        #print(outpath)
	webpage = urlopen(teamurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
	header = soup.find("table",{"id":teamname}).find("thead")
        table = soup.find("table",{"id":teamname}).find("tbody").findAll("tr")
        out = open(outpath,'w')
        for j in header.find_all("th"):
		out.write(j.get_text().replace(u'\xa0', u' ')+",")
	out.write("\n")
	
	for i in table:
		for j in i.find_all("td"):
 	            out.write(j.get_text().replace(u'\xa0', u' ').replace('*','')+",")
		out.write("\n")
	
	out.close()	
	return;

#begin individual team season stats
for i in table:
 	for k in i.find_all('a'):
	         team = k.get('href')
	         print('writing team ' + team + '...' )
                 writeTeamSeasonStats(team)
                 print('going to sleep 1 sec...')
                 time.sleep(1)
	       
print ('Done!')
