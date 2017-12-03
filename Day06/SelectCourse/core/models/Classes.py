# -------------------------------
# Task Name：班级类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib import Common


class School(BaseModel):
    db_path = DbHelper("school").file_db_handle()

    def __init__(self, name, fee, school_id):
        self.id = Common.create_uuid()
        self.name = name
        self.fee = fee
        self.school_id = school_id
