# -------------------------------
# Task Name：日志记录模块
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------

import logging
from conf import settings

"""
:param logging_type: 日志类型
:return: 返回logger日志对象
"""


def log(logging_type):
    # 生成日志对象
    logger = logging.getLogger(logging_type)
    # 设置日志级别
    logger.setLevel(settings.LOG_LEVEL)

    # 日志打印到屏幕，获取对象
    ch = logging.StreamHandler()
    ch.setLevel(settings.LOG_LEVEL)

    # 获取文件日志对象及日志文件
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_File[logging_type])
    fh = logging.FileHandler(log_file, "a", encoding="utf-8")
    fh.setLevel(settings.LOG_LEVEL)

    # 日志格式
    formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")

    # 输出格式
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把日志打印到指定的handler
    logger.addHandler(ch)
    logger.addHandler(fh)

    # log方法返回logger对象
    return logger
