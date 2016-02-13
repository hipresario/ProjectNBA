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

def processHtmlString(value):
	       temp = value.replace(u'\xa0', u'').replace(u'\u25aa',u'').replace(',',u'').strip()
	       return temp.lstrip('$');

def getMVPList():
	mvpurl = mainurl + '/awards/mvp.html'
	outpath = currentpath + '/data/mvp.csv'
	webpage = urlopen(mvpurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
	table = soup.find('table',{'id':'NBA-mvp'})
	out = open(outpath,'a')
	out.write('Season,Lg,Player,Vote,Age,Tm,G,MP,PTS,TRB,AST,STL,BLK,FG%,3P%,FT%,WS,WS/48\n')
	if table:
	    rows = table.find('tbody').findAll('tr')
	    if rows:
		for row in rows:
		    tds = row.findAll('td')
		    result = []
		    for td in tds:
		       result.append(td.get_text())
		    out.write(','.join(result) + '\n')
	out.close()	
	time.sleep(1)
	return

def getROYList():
	mvpurl = mainurl + '/awards/roy.html'
	outpath = currentpath + '/data/roy.csv'
	webpage = urlopen(mvpurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
	table = soup.find('table',{'id':'NBA-roy'})
	out = open(outpath,'a')
	out.write('Season,Lg,Player,Vote,Age,Tm,G,MP,PTS,TRB,AST,STL,BLK,FG%,3P%,FT%,WS,WS/48\n')
	if table:
	    rows = table.find('tbody').findAll('tr')
	    if rows:
		for row in rows:
		    tds = row.findAll('td')
		    result = []
		    for td in tds:
		       result.append(processHtmlString(td.get_text()))
		    out.write(','.join(result) + '\n')
	out.close()	
	time.sleep(1)
	return

def getSalaryCap():
	capurl = mainurl + '/contracts/salary-cap-history.html'
	outpath = currentpath + '/data/salary_cap.csv'
	webpage = urlopen(capurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
	table = soup.find('table',{'id':'teams'})
	out = open(outpath,'a')
	out.write('Year,Salary Cap,Salary Cap 2015\n')
	if table:
	    rows = table.find('tbody').findAll('tr')
	    if rows:
		for row in rows:
		    tds = row.findAll('td')
		    result = []
		    for td in tds:
		       result.append(processHtmlString(td.get_text()))
		    out.write(','.join(result) + '\n')
	out.close()	
	time.sleep(1)

#getMVPList()
#getROYList()
getSalaryCap()
