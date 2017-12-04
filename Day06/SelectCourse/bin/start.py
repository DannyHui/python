# -------------------------------
# Task Name：
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
import os
import sys

# 程序文件主目录
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(BASE_DIR)

from core.Main import Main

if __name__ == '__main__':
    main = Main()
    main.run()
    