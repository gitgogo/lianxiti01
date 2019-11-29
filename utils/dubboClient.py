#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-15 16:18
# software: PyCharm

# Hessian
from pyhessian.client import HessianProxy
from pyhessian import protocol
import json


def invoke_hessian(service, interface, method, req, retcode='000000'):
    try:
        url = 'http://192.168.0.1:10883/' + service + '.' + interface
        res = getattr(HessianProxy(url), method)(req)
        print('Res:\t%s' % json.dumps(res, ensure_ascii=False))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    service = 'com.service.common.api.service'
    interface = 'TestHessianService'
    method = 'testHessian'
    req = protocol.object_factory('com.service.common.api.service.model.req.TestHessianRequest',
                                  param1='lovesoo', param2=10086)
    invoke_hessian(service, interface, method, req)


# 或者另外一种测试方法
# import dubbo_telnet
#
#
# def coondoubble_data(Host, Port, interface, method, param):
#     try:
#         # 初始化dubbo对象
#         conn = dubbo_telnet.connect(Host, Port)
#         # 设置telnet连接超时时间
#         conn.set_connect_timeout(10)
#         # 设置dubbo服务返回响应的编码
#         conn.set_encoding('gbk')
#         conn.invoke(interface, method, param)
#         command = 'invoke %s.%s(%s)' % (interface, method, param)
#         return conn.do(command)
#     except:
#         return Exception
#
#
# if __name__ == "__main__":
#     Host = '192.168.1.203'  # Doubble服务器IP
#     Port = 28008  # Doubble服务端口
#     interface = 'com.zrj.pay.trade.api.QueryTradeService'  # 接口
#     method = 'tradeDetailQuery'  # 方法
#     param = '{"message": "HelloWorld"}'  # 参数
#     data = coondoubble_data(Host, Port, interface, method, param)
#     print(data)
