
# 指定镜像
FROM python:3.8

# 作者信息
MAINTAINER zyz <zhangyazhou@mofanghr.com>

# 设置docker容器的时区
RUN mv /etc/localtime /etc/localtime_bak
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime

# 创建工作目录
RUN mkdir /root/project -p
WORKDIR /root/project

# 安装vim 方便维护
RUN apt-get update
RUN apt-get install vim -y

# 安装运行依赖包
RUN pip install flask==1.1.1 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install flask-sqlalchemy==2.4.1 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install tornado==6.0.4 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install psycopg2==2.8.4 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install gevent==1.4.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install gunicorn==20.0.4 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install BeautifulReport==0.1.2 -i https://pypi.tuna.tsinghua.edu.cn/simple/
RUN pip install pika==1.1.0 -i https://pypi.tuna.tsinghua.edu.cn/simple/

# 设置容器启动运行命令
CMD /bin/bash