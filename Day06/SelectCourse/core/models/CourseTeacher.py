# -------------------------------
# Task Name：课程老师关系类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib.Common import Common


class CourseTeacher(BaseModel):
    db_path = DbHelper("course_teacher").file_db_handle()

    def __init__(self, course_id, teacher_id):
        self.id = Common.create_uuid()
        self.course_id = course_id
        self.teacher_id = teacher_id
