#!/usr/bin/env python

import MySQLdb
import requests, urllib3
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

# Open database connection


# execute SQL query using execute() method.
#cursor.execute("SELECT WebUrl")

# Fetch a single row using fetchone() method.
#data = cursor.fetchone()

#print "Database version : %s " % data

# disconnect from server


def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup

def main(search_string, search_page_total, search_website):
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock" )
     cursor = db.cursor()
     for j in xrange(1,search_page_total+1):
#          url = 'https://www.limetorrents.cc/search/all/udemy/date/2/'
#          url = search_website + '/search/all/' + search_string + '/date/' + str(j)
          if j == 1 :
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
                    sql = "INSERT INTO WebUrl(name, link, key_word) VALUES(%s, %s, %s)"
                    sql2 =  "SELECT count(*) FROM WebUrl where name = %s and link = %s"
                    cursor.execute(sql2, (string_list[1], string_list[0]))
                    result=cursor.fetchone()
                    if result[0] != 0:
                         print string_list[1] + '\t\t' + string_list[0] + '\t\t' + 'already in database!'
                    else:
                         try:
                             # Execute the SQL command
                              cursor.execute(sql, (string_list[1], string_list[0], search_string))
                              print "insert successful"
                              # Commit your changes in the database
                              db.commit()
                         except:
                             # Rollback in case there is any error
                             db.rollback()
                             print "Insert Failed"
#                    print string_list[1] + '\t\t' + string_list[0]
     db.close()

if __name__ == "__main__":
     string_list =["udemy","tutsplus", "tutplus","tuts+","oreilly","o'reilly","lynda", \
                   "cbt nuggest","pluralsight","learn","learning","raspberry pi", 'itpro']

#     string_list =['udemy']
     for s in string_list:
          search_string=s.replace(' ', '-')
          search_page_total = 2
          search_website='https://limetorrents.cc'
          main(search_string, search_page_total, search_website)

