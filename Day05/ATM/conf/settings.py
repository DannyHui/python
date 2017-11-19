# -------------------------------
# Task Name：配置信息模块
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------

import os
import sys
import logging

# 程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加环境变量
sys.path.append(BASE_DIR)

# 数据库信息
DATABASE = {
    'engineer': "file_storage",  # 数据存储格式：文件/数据库
    'dbname': "accounts",  # 数据文件存储目录名称
    'dbpath': os.path.join(BASE_DIR, "db")  # 数据文件路径
}
# 日志信息
# 日志级别
LOG_LEVEL = logging.INFO
# 日志文件
LOG_File = {
    'access': "access.log" #访问日志
}
