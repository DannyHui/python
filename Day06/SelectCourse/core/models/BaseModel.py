# -------------------------------
# Task Name：model基类
# Description ：
# Author ： Danny
# date： 2017/12/2
# -------------------------------
import os
import pickle


class BaseModel(object):
    def save(self):
        """
        保存对象
        :return:
        """
        file_path = os.path.join(self.db_path, self.id)
        pickle.dump(self, open(file_path, 'wb'))

    @classmethod
    def get_all_list(cls):
        """
        获取所有的对象集合
        :return:
        """
        obj_list = []
        for filename in os.listdir(cls.db_path):
            if filename.strip() != '__init__.py':
                file_path = os.path.join(cls.db_path, filename)
                obj = pickle.load(open(file_path, 'rb'))
                obj_list.append(obj)
        return obj_list

    @classmethod
    def get_obj_by_id(cls, id):
        """
        根据ID获取对象
        :param self:
        :return:
        """
        for filename in os.listdir(cls.db_path):
            if filename == id:
                file_path = os.path.join(cls.db_path, id)
                return pickle.load(open(file_path, 'rb'))
        return None
