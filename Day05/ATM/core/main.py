# -------------------------------
# Task Name：主要业务逻辑交互模块
# Description ：
# Author ： Danny
# date： 2017/11/19
# -------------------------------
from prettytable import PrettyTable

from conf import settings
from core import log
from core import account
from core import auth
from core import transaction


# 用户数据信息

user_data = {
    'account_id': None,  # 帐号ID
    'is_authenticated': False,  # 是否认证
    'account_data': None  # 帐号数据

}
# 创建日志对象
access_logger = log.log("access")
transaction_logger = log.log("transaction")


def get_account_info(account_id):
    """
    输出用户信息
    :param account_id: 用户ID
    :return:
    """
    account_data = account.get_account(account_id)
    cur_balance = """
        -------------信用卡余额信息--------------
        信用额度:%s
        可用额度:%s
        -------------信用卡余额信息--------------
        """ % (account_data["credit"], account_data["balance"])
    print(cur_balance)
    return account_data


def account_info(user_data):
    """
    查看账户信息
    :param user_data:
    :return:
    """
    # 数据格式化输出
    title = ["用户名", "密码", "信用额度", "注册日期", "过期日期", "状态", "可用额度", "还款日期"]
    # x = PrettyTable(user_data["account_data"].keys())
    x = PrettyTable(title)
    x.align["用户名"] = "l"  # 以第一个字段左对齐
    x.padding_width = 4
    str_status = ("正常" if int(user_data["account_data"]["status"]) == 0 else "异常")
    user_data["account_data"]["status"] = str_status
    x.add_row(user_data["account_data"].values())
    print(x)


def repay(user_data):
    """
    还款
    :param user_data: 用户信息
    :return:
    """
    while True:
        account_data = get_account_info(user_data["account_id"])
        repay_amount = input("\033[31;1m请输入还款金额或者输入b退出:\033[0m").strip()
        if repay_amount == "b":
            break
        elif len(repay_amount) > 0 and repay_amount.isdigit():
            new_account_data = transaction.with_transaction(account_data, "repay", repay_amount, transaction_logger)
            print("\033[42;1m新的余额:%s\033[0m" % new_account_data["balance"])

        else:
            print("\033[31;1m输入错误，请您重新输入!\033[0m")




def withdraw(user_data):
    """
    取款
    :param user_data: 用户信息
    :return:
    """
    while True:
        account_data = get_account_info(user_data["account_id"])
        withdraw_amount = input("\033[31;1m请输入取款金额或者输入b退出:\033[0m").strip()
        if withdraw_amount == "b":
            break
        elif len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            if float(withdraw_amount) <= account_data["balance"]:
                new_account_data = transaction.with_transaction(account_data, "withdraw", withdraw_amount,
                                                                transaction_logger)
                print("\033[42;1m新的余额:%s\033[0m" % new_account_data["balance"])
            else:
                print("\033[31;1m余额不足，请您重新输入！\033[0m")

        else:
            print("\033[31;1m输入错误，请您重新输入!\033[0m")

def transfer(user_data):
    """
    转账
    :param user_data: 用户信息
    :return:
    """
    while True:
        account_data = get_account_info(user_data["account_id"])
        transfer_amount = input("\033[31;1m请输入转账金额或者输入b退出:\033[0m").strip()
        if transfer_amount == "b":
            break
        elif len(transfer_amount) > 0 and transfer_amount.isdigit():
            if float(transfer_amount) <= account_data["balance"]:
                new_account_data = transaction.with_transaction(account_data, "transfer", transfer_amount,
                                                                transaction_logger)
                print("\033[42;1m新的余额:%s\033[0m" % new_account_data["balance"])
            else:
                print("\033[31;1m余额不足，请您重新输入！\033[0m")

        else:
            print("\033[31;1m输入错误，请您重新输入!\033[0m")

def paylist(user_data):
    """
    查看账单
    :param user_data: 用户信息
    :return:
    """
    time = input("请输入查看日期（年-月-日）:")
    log_file = "%s/log/%s" % (settings.BASE_DIR, settings.LOG_File["transaction"])
    with open(log_file, "r", encoding="utf-8") as read_file:
        for line in read_file.readlines():
            if time == line[0:10]:
                print(line)
            elif time == line[0:7]:
                print(line)
            elif time == line[0:4]:
                print(line)


def logout(user_data):
    """
    退出系统
    :param user_data: 用户信息
    :return:
    """
    print("欢迎%s下次使用！" % user_data["account_id"])
    exit()


# 用户交互
def interactive(user_data):
    msg = (
        """
        -------------ATM---------------
        \033[31;1m
        1.  账户信息
        2.  还款(存款)
        3.  提现(取款)
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
        "5": paylist,
        "6": logout
    }
    while True:
        choice = input("请选择功能菜单编号<<<:").strip()
        if choice in menu_dic:
            menu_dic[choice](user_data)
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
        # 将用户登录信息赋给用户数据信息user_data
        user_data["account_data"] = login_account
        user_data["account_id"] = user_data["account_data"].get("id")
        # 用户交互
        interactive(user_data)
