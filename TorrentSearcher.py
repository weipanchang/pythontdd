#!/usr/bin/env python
import MySQLdb
import urlparse
import requests, urllib3, sys
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()

def soup_maker(url):
     soup = BeautifulSoup(requests.get(url, verify=False).content, "html.parser")
     return soup

def search_by_publisher(search_string, search_page_total, search_website):
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock", use_unicode=True, charset="utf8")
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
#               str2 = str(i).lower()
               if search_string in ["o'reilly","oreilly"]:
                    if i.get_text().encode('utf-8','ignore').lower().startswith(search_string) == False:
                         break
               if  i.get_text().lower().find(search_string) != -1 \
                    and i.get('href') != "https://torrents.me/" \
                    and (i.has_attr('title') == False) \
                    and (i.has_attr('target') == False):
#                    or ((str(i.get('href')).lower())[1:1 + string_search_length:]) == search_string):
#               if str2[:10:] == '<a href="/' and ((str2)[10:10 + string_search_length:] == search_string \
#                    or (str2)[11:11 + string_search_length:] == search_string):                    
#                    string_list = str(i)[10:-4:].split('">')
                    sql1 = "INSERT INTO WebUrl(name, link, key_word) VALUES(%s, %s, %s)"
                    sql2 =  "SELECT count(*) FROM WebUrl where name = %s and link = %s"
                    cursor.execute(sql2, (i.get_text(), urlparse.urljoin(search_website, i.get("href"))))
#                    cursor.execute(sql2, (string_list[1], urlparse.urljoin(search_website, string_list[0])))                    
                    result=cursor.fetchone()
                    if result[0] != 0:
                         None
#                         print i.get_text() + '\t\t' + i.get('href')+ '\t\t' + 'already in database!'
                    else:
                         try:
                             # Execute the SQL command
                              cursor.execute(sql1, (i.get_text() , \
                                                    urlparse.urljoin(search_website, i.get("href")), \
                                                    search_string))
#                              if i.get_text().find('Hadoop') != -1:
                              
#                              print str(i.get_text()) + '\t\t' + urlparse.urljoin(search_website, i.get('href'))+ '\t\t'
#                              print string_list[1] + '\t\t' + urlparse.urljoin(search_website, string_list[0])
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
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock", use_unicode=True, charset="utf8")
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
               if i.get('href') != "https://torrents.me/" \
                    and (i.has_attr('title') == False) \
                    and (i.has_attr('target') == False):
                    for str1 in search_string:
                         if i.get_text().lower().find(str1) == -1:
                              findit = False
#                              print str1, str2, str2.find(str1), findit
                              break
#                    if i.get.text().find('html') == -1:
#                              findit = False
                    if findit == True:
<<<<<<< HEAD
                         string_list = str(i)[10:-4:].split('">')
                         print string_list
=======
#                         string_list = str(i)[10:-4:].split('">')
#                         print string_list
>>>>>>> 60ffd40d48a1a311affa87959dd8ad232ec67ced
                         sql1 = "INSERT INTO WebUrl(name, link, key_word) VALUES(%s, %s, %s)"
                         sql2 =  "SELECT count(*) FROM WebUrl where name = %s and link = %s"
                         cursor.execute(sql2, (i.get_text(), urlparse.urljoin(search_website,  i.get("href"))))
                         result=cursor.fetchone()
                         if result[0] != 0:
                              None
#                              print string_list[1] + '\t\t' + string_list[0] + '\t\t' + 'already in database!'
                         else:
                              try:
                              # Execute the SQL command
                                   cursor.execute(sql1, (i.get_text(), \
                                                       urlparse.urljoin(search_website, i.get("href")), \
                                                       search_keyword.replace("-", " ")))
#                                   print string_list[1] + '\t\t' + "https://www.limetorrents.cc/" + string_list[0]
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
#     string_list =['udemy']
     string_list =["udemy","tutsplus", "tutplus","tuts+" ,"tuts plus","oreilly","o'reilly","lynda", "apress", \
                   "cbt nuggest","pluralsight","skillfeed", "learn","learning","raspberry pi", "raspberry-pi",\
<<<<<<< HEAD
                   "itpro", "sams", "teamtreehouse", "livelessons"]
=======
                   "itpro", "sams", "teamtreehouse", "livelessons", "wrox", "addison wesley", "prentice hall"]
>>>>>>> 60ffd40d48a1a311affa87959dd8ad232ec67ced
     search_website='https://limetorrents.cc'
     if len (sys.argv[1::]) <= 1:
          for s in string_list:
               search_string=s.replace(' ', '-')
               search_page_total = 2
               search_by_publisher(search_string, search_page_total, search_website)
     else:
          search_string = [i.lower() for i in sys.argv[1::]]
<<<<<<< HEAD
          search_page_total = 1
=======
          search_page_total = 2
>>>>>>> 60ffd40d48a1a311affa87959dd8ad232ec67ced
          search_by_keyword(search_string, search_page_total, search_website)
     db = MySQLdb.connect("localhost","root","abc123","Web_Scrape", unix_socket="/opt/lampp/var/mysql/mysql.sock", use_unicode=True, charset="utf8")
     cursor = db.cursor()
     sql1 = "SELECT @time := `date` FROM `WebUrl` group by `date` order by `date` DESC limit 1"
     sql2 = "SELECT * FROM  `WebUrl` WHERE (`date` >= DATE_SUB(@time, INTERVAL 3 SECOND))";
<<<<<<< HEAD
     sql3 = "UPDATE `WebUrl` SET `key_word` = 'tuts plus' WHERE `key_word` = 'tuts+' or `key_word` = 'tutplus'"
=======
     sql3 = "UPDATE `WebUrl` SET `key_word` = 'tuts plus' WHERE `key_word` = 'tuts+' or \
          `key_word` = 'tutplus'  or `key_word` = 'tut-plus'  or `key_word` = 'tutsplus'"
>>>>>>> 60ffd40d48a1a311affa87959dd8ad232ec67ced
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
<<<<<<< HEAD
          print row[1] + "\t" + row[2] + "\t" + row[3]
=======
          print row[1] + "\t" + urlparse.urljoin(search_website, row[2]) + "\t" + row[3]
          print ""
     print ""
     print "The last timestamp is ====>    " + str(row[4])
>>>>>>> 60ffd40d48a1a311affa87959dd8ad232ec67ced
     cursor.execute(sql3)
     cursor.execute(sql4)
     db.commit()
     db.close()
 
