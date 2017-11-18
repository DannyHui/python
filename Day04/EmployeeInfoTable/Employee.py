# -------------------------------
# Task Name：
# 员工信息表程序，实现增删改查操作：
# select * from staff where age > 37
# 可进行模糊查询，语法至少支持下面3种:
# 　　select name,age from staff where age > 22
# 　　select  * from staff where dept = "IT"
#     select  * from staff where enroll_date like "2013"
# 查到的信息，打印后，最后面还要显示查到的条数
# 可创建新员工纪录，以phone做唯一键，staff_id需自增
# 可删除指定员工信息纪录，输入员工id，即可删除
# 可修改员工信息，语法如下:
# 　　update staff set dept="Market" where dept = "IT"
# Description ：
# Author ： Danny
# date： 2017/11/15
# -------------------------------

from prettytable import PrettyTable
import os


# sql 解析
def SqlParse(sql):
    parse_commond = {
        "insert": InsertParse,
        "delete": DeleteParse,
        "update": UpdateParse,
        "select": SelectParse
    }
    sql_list = sql.split(' ')
    sql_commond = sql_list[0]
    sql_dict = ''
    if sql_commond in parse_commond:
        sql_dict = parse_commond[sql_commond](sql_list)
    return sql_dict


# 检查输入sql格式是否合法
def checkSqlFormat(sql_dict):
    ischeck = True
    cols = ["id", "name", "age", "phone", "dept", "enroll_date"]
    if sql_dict["commond"].__name__ == "Insert":
        if len(sql_dict["into"]) > 0 and sql_dict["into"][0] != "staff":
            ischeck = False
        if ischeck and len(sql_dict["values"][0].split(',')) != 5:
            ischeck = False
    elif sql_dict["commond"].__name__ == "Delete":
        if len(sql_dict["from"]) > 0 and sql_dict["from"][0] != "staff":
            ischeck = False
        if ischeck and len(sql_dict["where"]) > 0:
            ischeck = CheckSqlWhere(sql_dict["where"])
    elif sql_dict["commond"].__name__ == "Update":
        if len(sql_dict["update"]) > 0 and sql_dict["update"][0] != "staff":
            ischeck = False
        if ischeck and len(sql_dict.get("set")) > 0:
            for item in sql_dict.get("set"):
                if list(item.keys())[0] not in cols:
                    ischeck = False
                    break
        if ischeck and len(sql_dict["where"]) > 0:
            ischeck = CheckSqlWhere(sql_dict["where"])
    elif sql_dict["commond"].__name__ == "Select":
        if len(sql_dict["from"]) > 0 and sql_dict["from"][0] != "staff":
            ischeck = False
        if ischeck and len(sql_dict["select"]) > 0:
            if sql_dict["select"][0] != '*':
                for field in sql_dict["select"][0].split(','):
                    if field not in cols:
                        ischeck = False
                        break
        if ischeck and len(sql_dict["where"]) > 0:
            ischeck = CheckSqlWhere(sql_dict["where"])
        if ischeck and len(sql_dict["limit"]) > 0:
            if not str(sql_dict["limit"][0]).isdigit():
                ischeck = False
    return ischeck


# where条件 格式校验
def CheckSqlWhere(sql_where):
    ischeck = True
    logic_opt = ["or", "and"]
    for wh in sql_where:
        if wh not in logic_opt:
            if type(wh) is not list:
                ischeck = False
                break
            else:
                if len(wh) != 3:
                    ischeck = False
                    break
    return ischeck


# 添加语句解析 Insert
def InsertParse(sql_list):
    sql_dict = {
        "commond": Insert,  # 操作命令
        "into": [],  # 表名
        "values": [],  # 插入的值
    }
    sql_dict = CommondParse(sql_dict, sql_list)
    return sql_dict


# 删除语句解析 Delete
def DeleteParse(sql_list):
    sql_dict = {
        "commond": Delete,  # 操作命令
        "from": [],  # 表名
        "where": [],  # 过滤条件
    }
    sql_dict = CommondParse(sql_dict, sql_list)
    return sql_dict


# 更新语句解析 Update
def UpdateParse(sql_list):
    sql_dict = {
        "commond": Update,  # 操作命令
        "update": [],  # 表名
        "set": [],  # 赋值语句
        "where": []  # 过滤条件
    }
    sql_dict = CommondParse(sql_dict, sql_list)
    return sql_dict


