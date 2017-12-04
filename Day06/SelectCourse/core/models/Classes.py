# -------------------------------
# Task Name：班级类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib import Common


class Classes(BaseModel):
    db_path = DbHelper("school").file_db_handle()

    def __init__(self, name, school_id, course_teacher_list):
        self.id = Common.create_uuid()
        self.name = name
        self.school_id = school_id
        self.course_teacher_list = course_teacher_list
