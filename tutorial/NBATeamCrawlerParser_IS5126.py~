#jianmin
from urllib2 import urlopen 
from bs4 import BeautifulSoup
import csv

webpage = urlopen('http://www.basketball-reference.com/teams/').read()

soup = BeautifulSoup(webpage)

#retrieve teams with detailed profiles
#filter multiple attributes at once by passing in more than one keyword argument
#put "class" and "full_table" into a dictionary and passing the dictionary into find_all()
#table = soup.findAll("tr",{"class":"full_table"})
table = soup.find("table",{"id":"active"}).findAll("tr",{"class":"full_table"})
header = soup.find("table",{"id":"active"}).find("thead")
#print table

#print only team name and url
#for t in table:
#        for target in t.find_all('a'):
#                print target.get_text()
#                print target.get('href')

#return the first result by searching tag tr
#print soup.tr

#output to csv file
out = open('out.csv','w')
print (table)

for j in header.find_all("th"):
		 out.write(j.get_text()+",")
out.write("\n")

for i in table:
	for j in i.find_all("td"):
		 out.write(j.get_text()+",")
	out.write("\n")
	
out.close()	
print ('Done!')
