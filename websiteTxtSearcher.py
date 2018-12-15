# websiteTxtSearcher.py
# Searches a website recursively for any given string.
# FB - 201009105
import urllib2
from os.path import basename
import urlparse
#import BeautifulSoup # for HTML parsing
from bs4 import BeautifulSoup

import requests
# import ssl
# 
# ccontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# context.verify_mode = ssl.CERT_NONE
# context.check_hostname = False

# This restores the same behavior as before.

global urlList
urlList = []

# recursively search starting from the root URL
def searchUrl(url, level, searchText): # the root URL is level 0
    # do not go to other websites
    global website
    netloc = urlparse.urlsplit(url).netloc.split('.')
    if netloc[-2] + netloc[-1] != website:
        return

    global urlList
    if url in urlList: # prevent using the same URL again
        return

    try:
#        context = ssl._create_unverified_context()
        urlContent = urllib2.urlopen(url,context=context, verify=False).read()
#        soup = BeautifulSoup(''.join(urllib2.urlopen(url,context=context).read()), verify=False)
        urlList.append(url)
    except:
        return

    soup = BeautifulSoup(''.join(urlContent))

    # remove script tags
    c=soup.findAll('script')
    for i in c:
        i.extract() 
    # get text content of the URL
    try:
        body_texts = soup.body(text=True)
        
    except:
        return
    text = ''.join(body_texts)
    

    # search
    if text.find(searchText) > -1:
        print url
        print

    # if there are links on the webpage then recursively repeat
    if level > 0:
        linkTags = soup.findAll('a')
        if len(linkTags) > 0:
            for linkTag in linkTags:
                try:
                    linkUrl = linkTag['href']
                    searchUrl(linkUrl, level - 1, searchText)
                except:
                    pass

# main
rootUrl = 'https://www.yahoo.com'
#rootUrl = 'https://www.limetorrents.cc'
netloc = urlparse.urlsplit(rootUrl).netloc.split('.')
global website
website = netloc[-2] + netloc[-1]
searchUrl(rootUrl, 1, " Man ")

