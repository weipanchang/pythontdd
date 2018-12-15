#!/usr/bin/env python
#!/usr/bin/env python
import re
import xml.etree.ElementTree as ET
import urllib2
#from BeautifulSoup import BeautifulSoup as bs
from bs4 import BeautifulSoup as bs

def get_historical_data(name, number_of_days):
    data = []
    url = "https://finance.yahoo.com/quote/AMZN/history?p=AMZN"
#    rows = bs(urllib2.urlopen(url).read(), 'lxml').findAll('table')[0].tbody.findAll('tr')
    page = bs(urllib2.urlopen(url).read(), 'lxml').find('body')
    for tag in page.findAll():
        try:
            if tag.attrs['data-value']=="YTD" :
                print "found"            
                key_list = list()
                key_list.extend(list(tag.attrs))
                print key_list
                print tag.prettify()
            # try:
            #     if len(key_list)  ==0:
                print tag.name
        except:
            pass
#     for div in page.findAll():
# #        if "data-reactid" in div.attrs.keys():
# #            if div.attrs['data-reactid'] == '3':
# #            try:
# #                if div.attrs['class'] == "'Mt(15px)', 'drop-down-selector', 'historical'":
#         try:
#             if div.attrs.has_key('class') and div.attrs['class'][2] == 'historical':
# #                print div.attrs['class']
#                 children = div.findChildren()
#                 for child in children:
#                     if child.name =='span':
#                         children2  = child.findChildren()   
#                         for child2 in children2:
#                             if child2.name =='span':
#                                 print child2.prettify()
#         except:
#             pass
    # for span in  page.findAll('span'):
    #     for span2 in span.findAll('span'):
    #         children =  span2.findChildren()
    #         for child in children:
    #             print child.name
# for tag in tags:
#     tags_keys = list()
#     for line in htmlist:
#         aux=BeautifulSoup(line, "html.parser").find(tag)
#         if aux:
#             tags_keys.extend(list(aux.attrs))
#     print(tag+":"+",".join(sorted(set(tags_keys))))
#    doc = rows.prettify()
#    print doc.encode('utf-8')
#    with open("python.txt",'a', encoding='utf-8') as inputfile:
#        inputfile.write(doc)
    # for j in rows.findAll('input'):
    #     try: 
    #         if j.find(attrs={"data-test" :"date-picker-full-range"}):
    #             print "Found"
    #     except:
    #         pass
        #         
        # for tag in j.findAll():
        #     print tag.name
        # for k in j.findAll('input'):
        #     try:
        #         if k.findAll(attrs={"data-test":"date-picker-full-range"}):
        #             print k
        #     except:
        #        pass
#        for k in j.findAll('span'):
#            for l in k.findAll(string =  'Time Period'):
#                print l
            
    # for each_row in rows:
    #     divs = each_row.findAll('td')
    #     if divs[1].span.text  != 'Dividend': #Ignore this row in the table
    #         #I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
    #         data.append({'Date': divs[0].span.text, 'Open': float(divs[1].span.text.replace(',',''))})
    # 
    # return data[:number_of_days]

#Test
# for i in get_historical_data('amzn', 5):
#     print i

# def get_historical_data(name, number_of_days):
#     url = "https://finance.yahoo.com/quote/" + name + "/history/"
# 
#     page = bs(urllib2.urlopen(url).read(), 'lxml')
#     tree = ET.parse(page)

#      
#     rows = page.body.findAll("input", {"data-test","date-picker-full-range"})
#     print rows
get_historical_data('amzn', 5)

#data-test="date-picker-full-range"