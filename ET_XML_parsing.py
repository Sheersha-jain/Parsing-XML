import xml.etree.ElementTree as ET


class DatabaseConfigParser(object):
    def __init__(self, path):
        self.xml_file_path = path
        self.user = ''
        self.host = ''
        self.password = ''

    def parse(self):
        root = ET.parse(self.xml_file_path)
        content = root.find("user")
        self.user = content.text
        self.host = root.find("host").text
        self.password = root.find("password").text
        return {
            'host': self.host,
            'user': self.user,
            'password': self.password
            }



if __name__ == "__main__":
    db_config = DatabaseConfigParser("details.xml")
    print db_config.parse()















#import xml.etree.ElementTree as ET
#
#
#def xml_data():
#    root = ET.parse("details.xml")
#    data = root.findall("database")
#    content = ""
#
#    for database in data:
#       # host = database.find("host")
#       # content += host + '\n '
#        user = logentry.find("user").txt
#        content += host + '\n'
#        user = database.find("user")
#        if user is not None:
#            content += "   Comments: \n        " + user.text + '\n\n'
#        else:
#            content += "No comment made."
#
#    print content
#
#if __name__ == "__main__":
#    xml_data()
