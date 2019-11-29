#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-29 17:44
# software: PyCharm

import os
import time


def main():
    content = '我是一个中国人我爱我的祖国'
    while True:
        # 清理屏幕上的输出
        os.system('clear')  # os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()