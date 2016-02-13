#jianmin for IS5126 Project 1
#compare Regex and BeautifulSoup to get URLs
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv
import os
import time
import re
import timeit

mainurl = 'http://www.basketball-reference.com'
currentpath = os.path.dirname(os.path.abspath(__file__))

def getPlayersIndexUrls(isRegex):
	#BeautifulSoup to get a-z index 
	def getPlayerIndexHrefByBS(webpage):
		soup = BeautifulSoup(webpage,  "html.parser")
		#get each player index page url a-z
		index = soup.find("div",{"id":"page_content"}).find("p")
		hrefs = []
		for i in index.findAll('a'):
			href = i.get('href')
			hrefs.append(href)
		#print(hrefs)	
		return hrefs;
	
	#Regex to get a-z index
	def getPlayerIndexHrefByRegex(webpage):
		urls = re.findall('href="(/players/[a-z]/)"',webpage)
		hrefs = urls[0:25] if len(urls) > 0 else []
 		#print(hrefs)
		return hrefs;    

	playersindexurl = mainurl + '/players/'
	webpage = urlopen(playersindexurl).read()
	urls = getPlayerIndexHrefByRegex(webpage) if isRegex else getPlayerIndexHrefByBS(webpage)
	time.sleep(1)
	return urls;

def getPlayerUrls(isRegex):
	def getPlayerUrlsByBS (playerurl):
		webpage = urlopen(playerurl).read()
		soup = BeautifulSoup(webpage,  "html.parser")
		players = soup.find("table",{"id":"players"}).findAll("strong")
		playerurls = []
		if players:
		   for i in players:
		      href = i.find("a").get("href")
		      if href:
			  playerurls.append(href)
		
		return playerurls;

	def getPlayerUrlsByRegex (playerurl):
		webpage = urlopen(playerurl).read()
		strongtags = re.findall('<strong><a(.*?)</strong>',webpage)
		playerurls = []
		if strongtags:
		   for i in strongtags:
			href = re.findall('/players/[a-z]/.*\.html', i)
			if href:
		            playerurls.append(''.join(href).strip())	

		return playerurls;
	
	playerindex = getPlayersIndexUrls(isRegex)
	if playerindex:
	  allplayerurls = []
	  for i in playerindex:
		url = mainurl + i
		playerurls = getPlayerUrlsByRegex(url) if isRegex else getPlayerUrlsByBS(url)
		allplayerurls.extend(playerurls)
		time.sleep(1)
 	#print(allplayerurls)
	return allplayerurls;

def getPlayerUrlsSinceYear(year):

	def getPlayerUrlsAfterYear(year,playerurl):
		webpage = urlopen(playerurl).read()
		soup = BeautifulSoup(webpage,  "html.parser")
		players = soup.find("table",{"id":"players"}).find("tbody").findAll('tr')
		playerurls = []
		if players:
		   for i in players:
		        tds = i.findAll('td')
                        toYear = int(tds[2].get_text())
			flag = (toYear - year) >= 0			
			if flag: 
			   href = i.find("a").get("href")
		           if href:
			      playerurls.append(href)
		
		return playerurls;

	playerindex = getPlayersIndexUrls(True)
	if playerindex:
	  allplayerurls = []
	  for i in playerindex:
		url = mainurl + i
		playerurls = getPlayerUrlsAfterYear(year,url)
		allplayerurls.extend(playerurls)
		print('Going to sleep 1 sec...')
		time.sleep(1)
 	#print(allplayerurls)
	return allplayerurls;		

def getTeamUrls(isRegex):
	def getTeamUrlsByBS(webpage):
		soup = BeautifulSoup(webpage,  "html.parser")
		table = soup.find("table",{"id":"active"}).findAll("tr",{"class":"full_table"})
		hrefs = []
 		for i in table:
		    for k in i.find_all('a'):
  	            	team = k.get('href')
		    	hrefs.append(team)
		return hrefs;

	def getTeamUrlsByRegex(webpage):
		urls = re.findall('<td align="left" ><a href="(.*?)">', webpage)
		#only active teams
 		hrefs = urls[0:30]
		return hrefs;    		

	teamurl = mainurl +'/teams/'
	webpage = urlopen(teamurl).read()
	urls = getTeamUrlsByRegex(webpage) if isRegex else getTeamUrlsByBS(webpage)
	time.sleep(1)
	return urls;

def writePlayerUrls():
	allplayerspath = currentpath + '/data/active_player_urls.csv';
	out = open(allplayerspath,'a')
	urls = getPlayerUrls(True)
	out.write('Player URL\n')
	for i in urls:
           out.write(i + '\n')
	out.close()
	return

def writeTeamUrls():
	allteamspath = currentpath + '/data/team_urls.csv';
	out = open(allteamspath,'a')
	urls = getTeamUrls(True)
	out.write('Team,Name,URL\n')
	for i in urls:
	   name = i.split('/')[2]
           out.write(name + ',' + i + '\n')
	out.close()
	return

def writePlayerUrlsSinceYear(year):
      	allplayerspath = currentpath + '/data/player_since_2000_urls.csv';
	out = open(allplayerspath,'a')
	out.write('Player URL\n')
	urls = getPlayerUrlsSinceYear(year)
	for i in urls:
           out.write(i + '\n')
	out.close()
	return
	
#writePlayerUrls()
#writeTeamUrls()
#writePlayerUrlsSinceYear(2000)


#True for regex method
def testAllPlayers():
	getPlayerUrls(True)

def testIndexPlayers():
	getPlayersIndexUrls(True)

def testTeamUrls():
	getTeamUrls(True)

#print time for testing methods run time
#print(timeit.Timer(testTeamUrls).timeit(number=1))

