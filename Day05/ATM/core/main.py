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
from core import product

# 用户数据信息
from Day05.ATM.core import shopping

user_data = {
    'account_id': None,  # 帐号ID
    'is_authenticated': False,  # 是否认证
    'account_data': None  # 帐号数据

}
# 创建日志对象
access_logger = log.log("access")
transaction_logger = log.log("transaction")


def show_account_info(account_id):
    """
     输出用户信用卡信息
     :param account_id: 用户ID
     :return:
     """
    account_data = account.get_account(account_id)
    cur_balance = """
           -------------信用卡信息--------------
           信用额度:%s
           可用额度:%s
           -------------信用卡信息--------------
           """ % (account_data["credit"], account_data["balance"])
    print(cur_balance)


def buyShop(user_data):
    buyProducts = []
    while True:
        # 显示商品列表
        productList = product.GetProductList()
        str_product = '''
        ---------------商品列表------------------
        '''
        print(str_product)
        # 格式化输出商品信息
        title = ["编号", "商品名称", "商品价格(元)"]
        x = PrettyTable(title)
        x.align["编号"] = "l"  # 以第一个字段左对齐
        x.padding_width = 2
        x.add_row(productList.values())
        print(x)
        code = input("请选择购买商品的编号| 退出(q)：").strip()
        if code.lower() == "q":
            # 显示购买记录
            shopping.ShowBuyList(buyProducts)
            break
        # 检查商品编号是否合法
        if not code.isdigit() or int(code) not in range(1, len(productList) + 1):
            print("商品编号输入不合法，请重新输入！")
            continue
        else:
            # 获取选择商品 名称 和价格
            product = product.GetProductInfo(int(code))
            productName = product[0]
            productPrice = product[1]
            userName = user_data["account_id"]
            # 获取用户信用卡可用额度
            account_data = account.get_account(userName)
            amount = account_data["balance"]
            # 判断余额是否足够
            if float(amount) < productPrice:
                print("您的信用卡余额不足，请选择其它商品！")
                continue
            else:
                # 保存消费记录
                shopping.SaveShoppingList(userName, productName, productPrice)
                # 修改用户信用卡信息
                new_balance = float(amount) - productPrice
                account_data = user_data["account_data"]
                account_data["balance"] = new_balance
                account.update_account(account_data)
                # 添加购买记录
                buyProducts.append(productName)

                # 是否继续购买
                while True:
                    isShop = input("是否继续购买(Y/N)| 退出(q)：").strip()
                    if isShop.lower() not in ['n', 'y', 'q']:
                        print("输入不合法，请重新输入！")
                        continue
                    else:
                        break
                if isShop.lower() == "y":
                    continue
                else:
                    # 显示购买记录
                    shopping.ShowBuyList(buyProducts)
                    break


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
        account_data = show_account_info(user_data["account_id"])
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
        account_data = show_account_info(user_data["account_id"])
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
        -------------欢迎来到个人业务平台---------------
        \033[31;1m
        1.  购物商城
        2.  账户信息
        3.  存款
        4.  取款
        5.  转账
        6.  账单
        7.  退出
        \033[0m"""
    )
    print(msg)
    menu_dic = {
        "1": buyshop,
        "2": account_info,
        "3": repay,
        "4": withdraw,
        "5": transfer,
        "6": paylist,
        "7": logout
    }
    while True:
        choice = input("请选择业务功能编号<<<:").strip()
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
