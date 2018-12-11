#!/usr/bin/python

import xml.dom.minidom

print("==========zadanie17==========")

xml_object = xml.dom.minidom.parse("ex_xml.xml")
xml_object.getElementsByTagName("menu")

print(xml_object.documentElement.nodeName + ", " + xml_object.documentElement.getAttribute('date'))

courses = xml_object.getElementsByTagName("course")
course_num = 0
for course in courses:
    course_num = course_num + 1
    print(course.nodeName + " number " + str(course_num))
    name = course.getElementsByTagName('name')[0]
    print("Name: " + str(name.childNodes[0].data))
    price = course.getElementsByTagName('price')[0]
    print("Price: " + str(price.childNodes[0].data))
    waiting_time = course.getElementsByTagName('waiting_time')[0]
    print("Waiting time: " + str(waiting_time.childNodes[0].data))
    ingredients = course.getElementsByTagName('ingredient')
    for ingredient in ingredients:
        print("Ingredient: " + str(ingredient.childNodes[0].data))

menu = xml_object.getElementsByTagName("menu")

menu[0].setAttribute("date", "2019-01-01")

file = open("ex_xml_changed.xml", "w")
xml_object.writexml(file)
file.close()
