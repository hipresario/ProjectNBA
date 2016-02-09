#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
import httplib, urllib2, socket
import csv
import time
from random import randint

###set working directory
#os.chdir(os.getcwd()+'\\Data')

def main(startline, endline):
    ###open input file, which contains article links
    input = open('ArticleList.csv')
    ###start crawler
    crawler(input, startline, endline)

def crawler(infile, startline, endline):
    ###open log file, which contains crawling logs
    log_file = open('crawler_log.csv', 'ab')
    log_writer = csv.writer(log_file, delimiter=',', quoting=csv.QUOTE_MINIMAL) 
    ###read the first line
    line = infile.readline().strip()
    ###store line number to determine where to start
    linenum = 1
    log_data = []
    while(line):
        ###go to intended lines, for multi-machine work
        if (linenum >= startline) & (linenum <= endline):
            connection_error = 0
            write2disk = 0
            print '*****************************Processing line '+str(linenum)+'*****************************'
            ###remove space in front and behind
            article_infor = line.strip()
            ###get each field
            pieces = article_infor.split(',')
            article_id = pieces[0]
            article_url = pieces[1]
            ###crawl non-premium pages only              
            print 'Article ' + str(article_id) +': ' + article_url 
                ###get html source
            html = get_html(article_url)
                ###error encountered in opening url
            if html=='':
                    connection_error = 1
                ###no error
            else:
                    connection_error = 0

                        ###store html file
                    outfile = open('html_'+str(article_id)+'.html', "w")
                    outfile.write(html)
                    outfile.close()
                    write2disk = 1

            ###record crawling log
            log_data.append([article_id, article_url, connection_error, write2disk])
            ###write to disk for every 20 articles
            if (linenum-startline+1)%20 == 0:   
                log_writer.writerows(log_data)
                log_file.flush()
                log_data = []
        ###read in next line
        line = infile.readline()
        linenum = linenum + 1 
    ###append to log file
    log_writer.writerows(log_data)
    log_file.close()


def get_html(url):

    ###make url request 
    request = urllib2.Request(url)
#    request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')
#    request.add_header('Referer', 'http://www.straitstimes.com/')
    try:
        page = urllib2.urlopen(request, timeout = 20)
    except urllib2.URLError, e:
        print 'Got an error when request the webpage with the code', e 
        html = ''
    except httplib.BadStatusLine:
        print 'Got bad status line!' 
        html = ''
    except socket.timeout:
        print 'URL request times out!' 
        html = ''
    else:
        ###get the source code of the page
        html = page.read()

    ###random delay to mimic normal user
    #time.sleep(randint(1,5))
    return html

###main()
input_str_start=raw_input('Please input start line: ')
input_str_end=raw_input('Please input end line: ')

main(int(input_str_start), int(input_str_end))
   
