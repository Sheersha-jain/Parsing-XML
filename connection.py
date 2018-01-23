import MySQLdb
import ET_XML_parsing
from ET_XML_parsing import DatabaseConfigParser
import xml.etree.ElementTree as ET

parser_ojetct = DatabaseConfigParser()
parser_object.parse(self)



#class Mysqlconnection:
#    def connection():
#        data=xml_parsing.xmlparsing()
#        print data
#        db = MySQLdb.connect(ipaddr="",    
#                     user="",         
#                     passwd="",  
#                     )        
#
#    connection()
#

###
def connection():
        user,passwd,ipaddr=xml_parsing.xmlparsing()
        print user
        print passwd
        print ipaddr

connection()
###

#import pymysql.cursors
#import pymysql
#connection = pymysql.connect(user='',
#                             password='',
#                             ipaddr='')



#import mysql.connector
#cnx = mysql.connector.connect(user='', password='',
#                              
#                              database='employees')

#try:
#   cursor = cnx.cursor()
#   cursor.execute("""
#      select 3 from your_table
#   """)
#   result = cursor.fetchall()
#   print result
#finally:
#    cnx.close()
