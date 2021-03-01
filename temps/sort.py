#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-18 16:59
# software: PyCharm


def maopao(data):
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
    return result


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


if __name__ == '__main__':
    data = [12, 23, 3, 33, 10, 1, 41, 5]
    b = maopao(data)
    # print(merge_sort(data))
    # print(quick_sort(data, 0, 7))
    # print(two(data, 4))
    print(search2(b, 12))
