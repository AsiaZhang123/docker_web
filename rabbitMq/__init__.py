import pika

MQ_HOST = '127.0.0.1'
MQ_PORT = 5672
MQ_USER = 'admin'
MQ_PWD = '123456'


class myQueue(object):
    def __init__(self):
        self.connect = None

    def create_channel(self):
        credential = pika.PlainCredentials(MQ_USER, MQ_PWD)  # 设置用户名，密码

        self.connect = pika.BlockingConnection(
            pika.ConnectionParameters(host=MQ_HOST, port=MQ_PORT, credentials=credential)
        )
        return self.connect.channel()  # 返回声明的管道

    def close(self):
        if self.connect is not None:
            self.connect.close()
