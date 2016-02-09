# -*- coding: cp1252 -*-
from bs4 import BeautifulSoup
import sys
import os
import codecs
import re
import csv

###set working directory
#os.chdir(os.getcwd()+'\\Data')


def ContentExtraction(num, input):

     soup=BeautifulSoup(input)
     index=num
 
     #standard straitstimes.com formet
     template='straitstimes_standard'

     try:title = soup.find("title").get_text().strip()
     except: title='NA'

     try:
          all_authors=soup.find_all("div", {"class":"author-field author-name"})
          author=''
          for name in all_authors:
              author=author+name.get_text().strip()+". "
     except: author='NA'

     try: time=soup.find("div",{"class":"story-postdate"}).get_text().strip()
     except: time='NA'

     try:           #parse all text lines in content into one line, separated by space
         content_soup=soup.find("div",{"class":"odd field-item"})
         content=''
         cons=content_soup.findAll("p")
         for c in cons:
            content=content+c.find(text=True).replace('\n','').replace('\r','').strip()+' '
     except: content='NA'

     if author=='NA' and time=='NA' and content=='NA':
         author ='UNKNOWN'
         time='UNKNOWN'
         content='UNKNOWN'
         template='UNKNOWN'
         
     done='successful'

     if content=='': content='NO_TEXT'
     
     try:
         outwriter.writerow((index,template,title.encode('utf-8'),author.encode('utf-8'),time.encode('utf-8'),
                             content.encode('utf-8'),done)) 

     except:
         done='unsuccessful'
         outwriter.writerow((index,done,done,done,done,done,done)) #keep track
         
     return 

    
def main(start_html, end_html):
     
    outwriter.writerow(('index','template','title','author','time',
                             'content','done'))
    
    for i in xrange(int(start_html), int(end_html)+1):
        try:
            input = codecs.open('html_'+str(i)+'.html')         ###Read article i
            index=i;
            ContentExtraction(index, input)            
        except:pass
    return


#read keyboard input
start=raw_input('Enter the start line: ')
end=raw_input('Enter the end line: ')
outArticles = codecs.open('outArticles.csv','w')   #output to csv file, encoded with utf-8, or some 'string' cannot be written to file
outwriter=csv.writer(outArticles,quoting=csv.QUOTE_NONNUMERIC, lineterminator='\n')
main(start,end)
outArticles.close()
