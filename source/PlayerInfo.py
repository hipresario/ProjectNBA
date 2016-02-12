#jianmin for IS5126 Project 1
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import time
import re
import csv
import os

def getPlayerInfoByBS(playerurl,outpath): 
	
 	#replace html special/empty characters, add ',' in the end
	def processHtmlString(value):
	       temp = value.replace(u'\xa0', u'').replace(u'\u25aa',u'').replace(',',u'').replace(u'\n','').replace(':','').rstrip('(').strip()
	       return temp;
	#must be in sequence
	def convertDictToString(dic):
		list = []
		list.append(dic['Name'])
		list.append(dic['Position'])		
		list.append(dic['Shoots'])
		list.append(dic['Height'])		
		list.append(dic['Weight'])
		list.append(dic['Born'])
		list.append(dic['High School'])		
		list.append(dic['College'])
		list.append(dic['Draft'])		
		list.append(dic['NBA Debut'])
		list.append(dic['Experience'])
		list.append(dic['D-League'])
		return ','.join(list);

	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")

	playerinfo = {'Name':'','Position':'','Shoots':'','Height':'','Weight':'','Born':'','High School':'','College':'','Draft':'','NBA Debut':'','Experience':'','D-League':''}

	index = soup.find("div",{"id":"info_box"})
	header = index.findAll("span",{"class":"bold_text"})

	#write player data 
	name = index.find('h1')
	playerinfo['Name'] = processHtmlString(name.get_text())
	for i in header:
		if (header.index(i) == 0) : 
			continue
		key = processHtmlString(i.get_text())
		next = processHtmlString(i.next_sibling)
		#Position,Shoots,Height,Weight
		if (header.index(i) < 5 ) : 
			playerinfo[key] = next
			continue
		if (key == 'Born'):
			dob = i.find_next_sibling('span')	
			birthplace = dob.next_sibling +  dob.next_sibling.next_sibling.string
			playerinfo[key] = processHtmlString(dob.get_text() + birthplace)	
			continue
		if (key == 'High School'):
			highschool = i.next_sibling			
			playerinfo[key] = processHtmlString(highschool)
			continue
		if (key == 'College'):
			college = i.find_next_sibling("a").get_text()
			playerinfo[key] = processHtmlString(college)
			continue
		if (key == 'NBA Debut'):
			debut = i.find_next_sibling("a").get_text()
			playerinfo[key] = processHtmlString(debut)
			continue
		if (key == 'Experience'):
			playerinfo[key] = next
			continue
		if (key == 'D-League'):
		        playerinfo[key] = next
			continue
		if (key == 'Draft'):
			draft1 = i.find_next_sibling("a")
			draft2 = draft1.next_sibling
			draft3 = draft1.find_next_sibling("a")
			draft = draft1.get_text() + draft2 + draft3.get_text()
			playerinfo[key] = processHtmlString(draft)
	 		continue
	#write to file
	out = open(outpath,'a+')
	out.write(convertDictToString(playerinfo))
	out.write('\n')
	out.close()
	print (name.get_text() + ' is done! Going to sleep 1 second...')
	time.sleep(1)
	return;
