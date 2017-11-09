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
import time

# 用户信息文件
userFileName='users.json'
productFileName='products.json'
shoppingFileName='shoppingSheets.json'
# 读取文件
def ReadFile(fileName):
    with open(fileName, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data
# 写入文件
def WriteFile(fileName,data):
    with open(fileName,'w',encoding='utf-8') as f1:
        json.dump(data, f1, ensure_ascii=False)
#添加用户信息
def InsertUser(name,pwd):
    users=ReadFile(userFileName)
    userInfo = {'name': name, 'pwd': pwd, 'amount': 0}
    users.append(userInfo)
    WriteFile(userFileName, users)
# 修改用户工资
def UpdateUserAmount(name,amount):
    users = ReadFile(userFileName)
    for u_dict in users:
        if u_dict["name"] == name:
            u_dict["amount"] = amount
            WriteFile(userFileName, users)
            break
# 查询用户余额
def GetUserAmount(name):
    users = ReadFile(userFileName)
    for u_dict in users:
        if u_dict["name"] == name:
            amount = u_dict["amount"]
            break
    return amount
# 检查用户是否存在
def IsExistUserName(name):
    users = ReadFile(userFileName)
    isExist = False
    for u_dict in users:
        if u_dict["name"] == name:
            isExist = True
    return isExist
# 检查用户名和密码是否正确
def CheckUserNamePwd(name,pwd):
    users = ReadFile(userFileName)
    isExist = False
    for u_dict in users:
        if u_dict["name"] == name and u_dict["pwd"] == pwd:
            isExist = True
    return isExist
# 获取用户消费记录
def GetUserShoppingSheet(name):
    shoppingSheets=ReadFile(shoppingFileName)
    str_sheet = "消费记录清单"
    print(str_sheet.center(40, '*'))
    if name in shoppingSheets:
        sheets = shoppingSheets[name]
        print('%-5s %-15s %-10s %-10s' % ('序号', '商品名称', '商品价格(元)','购买时间'))
        for index, item in enumerate(sheets):
            print('%-8d %-20s %-10d %-10s' % (index + 1, item['name'], item['price'],item['buytime']))
    else:
        print("您没有任何消费记录！")
# 保存用户消费记录
def SaveUserShoppingSheet(name,productName,price):
    sheets = ReadFile(shoppingFileName)
    shoppingSheet = {'name': productName, 'price': price, 'buytime': time.strftime("%Y-%m-%d %H:%M:%S")}
    if name in sheets:
        sheets[name].append(shoppingSheet)
    else:
        sheets[name]=[shoppingSheet]
    WriteFile(shoppingFileName,sheets)

# 获取商品列表
def GetProductList():
    products = ReadFile(productFileName)
    str_product = "商品列表"
    print(str_product.center(40, '*'))
    print('%-5s %-15s %-10s' % ('编号', '商品名称', '商品价格(元)'))
    for index, item in enumerate(products):
        print('%-8d %-20s %-10d' % (index + 1, item['name'], item['price']))
    return products

# 获取商品名称和价格
def GetProductInfo(products,code):
    for index,item in enumerate(products):
        if index+1==code:
            return (item["name"],item["price"])

# 检查商品编号是否合法
def CheckProductCode(products,code):
    isCheck=False
    if code.isdigit():
        if int(code)<=products.count() and int(code)>0:
            isCheck=True
    return  isCheck

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
    isShow=input("是否显示消费记录(Y/N)| 退出(q)：").strip()
    if isShow.lower()=="q":
        # 显示购买记录
        GetUserShoppingSheet(userName)
    else:
        if isShow.lower()=="y":
            # 显示消费记录
            GetUserShoppingSheet(userName)
        while True:
            # 显示商品列表
            productList = GetProductList()
            code = input("请选择购买商品的编号| 退出(q)：").strip()
            if code.lower() == "q":
                GetUserShoppingSheet(userName)
                break
            # 检查商品编号是否合法
            if not CheckProductCode(productList,code):
                print("商品编号输入不合法，请重新输入！")
                continue
            else:
                # 获取选择商品 名称 和价格
                product=GetProductInfo(productList,code)
                productName=product[0]
                productPrice=product[1]
                # 判断余额是否足够
                if amount<productPrice:
                    print("您的余额不足，请选择其它商品！")
                    continue
                else:
                    # 保存购买记录
                    SaveUserShoppingSheet(userName,productName,productPrice)
                    # 修改用户余额
                    UpdateUserAmount(userName,amount-productPrice)
                    isShop=input("您已购买成功，是否继续购买(Y/N)| 退出(q)：").strip()
                    if isShop.lower()=="y":
                        continue
                    else:
                        GetUserShoppingSheet(userName)
                        break
     exit("欢迎下次光临！")
