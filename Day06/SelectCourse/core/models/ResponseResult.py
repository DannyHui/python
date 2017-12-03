# -------------------------------
# Task Name：响应结果消息类
# Description ：
# Author ： Danny
# date： 2017/12/3
# -------------------------------
class ResponseResult(object):
    def __init__(self, status, msg, data):
        self.status = status
        self.msg = msg
        self.data = data