# 查询语句解析Select
def SelectParse(sql_list):
    sql_dict = {
        "commond": Select,  # 操作命令
        "select": [],  # 字段
        "from": [],  # 表名
        "where": [],  # 过滤条件
        "limit": []  # 记录数
    }
    sql_dict = CommondParse(sql_dict, sql_list)
    return sql_dict


# 命令解析
def CommondParse(sql_dict, sql_list):
    item_key = ''
    set_value = ''
    for item in sql_list:
        if item in sql_dict:
            item_key = item
        else:
            if len(item_key) > 0:
                if item_key == "set":
                    set_value += item
                else:
                    sql_dict[item_key].append(item)
    if "where" in sql_dict:
        sql_dict["where"] = WhereParse(sql_dict["where"])
    if "set" in sql_dict:
        sql_dict["set"] = SetParse(set_value)
    return sql_dict


# where 解析
def WhereParse(sql_where):
    operators = ["and", "or"]
    where_array = []
    str_where = []
    for item in sql_where:
        if len(item) == 0: continue
        if item in operators:
            where_array.append(str_where)
            where_array.append(item)
            str_where = []
        else:
            str_where.append(item)
    else:
        if len(str_where) > 0:
            where_array.append(str_where)
    return where_array


# set 解析
def SetParse(set_value):
    set_values = set_value.split(',')
    set_arr = []
    for item in set_values:
        item_key, item_value = item.split('=')
        set_dict = {}
        set_dict[item_key] = item_value
        set_arr.append(set_dict)
    return set_arr


# sql 操作命令分配
def sql_Execute(sql_dict):
    data = sql_dict.get("commond")(sql_dict)
    return data


# 增加操作
def Insert(sql_dict):
    # 返回数据
    data_arr = [0]
    # 自增长id
    id = 0
    # 手机号是否存在
    phone_exist = False
    phone = sql_dict.get("values")[0].split(',')[2]
    with open(str.format("{tbname}.txt", tbname=sql_dict.get("into")[0]), 'ab+') as f:
        f.seek(0, 0)
        lines = f.readlines()
        for line in lines:
            line = line.decode(encoding='utf-8')
            if phone == line.split(',')[3]:
                phone_exist = True
                break
        if not phone_exist:
            if len(lines) >= 1:
                line = lines[-1].decode(encoding='utf-8')
                new_id = int(line.split(',')[0]) + 1
            f.write(bytes("%s,%s\n" % (str(new_id), sql_dict.get("values")[0]), encoding='utf-8'))
    if phone_exist:
        data_arr[0] = 0
        data_arr.append("手机号已经存在！")
    else:
        data_arr[0] = 1
    return data_arr


# 删除操作
def Delete(sql_dict):
    # 标题
    title = "id,name,age,phone,dept,enroll_date"
    # 获得数据
    data_arr = [1]
    # 未满足删除条件的数据
    not_del_data = []
    # 数据总记录数
    total = 0
    if len(sql_dict.get("where")) > 0:
        tablename = sql_dict.get("from")[0]
        old_filename = str.format("{tbname}.txt", tbname=tablename)
        new_filename = str.format("{tbname}_new.txt", tbname=tablename)
        with open(old_filename, 'r', encoding="utf-8") as r_file, \
                open(new_filename, 'w', encoding="utf-8") as w_file:
            for line in r_file:
                total += 1
                data_dict = dict(zip(title.split(','), line.strip().split(',')))
                if not where_action(data_dict, sql_dict.get("where")):
                    not_del_data.append(line)
            if len(not_del_data) < total:
                for item in not_del_data:
                    w_file.write(item)
        # 删除原文件
        os.remove(old_filename)
        # 重命名新文件
        os.rename(new_filename, old_filename)
    print("删除%d条数据!" % (total - len(not_del_data)))
    return data_arr


