# -------------------------------
# Task Name：课程类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------

from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib.Common import Common


class Course(BaseModel):
    db_path = DbHelper("course").file_db_handle()

    def __init__(self, name, price, period, school_id):
        self.id = Common.create_uuid()
        self.name = name
        self.price = price
        self.period = period
        self.school_id = school_id
        self.__account = 0
