#!/usr/bin/env python

import requests
#import urllib2
from bs4 import BeautifulSoup

import urllib3
requests.packages.urllib3.disable_warnings()

#from requests.packages.urllib3.exceptions import InsecureRequestWarning
#requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def soup_maker(url):     
     soup = BeautifulSoup(requests.get(url, verify=False).content, "lxml")
     return soup

def main():
#   page = requests.get("https://www.limetorrents.cc/", verify=False)
   url = 'https://www.yahoo.com/'
#   print str(soup_maker(url))[:1000]
   
#   page = requests.get("https://www.limetorrents.cc/", verify=False)
#   page = requests.get("https://www.yahoo.com/", verify=False)   
#   print page.status_code
   soup = soup_maker(url)
   
   try:
     body_texts = soup.body(text=True)
   except:
     return
   text = ''.join(body_texts) 

#   print str(page.content)[:1000]
#   print(soup.prettify())
   if text.find(" Black ") > -1:
     print url
     print



if __name__ == "__main__":
   # if len(sys.argv) > 1:
   #  # Get address from command line.
   #    address = ' '.join(sys.argv[1:])
   # 
   # else:
   #     # Get address from clipboard.
   #     address = pyperclip.paste()
   
   main()
   
# def soup_maker(url):     
#     soup = BeautifulSoup(requests.get(url).content)
#     return soup
# 
# if __name__ == "__main__":
#     import requests    
#     url = 'https://close5.com/home/'
#     print str(soup_maker(url))[:1000]