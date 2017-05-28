#!/usr/bin/env python

import requests
#import urllib2
from bs4 import BeautifulSoup

import urllib3
requests.packages.urllib3.disable_warnings()


def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup

def main():
#   page = requests.get("https://www.limetorrents.cc/", verify=False)
   url = 'https://www.limetorrents.cc/search/all/udemy/date/2/'
#   urlContent = urllib3.urlopen(url,context=context).read()
#   url = 'https://www.limetorrents.cc/search/all/udemy/'
#   page = requests.get("https://www.limetorrents.cc/", verify=False)
#   page = requests.get("https://www.yahoo.com/", verify=False)
#   print page.status_code
#   soup = BeautifulSoup(''.join(urlContent))
   soup = soup_maker(url)
   name_box = soup.find_all('a')
#   print
#   print name_box
   for i in name_box:
#     if (type(str(i)) == 'str') and str(i).startwith('<a href='):
#     if (isinstance(str(i), basestring) == True) and str(i)[:8:] == '<a href=':
#     if type(str(i)) == str and str(i)[:15:] == '<a href="/Udemy':
     if str(i)[:15:] == '<a href="/Udemy':
          print str(i)[10::]
   # 
   # try:
   #   body_texts = soup.body(text=True)
   # except:
   #   return
   # text = ''.join(body_texts)
   # 
   # if text.find("Machine") > -1:
   #   print url
   #   print



if __name__ == "__main__":
   # if len(sys.argv) > 1:
   #  # Get address from command line.
   #    address = ' '.join(sys.argv[1:])
   #
   # else:
   #     # Get address from clipboard.
   #     address = pyperclip.paste()
   main()
