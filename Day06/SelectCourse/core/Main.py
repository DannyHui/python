# -------------------------------
# Task Name：主要业务逻辑交互模块
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from core.services.InitializeService import InitializeService
from core.services.AdminService import AdminService
from core.services.TeacherService import TeacherService
from core.services.StudentService import StudentService


class Main(object):
    def __init__(self):
        pass

    def interactive(self):
        """
        用户交互
        :return:
        """
        msg = (
            """
            -------------欢迎来到选课平台---------------
            \033[31;1m
            1.  初始化
            2.  管理员
            3.  老师
            4.  学生
            \033[0m"""
        )
        role_dic = {
            "1": InitializeService().main,
            "2": AdminService().login,
            "3": TeacherService().login,
            "4": StudentService().login
        }
        while True:
            print(msg)
            choice = input("请选择角色编号<<<:").strip()
            if choice in role_dic:
                role_dic[choice]()
            else:
                print("\033[1;31;40m选项错误，请重新输入!\033[0m")

    def run(self):
        """
        启动项
        :return:
        """
        self.interactive()