# 修改操作
def Update(sql_dict):
    # 标题
    title = "id,name,age,phone,dept,enroll_date"
    # 返回数据
    data_return = [1]
    # 记录数据
    data_arr = []
    # 修改记录数
    updateRecord = 0
    tablename = sql_dict.get("update")[0]
    old_filename = str.format("{tbname}.txt", tbname=tablename)
    new_filename = str.format("{tbname}_new.txt", tbname=tablename)
    with open(old_filename, 'r', encoding="utf-8") as r_file, \
            open(new_filename, 'w', encoding="utf-8") as w_file:
        for line in r_file:
            data_dict = dict(zip(title.split(','), line.strip().split(',')))
            # where 条件过滤
            if where_action(data_dict, sql_dict.get("where")):
                updateRecord += 1
                # 修改数据
                for item in sql_dict.get("set"):
                    data_dict[list(item.keys())[0]] = list(item.values())[0]
            data_arr.append(','.join(list(data_dict.values())) + "\n")
        for item in data_arr:
            w_file.write(item)
    # 删除原文件
    os.remove(old_filename)
    # 重命名新文件
    os.rename(new_filename, old_filename)
    print("修改%d条数据!" % (updateRecord))
    return data_return


# 查询操作
def Select(sql_dict):
    # 标题
    title = "id,name,age,phone,dept,enroll_date"
    # 获得数据
    data_arr = []
    with open(str.format("{tbname}.txt", tbname=sql_dict.get("from")[0]), 'r', encoding="utf-8") as f:
        for line in f:
            data_dict = dict(zip(title.split(','), line.strip().split(',')))
            # where 条件过滤
            if where_action(data_dict, sql_dict.get("where")):
                # field 字段筛选
                fields_key = str(sql_dict.get("select")[0])
                fields_value = []
                if fields_key != "*":
                    fields_key = fields_key.split(',')
                    for key in fields_key:
                        fields_value.append(data_dict[key])
                    data_dict = dict(zip(fields_key, fields_value))
                # 保存符合条件的数据
                data_arr.append(data_dict)
    # limit 获取指定记录数
    if len(sql_dict.get("limit")) != 0:
        data_arr = data_arr[0:int(sql_dict.get("limit")[0])]
    return data_arr


# where 过滤条件
def where_action(data_dict, sql_where):
    if len(sql_where) == 0:
        return True
    exp_result = []
    for exp in sql_where:
        if type(exp) is list:
            exp_key, exp_opt, exp_value = exp
            if exp_opt == "=":
                exp_opt = "=="
            if data_dict[exp_key].isdigit():
                exp_value = int(exp_value)
                dict_value = int(data_dict[exp_key])
            else:
                dict_value = "'%s'" % data_dict[exp_key]
            if exp_opt != 'like':
                exp_result.append(str(eval("%s%s%s" % (dict_value, exp_opt, exp_value))))
            else:
                exp_result.append(str(exp_value in dict_value))
        else:
            exp_result.append(exp)
    return eval(' '.join(exp_result))


if __name__ == "__main__":
    while True:
        welcome_str = '''
                                              欢迎来到员工信息查询程序
        ------------------------------------------------------------------------------------------------------
        注意事项：
        1、命令区分大小写；
        2、中间一个空格隔开；
        3、表名称：staff，列名称：id,name,age,phone,dept,enroll_date；
        操作语法：
        添加：insert into 表名称 values 值1, 值2,....
        删除：delete from 表名称 where 列名称 = 某值
        修改：update 表名称 set 列名称 = 新值 where 列名称 = 某值
        查询：select * from 表名称 where 列名称 = 某值
              select * from 表名称 where 列名称 like 某值
              select 列名称1,列名称2... from 表名称 where 列名称 = 某值
        ------------------------------------------------------------------------------------------------------
            '''
        print(welcome_str)
        input_sql = input('请输入SQL语句(或者输入q退出)：\nSQL>').strip()
        if input_sql.lower() == 'q':
            print('感谢使用模拟SQL程序，欢迎再次使用，再见！')
            exit()
        else:
            if len(input_sql) == 0:
                continue
        # sql解析
        sql_dict = SqlParse(input_sql)
        if len(sql_dict) == 0 or checkSqlFormat(sql_dict) == False:
            print("SQL输入格式错误，请重新输入！")
            continue
        # sql执行
        data_arr = sql_Execute(sql_dict)
        if (len(data_arr) > 0):
            if type(data_arr[0]) is dict:
                # 数据格式化输出
                x = PrettyTable(data_arr[0].keys())
                x.align[list(data_arr[0].keys())[0]] = "l"  # 以第一个字段左对齐
                x.padding_width = 1
                for data in data_arr:
                    x.add_row(data.values())
                print("总记录数：%d" % len(data_arr))
                print(x)
            elif int(data_arr[0]) == 1:
                print("执行成功！")
            else:
                print("执行失败！")
                print(data_arr[1])
            continue
        else:
            print("无执行记录！")
