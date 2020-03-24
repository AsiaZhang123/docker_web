import os
import re
import logging.config

# 定义三种日志输出格式
# 其中name为make_logger的参数name
standard_format = '[%(levelname)s][%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s]' \
                  '\n[%(filename)s-%(funcName)s:%(lineno)d][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s-%(funcName)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 项目名
project_name = 'docker_web'
# 日志文件名
logfile_name = '/data/logs/' + project_name

# 日志配置
LOGGING_DIC = {
    'version': 1,
    # 禁用已经存在的logger实例
    'disable_existing_loggers': False,
    # 日志格式化(负责配置log message 的最终顺序，结构，及内容)
    'formatters': {
        'distinct': {
            'format': standard_format
        },
        'simple': {
            'format': simple_format
        },
        'less_simple': {
            'format': id_simple_format
        },
    },
    # 过滤器，决定哪个log记录被输出
    'filters': {},
    # 负责将Log message 分派到指定的destination(目的地)
    'handlers': {
        # 打印到终端的日志
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'distinct'
        },
        # 打印到common文件的日志,收集info及以上的日志
        'common': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'simple',
            'filename': '%s/access.log' % logfile_name,  # 日志文件路径
            'maxBytes': 1024 * 1024 * 5,  # 日志大小 5M
            'backupCount': 5,  # 备份5个日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
        # 打印到importance文件的日志,收集error及以上的日志
        'importance': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件
            'formatter': 'distinct',
            'filename': '%s/importance.log' % logfile_name,  # 日志文件
            # 'maxBytes': 1024*1024*5,  # 日志大小 5M
            'maxBytes': 300,  # 日志大小 300kb
            'backupCount': 5,  # 备份5个日志文件
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    # logger实例
    'loggers': {
        # 默认的logger应用如下配置
        '': {
            'handlers': ['console'],  # log数据打印到控制台
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'default': {
            'handlers': ['console', 'common', 'importance'],
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'common': {
            'handlers': ['console', 'common'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到控制台
            'level': 'INFO',
            'propagate': True,  # 向上（更高level的logger）传递
        },
        'importance': {
            'handlers': ['console', 'importance'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到控制台
            'level': 'ERROR'
        },

    },
}


class Log(object):
    @staticmethod
    def isdir_logs():
        """
        判断日志文件是否存在，不存在则创建
        :return:
        """
        # 当前文件的目录

        # basedir = os.path.dirname(os.path.abspath(__file__))
        # pattern = '(.*/%s)' % project_name
        # project_dir = re.search(pattern, basedir).group()
        # # logs文件的路径
        # log_path = os.path.join(project_dir, logfile_name)
        # # 判断日志文件夹是否在项目文件中
        # if not os.path.isdir(log_path):
        #     os.mkdir(log_path)

        # 判断日志文件夹是否存在
        if not os.path.isdir(logfile_name):
            os.mkdir(logfile_name)

    @staticmethod
    def make_logger(name=None):
        """
        1. 如果不传name，则根据__name__去loggers里查找__name__对应的logger配置(__name__为调用文件名)
        获取logger对象通过方法logging.getLogger(__name__)，不同的文件__name__不同，这保证了打印日志时标识信息不同，
        2. 如果传name,则根据name获取loggers对象
        3. 如果拿着name或者__name__去loggers里找key名时却发现找不到，于是默认使用key=''的配置
        :return: logger
        """
        logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的logging配置
        if name:
            logger = logging.getLogger(name)
        else:
            logger = logging.getLogger(__name__)
        return logger


Log().isdir_logs()
mf_logger = Log.make_logger('default')
mf_logger.info('787878')
