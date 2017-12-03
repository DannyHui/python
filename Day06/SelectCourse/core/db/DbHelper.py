# -------------------------------
# Task Name：数据库连接引擎类
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------
import os
from conf import settings

class DbHelper(object):
    def __init__(self,tbname):
        self.database = settings.DATABASE
        self.tbname = tbname

    def file_db_handle(self):
        """
         文件存储数据
         :param database: 数据库配置参数
         :param tbname: 数据表名称
         :return: 返回路径
         """
        db_path = os.path.join(self.database["dbpath"], self.tbname)
        return db_path

    def mysql_db_handle(self):
        """
        mysql存储数据
        :param database: 数据库配置参数
        :param tbname: 数据表名称
        :return: 返回路径
        """
        pass

    def handle(self):
        """
        数据处理
        :param database: 数据库配置参数
        :param tbname: 数据表名称
        :return: 返回路径
        """
        if self.database["engineer"] == "file_storage":
            return file_db_handle(self.tbname)
        if self.database["engineer"] == "mysql":
            return mysql_db_handle(self.tbname)