# -------------------------------
# Task Name：教师类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
import time
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib.Common import Common


class Teacher(BaseModel):
    db_path = DbHelper("teacher").file_db_handle()

    def __init__(self, name, level):
        self.id = Common.create_uuid()
        self.name = name
        self.level = level
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.__account = 0