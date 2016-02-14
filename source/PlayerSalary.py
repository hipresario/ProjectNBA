#jianmin for IS5126 Project 1
#get player salary
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import time
import csv
import os

def getPlayerSalary(playerurl,outpath): 
	
 	#replace html special/empty characters
	def processHtmlString(value):
	       temp = value.replace(u'\xa0', u'').replace(u'\u25aa',u'').replace(',',u'').strip()
	       return temp.lstrip('$');
	#must be in sequence
	def convertDictToString(salaries):
	        rows = []
		for dic in salaries:
			list = []
			list.append(dic['Name'])
			list.append(dic['Season'])		
			list.append(dic['Team'])
			list.append(dic['Lg'])		
			list.append(dic['Salary'])
			rows.append(','.join(list) + '\n')
		return ''.join(rows);

	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")

	header = soup.find("div",{"id":"info_box"})
	index = soup.find("table",{"id":"salaries"})
	
	#get player name
	name = processHtmlString(header.find('h1').get_text())

	salaries = []
	if not index is None:
		#salaries	
		for i in index.find('tbody').findAll('tr'):
			tds = i.findAll('td')
			playerinfo = {'Name':'','Season':'','Team':'','Lg':'','Salary':''}
			playerinfo['Name'] = name
			for j in tds :
				if (tds.index(j) == 0):
					playerinfo['Season'] = processHtmlString(j.get_text())
				elif (tds.index(j) == 1):
					playerinfo['Team'] = processHtmlString(j.get_text())
				elif (tds.index(j) == 2):
					playerinfo['Lg'] = processHtmlString(j.get_text())
				else:
					playerinfo['Salary'] = processHtmlString(j.get_text())				
				 
			salaries.append(playerinfo)
	#if has contract, add new salaries
	contract = soup.find("table",{"id":"contract"})
	if not contract is None:
	   ths = contract.findAll('th')
	   seasons = []
	   for j in ths:
		if (ths.index(j) != 0):
			seasons.append(processHtmlString(j.get_text()))
	   team = ''
	   c_salaries = []
	   tds = contract.findAll('td')
	   for k in tds:
	        #print(k)
		if (tds.index(k) == 0):
			team = (processHtmlString(k.get_text()))
			 
		else:
			c_salaries.append(processHtmlString(k.get_text()))
	   
	   for s_sea,c_sal in zip(seasons,c_salaries):
		playerinfo = {'Name':'','Season':'','Team':'','Lg':'','Salary':''}
		playerinfo['Name'] = name
		playerinfo['Season'] = s_sea
		playerinfo['Team'] = team
		playerinfo['Lg'] = 'NBA'
		playerinfo['Salary'] = c_sal
	   	salaries.append(playerinfo)

	#print(salaries)
	#write to file
	out = open(outpath,'a+')
	out.write(convertDictToString(salaries))
	out.close()
	print (name + ' is done! Going to sleep 1 second...')
	time.sleep(1)
	return;
