#!/usr/bin/env python

import requests, urllib3
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup

def main(search_string, search_page_total, search_website):
     for j in xrange(search_page_total+1):
#          url = 'https://www.limetorrents.cc/search/all/udemy/date/2/'
#          url = search_website + '/search/all/' + search_string + '/date/' + str(j)
          if j == 0 :
               url = search_website + '/search/all/' + search_string
          else:
               url = search_website + '/search/all/' + search_string + '/date/' + str(j)
          soup = soup_maker(url)
          name_box = soup.find_all('a')
     
          for i in name_box:
               string_search_length = len(search_string)
               str2 = str(i).lower()
               if str2[:10:] == '<a href="/' and ((str2)[10:10 + string_search_length:] == search_string \
                    or (str2)[11:11 + string_search_length:] == search_string):
                    string_list = str(i)[10:-4:].split('">')
                    print string_list[1] + '\t\t' + string_list[0]  

if __name__ == "__main__":
     string_list =['udemy','tutsplus', 'tutplus','tuts+','oreilly','o\'reilly','lynda','cbt nuggest','pluralsight','learn','learning']
     for s in string_list:
          search_string=s.replace(' ', '-')
          search_page_total = 1
          search_website='https://limetorrents.cc'
          main(search_string, search_page_total, search_website)
