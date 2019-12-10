#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-29 17:59
# software: PyCharm

import random
import heapq
from functools import reduce

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
            return [d[h], i]
        else:
            d[j] = i

# 完全数
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
        a, b = b, a+b
    return l

# 素数
def prime_num(num):
    if num in [1,2]:
        return True
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

# 水仙花数
def daffodil_num(num):
    if num/100 < 1 or num/100 > 9:
        return False
    if pow(num%10,3)+pow((num//10)%10,3)+pow(num//100, 3) == num:
        return True

# 正整数反转
def reverse_num(num):
    n2 = 0
    while num > 0:
        n2 = n2*10 + num%10
        num //= 10
    return n2

# 最大公约数
def common_div(num1, num2):
    n = min(num1, num2)
    for i in range(n,1,-1):
        if num1%i == 0 and num2%i == 0:
            return i
    return -1

# 最小公倍数
def common_mul(num1, num2):
    n = max(num1, num2)
    for i in range(1, num1*num2):
        ns = n*i
        if ns%num1 == 0 and ns%num2 == 0:
            return ns
    return num1*num2

# 回文数
def recur_num(num):
    temp = num
    n = 0
    while temp > 0:
        n = n*10 + temp%10
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
    peoples = [True]*30
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
            if i * 5 + j * 3 + h // 3 == 100 and h % 3 ==0:
                return i, j, h


# 两数之和 有序数组
def fun(alist, target):
    i, j = 0, len(alist)-1
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

def merge_n(x, y, z):
    return reduce(merge2(x, y), [x, y, z])


if __name__ == '__main__':
    a = [1, 8, 5, 4, 0, 9, 6, 3, 7, 2]
    b = [2, 4, 5, 8, 10, 11, 20]
    # print(two(data, 4))
    # print(search2(b, 12))
    # print([x for x in range(1, 1000) if daffodil_num(x)])
    # print(fib(10))
    # print(recur_num(35953))
    # print(max2(a))
    # print(money_chicken())
    print(fun(b, 16))
