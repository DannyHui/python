# -------------------------------
# Task Name：主要业务逻辑交互模块
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------

from core import log
from core import account
from core import auth

# 用户数据信息
user_data = {
    'account_id': None,  # 帐号ID
    'is_authenticated': False,  # 是否认证
    'account_data': None  # 帐号数据

}
# 创建日志对象
access_logger = log.log("access")


# 查看账户信息
def account_info(access_data):
    pass


# 还款
def repay(access_data):
    pass


# 取款
def withdraw(access_data):
    pass


# 转账
def transfer(access_data):
    pass


# 查看账单
def paycheck(access_data):
    pass


# 退出
def logout(access_data):
    pass

# 用户交互
def interactive(access_data):
    msg = (
        """
        -------------ATM---------------
        \033[31;1m
        1.  账户信息
        2.  存款
        3.  取款
        4.  转账
        5.  账单
        6.  退出
        \033[0m"""
    )
    print(msg)
    menu_dic = {
        "1": account_info,
        "2": repay,
        "3": withdraw,
        "4": transfer,
        "5": paycheck,
        "6": logout
    }
    while True:
        choice = input("请选择功能菜单编号<<<:").strip()
        if choice in menu_dic:
            menu_dic[choice](access_data)
        else:
            print("\033[31;1m编号输入错误，请您重新输入!\033[0m")


def run():
    """
        程序启动
        :return:
    """
    # 用户认证
    login_account = auth.login_account(user_data, access_logger)
    if user_data["is_authenticated"]:  # 如果用户认证成功
        # 将用户登录信息赋给u用户数据信息ser_data
        user_data["account_data"] = login_account
        # 用户交互
        interactive(user_data)
