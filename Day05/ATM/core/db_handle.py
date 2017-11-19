# -------------------------------
# Task Name：数据库连接引擎模块
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------

def file_db_handle(database):
    """
        文件格式存储数据
        :param database:数据配置参数
        :return: 返回路径  ATM/db/accounts
    """
    db_path = "%s/%s" % (database["dbpath"], database["dbname"])
    return db_path

def mysql_db_handle(database):
    """
        mysql存储数据，方便以后对数据存储进行扩展
        :param database:数据库配置参数
    """
    pass


def handle(database):
    """
        数据处理
        :param database: 数据库配置参数
        :return: 返回路径
    """
    if database["engineer"] == "file_storage":
        return file_db_handle(database)
    if database["engineer"] == "mysql":
        return mysql_db_handle(database)