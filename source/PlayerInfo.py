#jianmin for IS5126 Project 1
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import time
import re
import csv
import os

#replace html special/empty characters
def processHtmlString(value):
        return value.replace(u'\xa0', u'').replace(u'\u25aa',u'').replace(',',u' ').replace(u'\n','').strip();

def getPlayerInfo(isRegex,playerurl,outpath):
	if isRegex:
	    getPlayerInfoByRegex(playerurl,outpath)
	else:
	    getPlayerInfoByBS(playerurl,outpath)

	return;

def getPlayerInfoByBS(playerurl,outpath): 	 
	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser") 
	table = soup.find("table",{"id":"players"})
	rows = table.find("tbody").findAll("tr")
	name = '';
	if rows:
	   allrecords = []
	   for row in rows:
		active = row.find('strong')
		if active:	    
		    tds = row.findAll('td')
		    name = processHtmlString(tds[0].get_text())
		    records = []
		    for td in tds:
			records.append(processHtmlString(td.get_text()))
		    allrecords.append(','.join(records) + '\n')
	   #write
	   out = open(outpath,'a+')
	   out.write(''.join(allrecords)) 
	   out.close()
	   print (name + ' is done! Going to sleep 1 second...')
	   time.sleep(1)
	return;


def getPlayerInfoByRegex(playerurl,outpath):
	webpage = urlopen(playerurl).read()
	tbody = re.findall('<strong>(.*?)</strong>', webpage)
	print(tbody)
	last = len(tbody)
	if last:
	   print(tbody[last-1])
	return;

