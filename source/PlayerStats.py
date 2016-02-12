#jianmin for IS5126 Project 1
#output active NBA player stats infor into csv files
#each player outputs a file
#logic: 
# 1. from all players Index page to get each player URL
# 2. from each URL page get the season stas 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import time
import csv
import os

def getPlayerStats(playerurl,outpath): 
	
 	#replace html special/empty characters
	def processHtmlString(value):
	       temp = value.replace(u'\u2605',u'').replace(u'\xa0', u'').replace(u'\u25aa',u'').replace(',',u'').replace('\n','').strip()
	       return temp;
	#must be in sequence
	def convertDictToString(stats):
		return ''.join(stats);

	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")

	header = soup.find("div",{"id":"info_box"})
	index = soup.find("table",{"id":"totals"})
	
	#get player name
	name = processHtmlString(header.find('h1').get_text())

	stats = []
	if not index is None:
		trs = index.find('tbody').findAll('tr')
		#print(trs)
		if trs:
		  for i in trs:
			tds = i.findAll('td')
			#print(tds)
			if tds:			
			  playerinfo = [name]
			  hasdata = tds[0].find('a')
			  for j in tds:
			      if hasdata:
			         playerinfo.append(processHtmlString(j.get_text()))				
			  if (len(playerinfo) == 31): 
			  	stats.append(','.join(playerinfo) + '\n')
	 

	#print(convertDictToString(stats))
	#write to file
	out = open(outpath,'a+')
	out.write(convertDictToString(stats))
	out.close()
	print (name + ' is done! Going to sleep 1 second...')
	time.sleep(1)
	return;

#getPlayerStats('http://www.basketball-reference.com/players/j/jonesso01.html','')
