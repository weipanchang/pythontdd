#!/usr/bin/env python

import MySQLdb
import requests, urllib3, sys
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup

def search_by_publisher(search_string, search_page_total, search_website):
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock" )
     cursor = db.cursor()
     for j in xrange(1,search_page_total+1):
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
                    sql1 = "INSERT INTO WebUrl(name, link, key_word) VALUES(%s, %s, %s)"
                    sql2 =  "SELECT count(*) FROM WebUrl where name = %s and link = %s"
                    cursor.execute(sql2, (string_list[1], string_list[0]))
                    result=cursor.fetchone()
                    if result[0] != 0:
                         None
#                         print string_list[1] + '\t\t' + string_list[0] + '\t\t' + 'already in database!'
                    else:
                         try:
                             # Execute the SQL command
                              cursor.execute(sql1, (string_list[1], string_list[0], search_string))
#                             print "insert successful"
                              # Commit your changes in the database
                              db.commit()
                         except:
                             # Rollback in case there is any error
                             db.rollback()
#                             print "Insert Failed"
#                    print string_list[1] + '\t\t' + string_list[0]
     db.close()
     
def search_by_keyword(search_string, search_page_total, search_website):
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock" )
     cursor = db.cursor()
     search_keyword = '-'.join(search_string)
#     print search_keyword
     for j in xrange(1,search_page_total+1):

          if j == 1 :
               url = search_website + '/search/all/' + search_keyword
          else:
               url = search_website + '/search/all/' + search_keyword + '/date/' + str(j)
          soup = soup_maker(url)
          name_box = soup.find_all('a')
     
          for i in name_box:
#               string_search_length = len(search_string)
               str2 = str(i).lower()
               findit = True
               if str2[:10:] == '<a href="/':
                    for str1 in search_string:
                         if str2.find(str1) == -1:
                              findit = False
#                              print str1, str2, str2.find(str1), findit
                              break
                         if str2.find('html') == -1:
                              findit = False
                    if findit == True:
                         string_list = str(i)[10:-4:].split('">')
                         print string_list
                         sql1 = "INSERT INTO WebUrl(name, link, key_word) VALUES(%s, %s, %s)"
                         sql2 =  "SELECT count(*) FROM WebUrl where name = %s and link = %s"
                         cursor.execute(sql2, (string_list[1], string_list[0]))
                         result=cursor.fetchone()
                         if result[0] != 0:
                              None
#                              print string_list[1] + '\t\t' + string_list[0] + '\t\t' + 'already in database!'
                         else:
                              try:
                              # Execute the SQL command
                                   cursor.execute(sql1, (string_list[1], string_list[0], search_keyword.replace("-", " ")))
#                                   print string_list[1] + '\t\t' + string_list[0]
#                                   print "Insert Successful"
                               # Commit your changes in the database
                                   db.commit()
                              except:
#                                  Rollback in case there is any error
                                   db.rollback()
#                                  print string_list[1] + '\t\t' + string_list[0]
                                   print "Insert Failed"
#                    print string_list[1] + '\t\t' + string_list[0]
     db.close()     

if __name__ == "__main__":
     string_list =["udemy","tutsplus", "tutplus","tuts+" ,"tuts plus","oreilly","o'reilly","lynda", "apress", \
                   "cbt nuggest","pluralsight","skillfeed", "learn","learning","raspberry pi", "raspberry-pi",\
                   "itpro", "sams", "teamtreehouse", "livelessons"]
     search_website='https://limetorrents.cc'
     if len (sys.argv[1::]) <= 1:
#     string_list =['udemy']
          for s in string_list:
               search_string=s.replace(' ', '-')
               search_page_total = 2
               search_by_publisher(search_string, search_page_total, search_website)
     else:
          search_string = [i.lower() for i in sys.argv[1::]]
          search_page_total = 1
          search_by_keyword(search_string, search_page_total, search_website)
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock" )
     cursor = db.cursor()
     sql1 = "SELECT @time := `date` FROM `WebUrl` group by `date` order by `date` DESC limit 1"
     sql2 = "SELECT * FROM  `WebUrl` WHERE (`date` >= DATE_SUB(@time, INTERVAL 3 SECOND))";
     sql3 = "UPDATE `WebUrl` SET `key_word` = 'tuts plus' WHERE `key_word` = 'tuts+' or `key_word` = 'tutplus'"
     sql4 = "UPDATE `WebUrl` SET `key_word` = 'raspberry pi' WHERE `key_word` = 'raspberry-pi'"
     cursor.execute(sql1)
     cursor.execute(sql2)
     result = cursor.fetchall()
     print ""
     print ""
     print ""
     print "                The last inserted record!          "
     print "================================================="
     print ""
     for row in result:
          print row[1] + "\t" + row[2] + "\t" + row[3]
     cursor.execute(sql3)
     cursor.execute(sql4)
     db.commit()
     db.close()
     
     


          
          

