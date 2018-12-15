import urllib2
from bs4 import BeautifulSoup as bs

#from BeautifulSoup import BeautifulSoup as bs

def get_historical_data(name, number_of_days):
    data = []
    url = "https://finance.yahoo.com/quote/" + name + "/history/"
    rows = bs(urllib2.urlopen(url).read(), "lxml").findAll('table')[0].tbody.findAll('tr')

    for each_row in rows:
        divs = each_row.findAll('td')
        if divs[1].span.text  != 'Dividend': #Ignore this row in the table
            #I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
            data.append({'Date': divs[0].span.text, 'Close': float(divs[1].span.text.replace(',',''))})

    return data[:number_of_days]

#Test
print type(get_historical_data('AAPL', 2500))
a = len(get_historical_data('AAPL', 250))
print a
#for i in get_historical_data('AAPL', 2500):
#    print i                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              