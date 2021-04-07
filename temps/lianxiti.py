#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-29 17:59
# software: PyCharm

import random
import heapq
from functools import reduce
import re


# 指定位数的验证码
def auth_code(len=4):
    all = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    s = ''
    for _ in range(len):
        s += random.choice(all)
    return s


# 两数之和
def two(a, item):
    d = {}
    for i, j in enumerate(a, 1):
        h = item - j
        if h in d:
            return [i, d[h]]
        else:
            d[j] = i


def two_num(data, tar):
    for i in range(2, len(data)):
        temp = data[:i]
        if tar - data[i] in temp:
            return data.index(tar - data[i]), i


# 完全数 如第一个完全数是6，它有约数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3＝6，恰好等于本身
def perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    return False


# 斐波那契数列
def fib(n):
    a, b = 0, 1
    l = []
    for i in range(n):
        l.append(b)
        a, b = b, a + b
    return l


# 素数
def prime_num(num):
    if num in [1, 2]:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# 水仙花数
def daffodil_num(num):
    if num / 100 < 1 or num / 100 > 9:
        return False
    if pow(num % 10, 3) + pow((num // 10) % 10, 3) + pow(num // 100, 3) == num:
        return True


# 正整数反转
def reverse_num(num):
    n2 = 0
    while num > 0:
        n2 = n2 * 10 + num % 10
        num //= 10
    return n2


# 最大公约数
def common_div(num1, num2):
    n = min(num1, num2)
    for i in range(n, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return -1


# 最小公倍数
def common_mul(num1, num2):
    n = max(num1, num2)
    for i in range(1, num1 * num2):
        ns = n * i
        if ns % num1 == 0 and ns % num2 == 0:
            return ns
    return num1 * num2


# 回文数
def recur_num(num):
    temp = num
    n = 0
    while temp > 0:
        n = n * 10 + temp % 10
        temp //= 10
    if n == num:
        return True
    return False


# 取给定数组中最大和第二大的数
def max2(x):
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for i in range(2, len(x)):
        if x[i] > m1:
            m2 = m1
            m1 = x[i]
        elif x[i] > m2:
            m2 = x[i]
    return m1, m2


# 约瑟夫环问题
def main2():
    peoples = [True] * 30
    count = index = num = 0
    while count < 15:
        if peoples[index]:
            num += 1
            if num == 9:
                count += 1
                peoples[index] = False
                num = 0
        index += 1
        index %= 30
    return peoples


# 百钱白鸡: 公鸡5元一只；母鸡3元一只；小鸡1元3只；用100元买100只鸡
def money_chicken():
    for i in range(20):
        for j in range(33):
            h = 100 - i - j
            if i * 5 + j * 3 + h // 3 == 100 and h % 3 == 0:
                return i, j, h


# 从s = "123.45.33.211?21.23.44.122?!10.11.23.22!kk.90.77.122" 中获取ip 并以ip的最后一个字段排序
def get_ip(s):
    ip_list = re.split(r'\?|!', s)
    ip_list = [x for x in ip_list if is_ip(x)]
    return sorted(ip_list, key=lambda x: int(x.split('.')[-1]), reverse=True)


def is_ip(ip):
    if re.match(r'(\d{1,3}\.){3}\d{1,3}', ip):
        return True
    else:
        return False


# 两数之和 有序数组
def fun(alist, target):
    i, j = 0, len(alist) - 1
    while j > i:
        two = alist[i] + alist[j]
        if two == target:
            return i, j
        elif two < target:
            i += 1
        else:
            j -= 1
    return -1


# N个有序的数组合并成一个数组
def merge_n(nlist):
    def merge2(alist, blist):
        i, j = 0, 0
        result = []
        while i < len(alist) and j < len(blist):
            if alist[i] <= blist[j]:
                result.append(alist[i])
                i += 1
            elif alist[i] > blist[j]:
                result.append(blist[j])
                j += 1
        result += alist[i:]
        result += blist[j:]
        return result

    return reduce(lambda x, y: merge2(x, y), nlist)


# 最长对称字符串
def longest_str(s):
    max = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i:j + 1] == s[i:j + 1][::-1] and j - i > max:
                max = j + 1 - i
    return max


# 删除对称字符串 abcbd-->ad  abcbag-->g
def remove_str(s):
    i, j = 0, 1
    while i < len(s) - 1:
        if s[i:j + 1] == s[i:j + 1][::-1]:
            s = s[:i] + s[j + 1:]
            i, j = 0, 1
        elif j < len(s) - 1:
            j += 1
        else:
            i += 1
            j = i + 1
    return s


def remove_str2(s):
    i = 0
    while i < len(s) - 1:
        j = i + 1
        while j < len(s):
            if s[i:j + 1] == s[i:j + 1][::-1]:
                s = s[:i] + s[j + 1:]
                i, j = 0, 1
            else:
                j += 1
        i += 1
    print(s)


# 冒泡排序用 while写法
def sorted2(alist):
    i, j = 0, 0
    while i < len(alist) - 1:
        if j < len(alist) - 1 - i and alist[j] > alist[j + 1]:
            alist[j], alist[j + 1] = alist[j + 1], alist[j]
            j += 1
        elif j < len(alist) - 1 - i:
            j += 1
        else:
            i += 1
            j = 0
    return alist


# 整数反转
def reverse_int(tar):
    result = 0
    while tar > 0:
        result = result * 10 + tar % 10
        tar //= 10
    return result


if __name__ == '__main__':
    a = [1, 8, 5, 4, 0, 7, 9, 2, 11]
    b = [2, 4, 5, 8, 10, 11, 20]
    c = [1, 3, 4, 7, 12]
    d = [6, 23, 31, 44]
    s = "123.45.33.211?21.23.44.122?!10.11.23.22!kk.90.77.122"
    # print(longest_str('gooogooole'))
    print(reverse_int(1342))
