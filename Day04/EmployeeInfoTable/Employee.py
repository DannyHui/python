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
    parse_commond={
        "insert":InsertParse,
        "delete":DeleteParse,
        "update":UpdateParse,
        "select":SelectParse
    }
    sql_spl=sql.split(' ')
    sql_commond=sql_spl[0]
    sql_dict=''
    if sql_commond in parse_commond:
        sql_dict=parse_commond[sql_commond](sql_spl)
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
    sql_dict={
        "commond":Select,
        "select":[],
        "from":[],
        "where":[],
        "limit":[]
    }
    sql_dic = CommondParse(sql_dict,sql_spl)
    return sql_dic

def CommondParse(sql_dict,sql_spl):
    pass
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

if __name__=="__main__":
    while True:
        sql=input("sql>").strip()
        if sql=="exit": break
        if len(sql)==0: continue
        # sql解析
        sql_dict=SqlParse(sql)
        if len(sql_dict)==0: continue


        # sql执行

        # res = sql_Execute(sql_dict)


