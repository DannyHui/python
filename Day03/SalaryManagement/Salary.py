# -------------------------------
# Task Name：作业三：工资管理系统
# Description ：
# 1、查询员工工资
# 2、修改员工工资
# 3、增加新员工记录
# 4、退出
# Author ： Danny
# date： 2017/11/5
# -------------------------------
import json
# 用户提示信息
msg = '''
1. 查询员工工资
2. 修改员工工资
3. 增加新员工记录
4. 退出
'''
# 员工信息存储文件
filename = 'info.txt'

# 员工信息数据
info_dict={}

# 读取用户信息
def InitUserInfo():
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith('\n'):
                line=line.strip()
                info_dict[line.split(' ')[0]]=line.split(' ')[1]
# 检查用户是否存在
def IsExistUser(name):
    isExist=False
    if name in info_dict:
        isExist = True
    return  isExist
# 获取用户工资
def GetUserSalary(name):
    return info_dict.get(name)
# 检查用户输入是否合法
def CheckUserInput(user_info):
    isCheck=True
    if len(user_info.split(' ')) != 2:
        isCheck = False
        print("格式输入错误，请重新输入！")
    else:
        name = user_info.split(' ')[0]
        salary = user_info.split(' ')[1]
        if not salary.isdigit():
            isCheck = False
            print("工资必须为数字，请重新输入！")
    return  isCheck

users=[]
# 读取用户信息文件
def ReadUserFile():
    with open('users.json', 'r', encoding='utf-8') as f:
        users = json.load(f)
# 写入用户信息文件
# 工资管理程序
while True:
    # 打印用户提示信息
    print(msg);
    action=input("\033[31;1m请输入操作选项>>：\033[0m")
    if action.isdigit():
        # 获取用户信息
        InitUserInfo()
        print(info_dict)
        ReadUserFile()
        print(users)
        if int(action) == 1:
            while True:
                name = input("请输入要查询的员工姓名（例如：Alex）:")
                # 判断用户是否存在
                isExist = IsExistUser(name)
                if isExist:
                    # 获取用户工资
                    salary=GetUserSalary(name)
                    print("{_name}的工资是：{_salary}".format(_name=name, _salary=salary))
                    break
                else:
                    print("员工不存在，请重新输入！")
                    continue
        elif int(action) == 2:
            while True:
                uinfo = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）:").strip()
                if CheckUserInput(uinfo):
                    name = uinfo.split(' ')[0]
                    if not IsExistUser(name):
                        print("员工不存在，请重新输入！")
                        continue
                    # 读文件
                    with open(filename, 'r', encoding='utf-8') as f1:
                        lines = f1.readlines()
                    # 写文件
                    with open(filename, 'w', encoding='utf-8') as f2:
                        for line in lines:
                            _name = line.split(' ')[0]
                            if _name == name:
                                line = uinfo + "\n"
                            f2.write(line)
                    print("修改成功！")
                    break
                else:
                    continue
        elif int(action) == 3:
            while True:
                uinfo = input("请输入要增加的员工姓名和工资，用空格分割（例如：Eric 100000）:").strip()
                if CheckUserInput(uinfo):
                    name = uinfo.split(' ')[0]
                    if IsExistUser(name):
                        print("员工已存在，请重新输入！")
                        continue
                    with open(filename, 'a', encoding='utf-8') as f3:
                        f3.write("\n" + uinfo)
                    print("增加成功！")
                    break
                else:
                    continue
        elif int(action) == 4:
            exit("再见！")
        else:
            print("输入错误，请重新输入！")
            continue
    else:
        print("输入错误，请重新输入！")
        continue