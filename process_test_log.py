"""
    用来测试多进程日志写入情况，
"""

import sys
import time
import multiprocessing
import requests


# 发送debug级别日志消息
def test(num):
    time.sleep(3)
    # logger.debug('日志测试' + str(num))
    for i in range(10):
        requests.get('http://192.168.127.140:3278/member/root/index.json?params={%22a%22:'+str(num)+'}')


if __name__ == '__main__':

    pool = multiprocessing.Pool(processes=10)

    for i in range(10):
        pool.apply_async(func=test, args=(i,))
    pool.close()
    pool.join()
    print('完毕')

import os

# f = os.open('access.log', 1)
