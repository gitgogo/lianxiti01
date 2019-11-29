#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-10-16 14:33
# software: PyCharm

import requests
import re


def down():
    base_url = "http://118.25.22.36/mysql/"
    # content = requests.get(url).content
    with open("/Users/finup/Desktop/tmp.html") as f:
        content = f.read()
        urls = re.findall('<a href="(.*)"', content)
        for url in urls:
            print(url)
            text = requests.get(base_url+url).content
            with open("/Users/finup/Documents/geek-mysql/"+url, 'wb') as f:
                f.write(text)


if __name__ == '__main__':
    down()