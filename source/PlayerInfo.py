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

def getPlayerInfoSinceYear(playerurl,outpath,year):
	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser") 
	table = soup.find("table",{"id":"players"})
	rows = table.find("tbody").findAll("tr")
	name = '';
	if rows:
	   allrecords = []
	   for row in rows:
		tds = row.findAll('td')
                toYear = int(tds[2].get_text())
		flag = (toYear - year) >= 0
		if flag:
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
	tbody = re.findall('(?is)<tbody>.*?</tbody>', webpage)
	trs = re.findall('(?is)<tr.*?</tr>', ''.join(tbody))
	allrecords = []
	name = ''
	for tr in trs:
		strong = re.findall('<strong>(.*?)</strong>', tr)
		
		if strong:
		   records = []
		   tds = re.findall('(?is)<td.*?</td>',tr)
		   if len(tds) == 8:
		      count = 0
		      for td in tds: 
		        if (count == 0):
					name = re.findall('">(.*?)</a>',td)
					records.append(processHtmlString(''.join(name)))
			if (count == 1):
					t1 = re.findall('>(.*?)</td>',td)
					records.append(processHtmlString(''.join(t1)))
			if (count == 2):
					t2 = re.findall('>(.*?)</td>',td)
					records.append(processHtmlString(''.join(t2)))
			if (count == 3):
					t3 = re.findall('>(.*?)</td>',td)
					records.append(processHtmlString(''.join(t3)))
			if (count == 4):	
					t4 = re.findall('>(.*?)</td>',td)
					records.append(processHtmlString(''.join(t4)))
			if (count == 5):
					t5 = re.findall('>(.*?)</td>',td)
					records.append(processHtmlString(''.join(t5)))
			if (count == 6):
					t6 = re.findall('day=.*?</a>',td)
					if t6:
					    dob = re.findall('>(.*?)</a>',''.join(t6))
					    records.append(processHtmlString(''.join(dob)))
					else:
					    records.append('')
			if (count == 7):
					t7 = re.findall('">(.*?)</a>',td)
					if t7:
					    records.append(processHtmlString(''.join(t7)))
					else:
					    records.append('')
			count+=1
		    
		      allrecords.append(','.join(records) + '\n')
	#print(allrecords)
	out = open(outpath,'a+')
	out.write(''.join(allrecords)) 
	out.close()
	print (name + ' is done! Going to sleep 1 second...')
	time.sleep(1)
	return;	

getPlayerInfoByRegex('http://www.basketball-reference.com/players/a','')
