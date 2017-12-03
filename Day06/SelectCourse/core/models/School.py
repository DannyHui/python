# -------------------------------
# Task Name：学校类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
import time
from core.db.DbHelper import DbHelper
from core.models.BaseModel import BaseModel
from lib.Common import Common


class School(BaseModel):
    db_path = DbHelper("school").file_db_handle()

    def __init__(self, name, address):
        self.id = Common.create_uuid()
        self.name = name
        self.address = address
        self.create_time = time.strftime('%Y-%m-%d %X')
        self.__income = 0
