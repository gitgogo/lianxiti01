#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-29 17:59
# software: PyCharm

# 指定位数的验证码
import random
def auth_code(len=4):
    all = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    for _ in range(len):
        s += random.choice(all)
    return s


if __name__ == '__main__':
    print(auth_code(8))
