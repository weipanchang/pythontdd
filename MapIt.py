#!/usr/bin/env python
from bs4 import BeautifulSoup
import requests

import sys
reload(sys)
sys.setdefaultencoding('utf8')
#BeautifulSoup(html_text,from_encoding="utf-8")

page = requests.get("https://www.limetorrents.cc/", verify=False)
#https://www.limetorrents.cc/
print page.status_code


soup = BeautifulSoup(page.content, 'html.parser', from_encoding="utf-8")
#print str((soup.prettify()).encode('ascii', 'ignore').decode('ascii'))
print str(soup.prettify())