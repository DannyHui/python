# -------------------------------
# Task Name：学生类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib import Common


class Student(BaseModel):
    db_path = DbHelper("student").file_db_handle()

    def __init__(self, name, age,classes_id):
        self.id = Common.create_uuid()
        self.name = name
        self.age = age
        self.classes_id = classes_id
