#!/usr/bin/env/python
# -*-coding:utf-8-*-

import json, re
import requests
from bs4 import BeautifulSoup



url = "http://www.jxmzpz.com/f_top.aspx?cn=2&wid=39"
response = requests.get(url)
# print response.text

soup = BeautifulSoup(response.text, 'lxml')
# print str(soup.find_all("li")).decode("unicode_escape")
li_list = str(soup.find_all("li")).decode("unicode_escape").split(",")
patter = re.compile(r'^(<li><a data-ajax=).*$(</a></li>)')
for li in li_list:
    print li
    # print re.search(r'^(<li><a data-ajax=)(.*)$(</a></li>)', li, flags=0)
    result = patter.findall(li)
    print result
