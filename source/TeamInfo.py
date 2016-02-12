#jianmin for IS5126 Project 1
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import time
import re
import csv
import os

#urls 
mainurl = 'http://www.basketball-reference.com'
currentpath = os.path.dirname(os.path.abspath(__file__))
teamurl = mainurl + '/teams/'

#paths
allteampath = currentpath + '/data/teams_profile.csv'

def processHtmlString(value):
	return value.strip().replace(u'\xa0', u' ').replace('*','').replace(',',' ');

def writeTeamInfoByBS():
	print('Writing basic team info...')
	webpage = urlopen(teamurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
	header = soup.find("table",{"id":"active"}).find("thead")
	table = soup.find("table",{"id":"active"}).findAll("tr",{"class":"full_table"})
        out = open(allteampath,'w')
        #all teams header infor
	out.write('Team,')
	for j in header.find_all("th"):
	    out.write(processHtmlString(j.get_text())+",")
	out.write("\n")

	#write out each team basic info
	for i in table:
	    tds = i.find_all("td")
	    href = tds[0].find('a').get('href')
	    name = href.split('/')[2]
	    out.write(name + ',')
	    for j in tds:
		out.write(processHtmlString(j.get_text())+",")
	    out.write("\n")
	
	out.close()
	print('Going to sleep 1 sec...')
	time.sleep(1)
	print('All Done!')
	return;

#writeTeamInfoByBS()
