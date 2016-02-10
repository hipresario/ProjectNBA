#jianmin for IS5126 Project 1
#output active NBA player stats infor into csv files
#each player outputs a file
#logic: 
# 1. from all players Index page to get each player URL
# 2. from each URL page get the season stas 
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import time

def getPlayerSalary(playerurl,outpath): 
	
 	#replace html special/empty characters
	def processHtmlString(value):
	       temp = value.replace(u'\xa0', u'').replace(u'\u25aa',u'').replace(',',u'').replace(u'\n','').replace(':','').rstrip('(').strip()
	       return temp.lstrip('$');
	#must be in sequence
	def convertDictToString(dic):
		list = []
		list.append(dic['Name'])
		list.append(dic['Season'])		
		list.append(dic['Team'])
		list.append(dic['Lg'])		
		list.append(dic['Salary'])
		return ','.join(list);

	webpage = urlopen(playerurl).read()
	soup = BeautifulSoup(webpage,  "html.parser")

	
	
	header = soup.find("div",{"id":"info_box"})
	index = soup.find("table",{"id":"salaries"})
	
	#get player name
	name = processHtmlString(header.find('h1').get_text())

	salaries = []
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
	        print(k)
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

	print(salaries)
	#write to file
	#out = open(outpath,'a+')
	#out.write(convertDictToString(playerinfo))
	#out.write('\n')
	#out.close()
	print (name + ' is done! Going to sleep 1 second...')
	time.sleep(1)
	return;

getPlayerSalary('http://www.basketball-reference.com/players/m/maxieja01.html','')
