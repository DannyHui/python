# -------------------------------
# Task Name：购物商城模块
# Description ：
# Author ： Danny
# date： 2017/11/21
# -------------------------------
import json

from core import db_handle
from conf import settings


def ShowBuyList(buyProducts):
    """
    显示购买记录
    :param buyProducts: 购买商品
    :return:
    """
    if len(buyProducts) == 0:
        print("您没有购买记录！")
    else:
        str_product = "您已购买的商品"
        print(str_product.center(30, '*'))
        for product in buyProducts:
            print("\033[32;1m{_product}\033[0m".format(_product=product))
# 保存用户消费记录
def SaveShoppingList(name, productName, price):
    shoplist_data=GetShoppingList()
    shoppingSheet = {'name': productName, 'price': price, 'buytime': time.strftime("%Y-%m-%d %H:%M:%S")}
    if name in shoplist_data:
        shoplist_data[name].append(shoppingSheet)
    else:
        shoplist_data[name] = [shoppingSheet]
    db_path = db_handle.handle(settings.DATABASE, "shoplist")
    shoplist_file = "%s\%s.json" % (db_path, "shoplists")
    with open(shoplist_file, "w", encoding="utf-8") as w_file:
        json.dump(shoplist_data, w_file)

def GetShoppingList():
    """
    获取用户消费记录
    :return:
    """
    db_path = db_handle.handle(settings.DATABASE, "shoplist")
    shoplist_file = "%s\%s.json" % (db_path, "shoplists")
    with open(shoplist_file, "r", encoding="utf-8") as r_file:
        shoplist_data = json.load(r_file)
    if shoplist_data == "":
        shoplist_data = {}
    return  shoplist_data
