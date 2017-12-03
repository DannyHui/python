# -------------------------------
# Task Name：课程老师关系类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib import Common


class CourseTeacher(BaseModel):
    db_path = DbHelper("school").file_db_handle()

    def __init__(self, course_id, teacher_id):
        self.id = Common.create_uuid()
        self.course_id = course_id
        self.teacher_id = teacher_id
    def get_course_teacher_list(self):
        course_teacher_list = self.get_all_list()
        if course_teacher_list:
            return