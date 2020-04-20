import pika
from rabbitMq import myQueue

# 普通生产消费者模式
# 生产者
conn = myQueue()
channel = conn.create_channel()  # 声明一个管道
# 声明一个queue, durable=True时，服务器宕机，队列名字持久化，和发消息时，properties参数配合使用，消息不丢失
channel.queue_declare(queue='hello', durable=True)
# 发消息
channel.basic_publish(
    exchange='',  # (交换机)通过绑定exchange,来确定这条消息要发送的范围
    routing_key='hello',  # 队列标识符
    body={'userID': '12', 'time': '2019-10-11 10:24:53'},  # 添加到队列中的消息
    properties=pika.BasicProperties(delivery_mode=2)  # 服务器宕机，队列中消息不丢失
)
conn.close()  # 发送完消息，关闭链接


# 广播, 订阅模式一 fanout
# 生产者
conn1 = myQueue()
channel1 = conn1.create_channel()  # 声明一个管道
# 发布订阅模式，不再需要声明管道，而是是需要声明一个频道
# exchange 类型不同，分发方式不同
#   fanout: 所有bind到此exchange的queue都可以接收消息
#   direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
#   topic: 所有符合routingKey(表达式)的routingKey所bind的queue可以接收消息
channel1.exchange_declare(exchange='all', exchange_type='fanout')

# 发布一条消息，实时发送，发送后消失
channel1.basic_publish(
    exchange='all',  # 通过绑定exchange,来确定这条消息要发送的范围
    routing_key='',  # 不需要队列
    body={'userID': '12', 'time': '2019-10-11 10:24:53'},  # 添加到队列中的消息
)
conn1.close()  # 发送完消息，关闭链接


# 广播, 订阅模式二 direct
# 生产者
conn2 = myQueue()
channel2 = conn2.create_channel()  # 声明一个管道
# 发布订阅模式，不再需要声明管道，而是是需要声明一个频道
# exchange 类型不同，分发方式不同
#   fanout: 所有bind到此exchange的queue都可以接收消息
#   direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
#   topic: 所有符合routingKey(表达式)的routingKey所bind的queue可以接收消息
channel2.exchange_declare(exchange='log', exchange_type='direct')

# 发布一条消息，实时发送，发送后消失
channel2.basic_publish(
    exchange='log',  # 通过绑定exchange,来确定这条消息要发送的范围
    routing_key='info',  # 发送标示
    body={'userID': '12', 'time': '2019-10-11 10:24:53'},  # 添加到队列中的消息
)

# 发布一条消息，routing_key=error
channel2.basic_publish(
    exchange='log',  # 通过绑定exchange,来确定这条消息要发送的范围
    routing_key='error',  # 发送标示
    body={'userID': '12', 'time': '2019-10-11 10:24:53'},  # 添加到队列中的消息
)
conn2.close()  # 发送完消息，关闭链接


# 广播, 订阅模式三 topic
# 生产者
conn3 = myQueue()
channel3 = conn3.create_channel()  # 声明一个管道
# 发布订阅模式，不再需要声明管道，而是是需要声明一个频道
# exchange 类型不同，分发方式不同
#   fanout: 所有bind到此exchange的queue都可以接收消息
#   direct: 通过routingKey和exchange决定的那个唯一的queue可以接收消息
#   topic: 所有符合routingKey(表达式)的routingKey所bind的queue可以接收消息
channel3.exchange_declare(exchange='logFile', exchange_type='topic')

# 发布一条消息，实时发送，发送后消失
channel3.basic_publish(
    exchange='logFile',  # 通过绑定exchange,来确定这条消息要发送的范围
    routing_key='info.log',  # 发送标示
    body={'userID': '12', 'time': '2019-10-11 10:24:53'},  # 添加到队列中的消息
)
conn3.close()  # 发送完消息，关闭链接

