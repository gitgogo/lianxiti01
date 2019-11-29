#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-18 16:59
# software: PyCharm


def mao(data):
    n = len(data)
    for i in range(n-1):
        for j in range(n-1-i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def merge(data):
    n = len(data)
    if n <= 1:
        return data
    mid = n // 2
    left = merge(data[:mid])
    right = merge(data[mid:])
    left_p = right_p = 0
    result = []
    while left_p < len(left) and right_p < len(right):
        if left[left_p] <= right[right_p]:
            result.append(left[left_p])
            left_p += 1
        else:
            result.append(right[right_p])
            right_p += 1
    result += left[left_p:]
    result += right[right_p:]


def quick_sort(alist, first, last):
    if first >= last:
        return
    n = len(alist)
    low = first
    high = last
    mid = alist[low]
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        alist[low], alist[high] = alist[high], alist[low]

        while low < high and alist[low] < mid:
            low += 1
        alist[low], alist[high] = alist[high], alist[low]
    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)
    return alist


def search(a, item):
    while len(a) > 0:
        mid = len(a) // 2
        if item == a[mid]:
            return True
        if item > a[mid]:
            a = a[mid + 1:]
        else:
            a = a[:mid]
    return False


def search2(a, item):
    if len(a) > 0:
        mid = len(a)//2
        if a[mid] == item:
            return True
        elif a[mid] > item:
            return search2(a[:mid], item)
        elif a[mid] < item:
            return search2(a[mid+1:], item)
    else:
        return False


def two(a, item):
    d = {}
    for i, j in enumerate(a, 1):
        h = item - j
        if h in d:
            return [i, d[h]]
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


if __name__ == '__main__':
    data = [12, 23, 3, 33, 10, 1, 41, 5]
    b = mao(data)
    # print(merge_sort(data))
    # print(quick_sort(data, 0, 7))
    # print(two(data, 4))
    # print(search2(b, 12))
    print([x for x in range(1, 1000) if daffodil_num(x)])
    print(fib(10))
    print(recur_num(35953))
