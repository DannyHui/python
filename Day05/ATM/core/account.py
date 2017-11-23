# -------------------------------
# Task Name：用户数据操作模块
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------
import json
from core import db_handle
from conf import settings

def get_account(account_id):
    """
    根据用户ID读取用户信息
    :param account_id: 用户ID
    :return: 用户信息的字典
    """
    db_path = db_handle.handle(settings.DATABASE,"account")
    account_file = "%s\%s.json" % (db_path, account_id)
    with open(account_file, "r", encoding="utf-8") as r_file:
        account_data = json.load(r_file)
    return account_data


def update_account(account_data):
    """
    将用户信息更新到文件中
    :param account_data: 用户信息
    :return:
    """
    db_path = db_handle.handle(settings.DATABASE,"account")
    account_file = "%s\%s.json" % (db_path, account_data["id"])
    with open(account_file, "w", encoding="utf-8") as w_file:
        json.dump(account_data, w_file)
