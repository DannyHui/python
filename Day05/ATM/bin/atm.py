# -------------------------------
# Task Name：
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------
import sys,os

# 程序文件主目录
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 添加环境变量
sys.path.append(path)

from core import main


if __name__ == '__main__':
    main.run()
