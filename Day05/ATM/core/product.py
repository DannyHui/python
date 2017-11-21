# -------------------------------
# Task Name：商品模块
# Description ：
# Author ： Danny
# date： 2017/11/21
# -------------------------------
import json
from conf import settings
from core import db_handle

def GetProductList():
    """
    获取商品列表
    :return: 商品信息
    """
    db_path = db_handle.handle(settings.DATABASE, "product")
    product_file = "%s\%s.json" % (db_path, "products")
    with open(product_file, "r", encoding="utf-8") as r_file:
        product_data = json.load(r_file)
    return product_data

def GetProductInfo(id):
    """
    获取商品名称和价格
    :param products: 商品信息列表
    :param id: 商品ID
    :return:
    """
    products = GetProductList()
    for item in products:
        if item["id"] == id:
            return (item["name"], item["price"])


