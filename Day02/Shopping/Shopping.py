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
productFileName='products.json'
# 读取用户信息文件
def ReadUserFile():
    with open(userFileName, 'r', encoding='utf-8') as f:
        users = json.load(f)
    return users
# 写入用户信息文件
def WriteUserFile(users):
    with open(userFileName,'w',encoding='utf-8') as f1:
        json.dump(users, f1, ensure_ascii=False)
#添加用户信息
def InsertUser(name,pwd):
    users=ReadUserFile()
    userInfo = {'name': name, 'pwd': pwd, 'amount': 0}
    users.append(userInfo)
    WriteUserFile(users)
# 修改用户工资
def UpdateUserAmount(name,amount):
    users = ReadUserFile()
    for u_dict in users:
        if u_dict["name"] == name:
            u_dict["amount"] = amount
            WriteUserFile(users)
            break
# 查询用户余额
def GetUserAmount(name):
    users = ReadUserFile()
    for u_dict in users:
        if u_dict["name"] == name:
            amount = u_dict["amount"]
            break
    return amount
# 检查用户是否存在
def IsExistUserName(name):
    users = ReadUserFile()
    isExist = False
    for u_dict in users:
        if u_dict["name"] == name:
            isExist = True
    return isExist
# 检查用户名和密码是否正确
def CheckUserNamePwd(name,pwd):
    users = ReadUserFile()
    isExist = False
    for u_dict in users:
        if u_dict["name"] == name and u_dict["pwd"] == pwd:
            isExist = True
    return isExist
# 获取用户消费记录

# 获取商品列表
def ReadProductFile():
    with open(productFileName, 'r', encoding='utf-8') as f2:
        products = json.load(f2)
    return products



while True:
    str_welcome = "欢迎进入购物系统"
    print(str_welcome.center(30,'*'))
    userName=input("请输入用户名：").strip()
    userPwd=input("请输入密码：")
    isLogin=False
    if IsExistUserName(userName):
        while not CheckUserNamePwd(userName,userPwd):
            print("密码错误，请重新输入！")
            userPwd = input("请输入密码：")
        else:
            isLogin=True
    else:
        InsertUser(userName,userPwd)
        while True:
            userAmount = input("请输入工资：")
            if not userAmount.isdigit():
                print("工资必须为数字,请重新输入！")
                continue
            else:
                UpdateUserAmount(userName,userAmount)
                isLogin = True
                break
    if isLogin:
        amount = GetUserAmount(userName)
        print("您的账户余额：\033[31;1m{_amount}\033[0m".format(_amount=amount))
        # 是否显示消费记录
        isShow=input("是否显示消费记录(Y/N)：").strip()
        if isShow=="Y":
            # 显示消费记录
            print("显示消费记录")
        else:
            # 显示商品列表
            str_product = "商品列表"
            print(str_product.center(40, '*'))
            print('%-5s %-15s %-10s' % ('编号', '商品名称', '商品价格(元)'))
            products = ReadProductFile()
            for index, item in enumerate(products):
                print('%-8d %-20s %-10d' % (index + 1, item['name'], item['price']))












