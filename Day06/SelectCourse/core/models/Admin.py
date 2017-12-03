# -------------------------------
# Task Name：管理员类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from conf import settings

from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib.Common import Common


class Admin(BaseModel):
    db_path = DbHelper("admin").file_db_handle()

    def __init__(self, username, password):
        self.id = Common.create_uuid()
        self.username = username
        self.password = password

    @staticmethod
    def login():
        try:
            username = input('请输入用户名: ').strip()
            userpwd = input('请输入密码: ').strip()
            for obj in Admin.get_all_list():
                if obj.username == username and obj.password == userpwd:
                    status = True
                    error = ''
                    data = '\033[1;32;40m登录成功 !\033[0m'
                    break
            else:
                raise Exception('\033[1;31;40m用户名或密码错误!\033[0m')
        except Exception as e:
            status = False
            error = str(e)
            data = ''
        return {'status': status, 'error': error, 'data': data}
