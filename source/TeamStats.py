#jianmin for IS5126 Project 1
#output active NBA teams season stas infor into csv files
#each team outputs a file
#logic: 
# 1. from Team Index page to get each team URL
# 2. from each URL page get the season stats 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv
import os
import time

def processHtmlString(value):
	return value.strip().replace(u'\xa0', u' ').replace('*','').replace(',',' ');
 
def getTeamSeasonStats(teamurl, name, outpath ):
	webpage = urlopen(teamurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")
        trs = soup.find("table",{"id":name}).find("tbody").findAll("tr")
        out = open(outpath,'a+')
	
 	if trs:
           records = []
	   for i in trs:
		data = [name]
		for j in i.find_all("td"):
	 	   data.append(processHtmlString(j.get_text()))
		records.append(','.join(data) + '\n')
	   out.write(''.join(records)) 	
	out.close()	
 	return;
