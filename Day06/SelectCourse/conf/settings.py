# -------------------------------
# Task Name：配置
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------

import os
import sys

# 程序文件主目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 添加环境变量
sys.path.append(BASE_DIR)

# 数据库信息
DATABASE = {
    'engineer': "file_storage",  # 数据存储格式：文件/数据库
    'dbpath': os.path.join(BASE_DIR, "db")  # 数据存储文件路径
}