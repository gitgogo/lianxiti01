#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/14 21:50
# @Author  : ralphliu
# @Site    : 
# @File    : lianxi02.py
# @Software: PyCharm

import heapq


# 输出数组中第二大、第三大的数字；第n大-用heapq的方法
# index1 = map(alist.index, heapq.nlargest(3, alist))
def the_second_num(alist):
    one, two, three = alist[0:3]
    for i in range(len(alist)):
        if alist[i] > one:
            three = two
            two = one
            one = alist[i]
        elif alist[i] > two:
            three = two
            two = alist[i]
        elif alist[i] > three:
            three = alist[i]
    return one, two, three


# 获取字符串中出现次数最多的字符及出现次数
def get_largest_str(s):
    d = {}
    for i in s:
        d[i] = s.count(i)
    max_str = max(d, key=lambda x: d[x])
    return max_str, d[max_str]


if __name__ == '__main__':
    alist = [2, 3, 1, 23, 5, 19, 20, 7]
    s = 'abcadabceegdda'
    print(get_largest_str(s))
