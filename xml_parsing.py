from xml.dom.minidom import parse
import xml.dom.minidom

def xmlparsing():

    DOMTree = xml.dom.minidom.parse("details.xml")
    collection = DOMTree.documentElement
    print 'host:'+collection.getElementsByTagName("host")
    print 'USER' + collection.getElementsByTagName("user")
    print 'password' + collection.getElementsByTagName("password")
   #  print collection
   #  data = collection.getElementsByTagName("host")
   # # data = collection.getElementsByTagName("host")
   # # data =  collection.getElementsByTagNameNS("database")
   #  print data
   #  for information in data:
   #      print "*****Information*****"
   #      print data
   #      if data.hasAttribute("title"):
   #          print "Title: %s" % data.getAttribute("title")
   #
   #  host = data.getElementsByTagName('host')[0]
   #  print "host: %s" % host.childNodes[0].data
   #  user = data.getElementsByTagName('user')[0]
   #  print "user: %s" % user.childNodes[0].data
   #  password = data.getElementsByTagName('password')[0]
   #  print "password: %s" % password.childNodes[0].data

xmlparsing()


















"""
import re
import sys

def xmlparsing():

    f = open('details.xml', 'rU')
    data = f.read()
    print data 



    IP =  re.findall(r'>\d+<', data)
    print IP

    x=re.findall(r'>(\w+)<', data)
    user = x[0]
#    print user

    password = x[1]
#    print password
    #print (user,password,IP)
    return (user,password,IP)"""
