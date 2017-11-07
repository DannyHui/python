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
import json
# 用户信息文件
userFileName='users.json'
# 用户信息数组
users=[]
# 读取用户信息文件
def ReadUserFile():
    with open(userFileName, 'r', encoding='utf-8') as f:
        users = json.load(f)
# 写入用户信息文件
def WriteUserFile():
    with open(userFileName,'w',encoding='utf-8') as f1:
        json.dump(users, f1, ensure_ascii=False)
#添加用户信息
def InsertUser(name,pwd):
    ReadUserFile()
    userInfo = {'name': name, 'pwd': pwd, 'amount': 0}
    users.append(userInfo)
    WriteUserFile()
# 修改用户工资
def UpdateUserAmount(name,amount):
    ReadUserFile()
    for u_dict in users:
        if u_dict["name"] == name:
            u_dict["amount"] = amount
            WriteUserFile()
            break
# 检查用户是否存在
def IsExistUserName(name):
    ReadUserFile()
    isExist = False
    for u_dict in users:
        if u_dict["name"] == name:
            isExist = True
    return isExist
# 检查用户名和密码是否正确
def CheckUserNamePwd(name,pwd):
    ReadUserFile()
    isExist = False
    for u_dict in users:
        if u_dict["name"] == name and u_dict["pwd"] == pwd:
            isExist = True
    return isExist
while True:
    str_welcome = "欢迎进入购物系统"
    print(str_welcome.center(30,'*'))
    userName=input("请输入用户名：")
    userPwd=input("请输入密码：")
    if IsExistUserName(userName):
        while not CheckUserNamePwd(userName,userPwd):
            userPwd = input("请输入密码：")
        else:
            print("登录成功")
    else:
        InsertUser(userName,userPwd)
        while True:
            amount = input("请输入工资：")
            if not amount.isdigit():
                print("工资必须为数字,请重新输入！")
                continue
            else:
                print("合法")










