# -------------------------------
# Task Name：购物车
# Description ：
# 1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
# 2、允许用户根据商品编号购买商品
# 3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
# 4、可随时退出，退出时，打印已购买商品和余额
# 5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
# 6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
# 7、允许查询之前的消费记录
# Author ： Danny
# date： 2017/11/2
# -------------------------------
# import json
# # 读取菜单文件的数据
# with open("test.json","r",encoding="utf-8") as f:
#     data = json.load(f)
# print(data)
import json

# 写入购物车用户数据
with open('users.json','w',encoding='utf-8') as f:
    data=[]
    for s in range(1 ,6):
        data1={'name':'test00'+str(s),'pwd':'123456','amount':1000,'balance':1000}
        data.append(data1)
    json.dump(data, f, ensure_ascii=False)

# 写入购物车用户数据
with open('products.json','w',encoding='utf-8') as f:
    data=[]
    for s in range(1 ,6):
        data1={'name':'test00'+str(s),'price':1000}
        data.append(data1)
    json.dump(data, f, ensure_ascii=False)

# data1 = {'name':'john',"age":12}
# data2 = {'name':'merry',"age":13}
# data = [data1,data2]
# print(data)
#
# file.close()
# file = open('test.json','r',encoding='utf-8')
# s = json.load(file)
# print (s[0]['name'])
