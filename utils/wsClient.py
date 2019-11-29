#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-12 19:55
# software: PyCharm
from threading import Thread
import websocket
import time


# 建立简单ws连接
# ws = websocket.WebSocket()
# ws.connect("ws://echo.websocket.org")

def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
        for i in range(3):
            ws.send("hello-%d" % i)
            time.sleep(1)
        time.sleep(1)
        ws.close()
        print("ws closed...")
    Thread(target=run).start()


# 短连接
from websocket import create_connection
ws = create_connection("ws://echo.websocket.org/")
print("Sending 'Hello, World'...")
ws.send("Hello, World")
result = ws.recv()
print("Received '%s'" % result)
ws.close()


if __name__ == '__main__':
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    # 长连接
    ws.run_forever()
