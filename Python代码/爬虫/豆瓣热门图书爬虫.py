# -*- coding: utf-8 -*-
"""
Created on Tue Apr  3 17:08:49 2018

@author: cg043
"""

import requests
import re

content = requests.get('https://book.douban.com/').text

pattern = re.compile('"book-info">.*?href="(.*?)".*?"_blank">(.*?)<.*?author">(.*?)</div>', re.S)
results = re.findall(pattern, content)

for result in results:
    url,name,author = result
    author = re.sub('\s','',author)
    print(url, name, author)