# -------------------------------
# Task Name：学生类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
import time
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib.Common import Common


class Student(BaseModel):
    db_path = DbHelper("student").file_db_handle()

    def __init__(self, name, age, sex,classes_id):
        self.id = Common.create_uuid()
        self.name = name
        self.sex = sex
        self.age = age
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.classes_id = classes_id
