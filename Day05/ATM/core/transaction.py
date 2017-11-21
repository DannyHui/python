# -------------------------------
# Task Name：交易模块
# Description ：
# Author ： Danny
# date： 2017/11/20
# -------------------------------
from conf import settings

from core import account


def with_transaction(account_data, transcation_type, amount, log_obj):
    """
    处理用户的交易
    :param account_data:用户的帐户信息(dict)
    :param transaction_type:用户交易类型
    :param amount:交易金额
    :return:用户交易后的帐户信息
    """
    amount = float(amount)
    if transcation_type in settings.TRANSACTION_TYPE:
        # 利息计算
        interest = amount * settings.TRANSACTION_TYPE[transcation_type]["interest"]
        # 账户余额
        balance = account_data["balance"]
        # 用户的帐户入账（plus）
        if settings.TRANSACTION_TYPE[transcation_type]["action"] == "plus":
            new_balance = balance + amount + interest
            log_obj.info("您的账户入账%s元,您的账户新的余额是%s元" % (amount, new_balance))
        # 用户的账户出账(minus)
        elif settings.TRANSACTION_TYPE[transcation_type]["action"] == "minus":
            new_balance = balance - amount - interest
            log_obj.info("您的账户出账%s元,您的账户新的余额是%s元" % (amount, new_balance))
            if new_balance < 0:
                new_balance = balance
                print("您的信用额度[%s]不能支付交易金额[-%s], 您当前的余额[%s]" \
                      % (account_data["credit"], (amount + interest), balace))
        account_data["balance"] = new_balance
        # 更新用户信息
        account.update_account(account_data)
        return account_data
    else:
        print("交易类型不存在!")
