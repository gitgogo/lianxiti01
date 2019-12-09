#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-09 11:29
# software: PyCharm

import hashlib


def encryption(s):
    hl = hashlib.md5()
    # hl = hashlib.md5(s.encode('utf-8')) # 或者这样写
    hl.update(s.encode('utf-8'))
    return hl.hexdigest().upper()


if __name__ == '__main__':
    print(encryption("i 'am a pen"))
