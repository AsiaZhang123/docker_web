from rabbitMq import myQueue


def callback(ch, method, properties, body):
    print(body)
    # ch.basic_ack() 和 auto_ack 配合使用，消费者宕机，消息不丢失
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 普通生产消费者模式
# 消费者
conn = myQueue()
channel = conn.create_channel()  # 声明一个管道
channel.queue_declare(queue='hello')  # 声明一个queue队列
channel.basic_qos(prefetch_count=1)  # 消费者端有超过一条消息积累则不再接收消息
channel.basic_consume(
    queue='hello',
    callback=callback,
    auto_ack=True   # auto_ack True 表示回调函数处理完消息向生产者确认
)
channel.start_consuming()  # 启动消费者


# 订阅发布模式一
# 消费者
conn1 = myQueue()
channel1 = conn1.create_channel()  # 声明一个管道
# 发布订阅模式，消费者需要随机一个管道名，来标示自己
queue_name = channel1.queue_declare(exclusive=True).method.queue  # exclusive排他，意思是生成的名字唯一
# 将随机的管道名，bind到频道
channel1.queue_bind(exchange='all', queue=queue_name)
channel1.basic_consume(
    queue=queue_name,
    callback=callback
)
channel1.start_consuming()  # 启动消费者


# 订阅发布模式二 ，接收指定关键字
# 消费者
conn2 = myQueue()
channel2 = conn2.create_channel()  # 声明一个管道
# 发布订阅模式，消费者需要随机一个管道名，来标示自己
queue_name = channel2.queue_declare(exclusive=True).method.queue  # exclusive排他，意思是生成的名字唯一
# 将随机的管道名，bind到频道,并指定关键字routing_key，可以绑定多个
channel2.queue_bind(exchange='log', queue=queue_name, routing_key='info')
channel2.queue_bind(exchange='log', queue=queue_name, routing_key='error')
channel2.basic_consume(
    queue=queue_name,
    callback=callback
)
channel2.start_consuming()  # 启动消费者


# 订阅发布模式三 匹配关键字
# 消费者
conn3 = myQueue()
channel3 = conn3.create_channel()  # 声明一个管道
channel3.exchange_declare(exchange='logFile', exchange_type='topic')
# 发布订阅模式，消费者需要随机一个管道名，来标示自己
queue_name = channel3.queue_declare(exclusive=True).method.queue  # exclusive排他，意思是生成的名字唯一
# 将随机的管道名，bind到频道,并指定关键字routing_key，可以绑定为字符串匹配模式。
channel3.queue_bind(exchange='logFile', queue=queue_name, routing_key='info.*')
channel3.queue_bind(exchange='logFile', queue=queue_name, routing_key='#')  # “#”号 代表全部接收
channel3.basic_consume(
    queue=queue_name,
    callback=callback
)
channel3.start_consuming()  # 启动消费者


