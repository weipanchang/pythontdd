#!/usr/bin/env python
import MySQLdb
import urlparse
import requests, urllib3, sys
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup
     
def search_by_keyword(search_website):

     soup = soup_maker(search_website)
     tags = soup.findAll('a')
#          print len(tags)
     for i in tags:
#               print type(i), i, i.contents
          try:
               for child in i.children:
#                    print child, type(child)
                    if child.has_attr('data-attribute'):
                         print child.attrs['data-attribute']
                         par = i.parent
                         atag=par.find('a')
                         print atag.attrs['href']
#                         print par.attrs['href']
          except:
               next

if __name__ == "__main__":
#     string_list =['udemy']

     search_website= 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=dji+drone&rh=i%3Aaps%2Ck%3Adji+drone'
     search_by_keyword(search_website)

