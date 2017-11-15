# -------------------------------
# Task Name：
# Description ：
# Author ： Danny
# date： 2017/11/2
# -------------------------------

import json

# 写入购物车用户数据
with open('users.json','w',encoding='utf-8') as f:
    for s in range(1 ,6):
        data1={'name':'test00'+str(s),'pwd':'123456','amount':1000,'balance':1000}
        data.append(data1)
    json.dump(data, f, ensure_ascii=False)
with open('users.json','r',encoding='utf-8') as f1:
    data=json.load(f1)
    print(data)

# 写入购物车用户数据
with open('products.json','w',encoding='utf-8') as f:
    for s in range(1 ,6):
        data1={'name':'test00'+str(s),'price':1000}
        data.append(data1)
    json.dump(data, f, ensure_ascii=False)
with open('products.json','r',encoding='utf-8') as f1:
    data=json.load(f1)
    print(data)