#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:liudongjie
# datetime:2019-11-11 16:04
# software: PyCharm

import xml.etree.ElementTree as et
import sys


def edit_xml(file_path, test_file):
    XML_NS_NAME = ""
    XML_NS_VALUE = "http://maven.apache.org/POM/4.0.0"
    et.register_namespace(XML_NS_NAME, XML_NS_VALUE)
    POM_NS = "{http://maven.apache.org/POM/4.0.0}"
    tree = et.parse(file_path)
    root = tree.getroot()
    for child in root.iter('%sjMeterTestFile' %POM_NS):
        # print(child.text)
        child.text = test_file
    tree.write(file_path)


if __name__ == '__main__':
    file_path = '/Users/finup/Downloads/pom.xml'
    test_file = sys.argv[1]
    edit_xml(file_path, test_file)
