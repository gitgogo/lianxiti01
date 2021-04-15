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

def selectSort(data):
    length = len(data)
    for i in range(length-1):
        minindex = i
        for j in range(i+1, length):
            if data[j] < data[minindex]:
                minindex = j
        data[i], data[minindex] = data[minindex], data[i]
    return data

def findKmin(data, k):
    for i in range(k):
        minindex = i
        minval = data[i]
        for j in range(i+1, len(data)):
            if data[j] < minval:
                minval = data[j]
                minindex = j
        data[i], data[minindex] = data[minindex], data[i]
    return data[:k]

def insertSort(arr):
    length = len(arr)
    if length <= 1:
        return
    for i in range(1, length):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value
    return arr

def bubbleSort(arr):
    length = len(arr)
    for i in range(length-1):
        for j in range(length-1 -i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def binSearch(arr, tar):
    f, l = 0, len(arr)
    mid = -1
    try:
        while f<=l and mid<len(arr)-1:
            mid = (l-f)//2 +f
            if tar == arr[mid]:
                return mid
            elif tar > arr[mid]:
                f = mid +1
            elif tar < arr[mid]:
                l = mid -1
        return -1
    except Exception as e:
        print(e, mid, l, f)


if __name__ == '__main__':
    data = [12, 23, 3, 33, 10, 1, 41, 5]
    b = maopao(data)
