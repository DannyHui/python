# -------------------------------
# Task Name：
# 员工信息表程序，实现增删改查操作：
#
# 可进行模糊查询，语法至少支持下面3种:
# 　　select name,age from staff_table where age > 22
# 　　select  * from staff_table where dept = "IT"
#     select  * from staff_table where enroll_date like "2013"
# 查到的信息，打印后，最后面还要显示查到的条数
# 可创建新员工纪录，以phone做唯一键，staff_id需自增
# 可删除指定员工信息纪录，输入员工id，即可删除
# 可修改员工信息，语法如下:
# 　　UPDATE staff_table SET dept="Market" where dept = "IT"
# Description ：
# Author ： Danny
# date： 2017/11/15
# -------------------------------
# sql 解析
def SqlParse(sql):
    parse_commond = {
        "insert": InsertParse,
        "delete": DeleteParse,
        "update": UpdateParse,
        "select": SelectParse
    }
    sql_split = sql.split(' ')
    sql_commond = sql_split[0]
    sql_dict = ''
    if sql_commond in parse_commond:
        sql_dict = parse_commond[sql_commond](sql_split)
    else:
        print("输入错误，请重新输入！")
    return sql_dict


def InsertParse(sql):
    pass


def DeleteParse(sql):
    pass


def UpdateParse(sql):
    pass


def SelectParse(sql_spl):
    sql_dict = {
        "commond": select,  # 命令
        "select": [],  # 字段
        "from": [],  # 表名
        "where": [],  # 过滤条件
        "limit": []  # 记录数
    }
    sql_dic = CommondParse(sql_dict, sql_spl)
    return sql_dic


# select * from staff_table where enroll_date like "2013"
def CommondParse(sql_dict, sql_spl):
    # 设置标志位
    tag = False
    str_char = ''
    item_key = ''
    for spl in sql_spl:
        if tag and spl in sql_dict:
            sql_dict[item_key]=str_char
            tag=False
            # sql_dict[item_key] = str_char
            # item_key = spl
            # tag = True
            # str_char = ''
            # continue
         if not tag and spl in sql_dict:
                item_key = spl
                tag = True
                continue
         if tag:
                str_char += spl
    else:
        sql_dict[item_key] = str_char
    return sql_dict


# sql 执行
def sql_Execute(sql_dic):
    pass


def Insert(sql_dic):
    pass


def Delete(sql_dic):
    pass


def Update(sql_dic):
    pass


def Select(sql_dic):
    pass


if __name__ == "__main__":
    while True:
        welcome_str = '''
                                              欢迎来到员工信息查询程序
        ------------------------------------------------------------------------------------------------------
        操作语法说明：
        添加：INSERT INTO 表名称 VALUES 值1, 值2,....
        删除：DELETE —> 输入欲删除的条目编号
        修改：UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
        查询：SELECT * FROM 表名称 WHERE 列名称 = 某值
              SELECT * FROM 表名称 WHERE 列名称 LIKE 某值
              SELECT 列名称1,列名称2... FROM 表名称 WHERE 列名称 = 某值
        ------------------------------------------------------------------------------------------------------
            '''
        print(welcome_str)
        input_sql = input('请输入SQL语句(或者输入q退出)：\nSQL>').strip()
        if input_sql.lower() == 'q':
            print('感谢使用模拟SQL程序，欢迎再次使用！再见！')
            exit()
        else:
            if len(input_sql) == 0:
                continue
        # sql解析
        sql_dict = SqlParse(input_sql)
        print(sql_dict)
        # if len(sql_dict)==0: continue


        # sql执行

        # res = sql_Execute(sql_dict)
