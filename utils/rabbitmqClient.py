#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:finup
# datetime:2019-11-13 15:18
# software: PyCharm
import pika

# 生产者
conn = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = conn.channel()
channel.exchange_declare(exchange='topic.exch',
                         exchange_type='topic')
# 在RabbitMQ中，消息永远不会直接发送到队列，它总是需要经过交换
channel.basic_publish(exchange='topic.exch',
                      routing_key='*.red.#',
                      body='hello, mq-12',
                      properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                      ))
conn.close()

# 消费者
conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = conn.channel()
channel.exchange_declare(exchange='topic.exch',
                      exchange_type='topic')
result = channel.queue_declare(queue='hello.6',
                               exclusive=True,) # 断开连接后删除队列exclusive=True
queue_name = result.method.queue
channel.queue_bind(exchange='topic.exch', queue=queue_name, routing_key='info.red.*')

# 当获取到消息的时候，Pika库就会调用此回调函数。
def callback(ch, method, propertites, body):
    print("received {}".format(body))
    # 手动确认mq消息接收
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue=queue_name,
                      on_message_callback=callback)

# 接收mq消息
channel.start_consuming()
