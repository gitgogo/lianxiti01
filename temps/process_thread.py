#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 22:55
# @Author  : ralphliu
# @Site    : 
# @File    : process_thread.py
# @Software: PyCharm

from multiprocessing import Process
from random import randint
from time import time, sleep
from os import getpid
from threading import Thread, Lock


def download(filename):
    print(f'启动下载进程，进程号{getpid()}')
    print(f'开始下载{filename}...')
    time_go = randint(5, 10)
    sleep(time_go)
    print(f'{filename}下载完成，耗时{time_go}秒。。')


class Download2(Thread):

    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'启动下载进程，进程号{getpid()}')
        print(f'开始下载{self._filename}...')
        time_go = randint(5, 10)
        sleep(time_go)
        print(f'{self._filename}下载完成，耗时{time_go}秒。。')


def multi_process():
    start = time()
    p1 = Process(target=download, args=('母猪产后护理.pdf',))
    p1.start()
    p2 = Process(target=download, args=('python.pm4',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print(f'总共耗费{(end-start)}')


def multi_thread():
    start = time()
    t1 = Thread(target=download, args=('母猪产后护理.pdf',))
    t1.start()
    t2 = Thread(target=download, args=('python.pm4',))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print(f'总共耗费{(end - start)}')


def multi_thread2():
    start = time()
    t1 = Download2('母猪产后护理.pdf')
    t1.start()
    t2 = Download2('python.pm4')
    t2.start()
    t1.join()
    t2.join()
    print(f'总共耗费{(time() - start)}')


class Account:

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def multi_process_share():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f'账户余额{account.balance}')


if __name__ == '__main__':
    # multi_thread2()
    multi_process_share()
