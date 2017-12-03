# -------------------------------
# Task Name：公用类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
import hashlib
import uuid
import time

class Common(object):

    @classmethod
    def create_uuid(self):
        """
        创建UUID
        :return:
        """
        return str(uuid.uuid1())

    @classmethod
    def create_md5(self):
        """
        创建MD5
        :return:
        """
        m = hashlib.md5()
        m.update(bytes(str(time.time), encoding="utf-8"))
        return m.hexdigest()

