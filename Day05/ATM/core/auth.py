# -------------------------------
# Task Name：用户认证
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------
import os
import time
from core import db_handle
from conf import settings
from core import account


def auth_account(account_id, password,log_obj):
    """
    用户登录认证
    :param acount: 用户名
    :param password: 密码
    :return:如果信用卡未超期，返回用户信息；反之则打印相应提示
    """
    db_path = db_handle.handle(settings.DATABASE)
    # 用户文件
    account_file = "%s\%s.json" % (db_path, account_id)
    # 判断用户是否存在
    if os.path.isfile(account_file):
        account_data = account.get_account(account_id)
        if account_data["password"] == password:
            expire_time = time.mktime(time.strptime(account_data["expire_date"], "%Y-%m-%d"))
            # 信用卡已超期
            if time.time() > expire_time:
                log_obj.error("用户【%s】的信用卡已过期,请尽快联系银行" % account_id)
                print("\033[31;1m用户【%s】的信用卡已过期,请尽快联系银行！" % account_id)
            # 信用卡未超期
            else:
                log_obj.info("用户【%s】登录成功" % account_id)
                return account_data
        else:
            log_obj.error("用户密码不正确")
            print("\033[31;1m用户密码不正确!\033[0m")
    else:
        log_obj.error("用户【%s】不存在!" % account_id)
        print("\033[31;1m 用户【%s】不存在!\033[0m" % account_id)

def login_account(user_data, log_obj):
    """
    用户登录
    :param user_data: 用户信息(dict)
    :param log_obj: 日志对象
    :return: 用户信息正确且信用卡正常则返回用户数据(dict),反之退出程序
    """
    retry = 0
    while not user_data["is_authenticated"] and retry < 3:
        account_id = input("请输入用户名:").strip()
        password = input("请输入密码:").strip()
        user_auth_data = auth_account(account_id, password, log_obj)
        if user_auth_data:
            user_data["is_authenticated"] = True
            user_data["account_id"] = account_id
            print("欢迎【%s】登录" % account_id)
            return user_auth_data
        retry += 1
    else:
        print("用户【%s】尝试输入密码次数达到3次..." % account_id)
        log_obj.error("用户【%s】尝试输入密码次数达到3次..." % account_id)
        exit()
