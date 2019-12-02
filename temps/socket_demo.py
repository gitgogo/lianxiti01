#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-12-02 12:02
# software: PyCharm

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from threading import Thread
from json import dumps


class FileTransferHandler(Thread):

    def __init__(self, cclient):
        super().__init__()
        self.cclient = cclient

    def run(self):
        d = dict(filename='1.png')
        json_str = dumps(d)
        self.cclient.send(json_str.encode('utf-8'))
        self.cclient.close()


def service():
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind(('127.0.0.1', 5555))
    server.listen(512)
    print('服务端开始监听...')
    while True:
        client, addr = server.accept()
        print(f'{str(addr)} 连接到了服务器')
        client.send(str(datetime.now()).encode('utf-8'))
        client.close()


def Client():
    client = socket()
    client.connect(('127.0.0.1', 5555))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    service()
