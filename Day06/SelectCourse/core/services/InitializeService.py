# -------------------------------
# Task Name：初始化服务类
# Description ：
# Author ： Danny
# date： 2017/12/3
# -------------------------------
from core.models.Admin import Admin

class InitializeService(object):
    def initialize(self):
        try:
            user = input('请输入初始化用户名：')
            pwd = input('请输入初始化密码：')
            obj = Admin(user, pwd)
            obj.save()
            return True
        except Exception as e:
            print(e)

    def main(self):
        show = """
            1. 初始化管理员
        """
        choice_dict = {
            '1': self.initialize
        }
        while True:
            print(show)
            choice = input('请选择操作项<<<:').strip()
            if choice in choice_dict:
                if choice_dict[choice]():
                    print('操作成功'.center(60, '-'))
                    break
                else:
                    print("\033[1;31;40m操作异常，请重新操作!\033[0m")
            else:
                print("\033[1;31;40m选项错误，请重新输入!\033[0m")