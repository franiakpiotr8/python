# !python

import xml.sax


class XmlHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.data = ""
        self.name = ""
        self.price = ""
        self.waiting_time = ""
        self.ingredients = list()
        self.course_num = 0

    def startElement(self, tag, attributes):
        self.data = tag
        if tag == "menu":
            date = attributes["date"]
            print("Menu, date: " + date)

        elif tag == "course":
            self.course_num = self.course_num + 1
            self.ingredients.clear()
            print("Course number " + str(self.course_num))

    def endElement(self, tag):
        if tag == "name":
            print("Name:", self.name)
        elif tag == "price":
            print("Price:", self.price)
        elif tag == "waiting_time":
            print("Waiting time:", self.waiting_time)
        elif tag == "course":
            print("Ingredients:", self.ingredients)


    def characters(self, content):
        if self.data == "name":
            self.name = content
        elif self.data == "price":
            self.price = content
        elif self.data == "waiting_time":
            self.waiting_time = content
        elif self.data == "ingredient" and not content.isspace():
            self.ingredients.append(content)


print("==========zadanie17==========")
print("Parsing file: ex_xml.xml ")

parser = xml.sax.make_parser()
Handler = XmlHandler()
parser.setContentHandler(Handler)

parser.parse("ex_xml.xml")
