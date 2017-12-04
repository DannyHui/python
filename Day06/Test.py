# -------------------------------
# Task Name：
# Description ：
# Author ： Danny
# date： 2017/12/4
# -------------------------------

class TestClassMethod(object):
    METHOD = 'method hoho'

    def __init__(self):
        self.name = 'danny'

    def test1(self):
        print('-------test1 start---------')
        print('test1')
        print(self.name)
        print('-------test1 end---------')
    @classmethod
    def test2(cls,id):
        print('-------test2 start---------')
        print(cls.METHOD)
        print('test2')
        print(TestClassMethod.METHOD)
        print('--------test2 end --------')

    @staticmethod
    def test3(id):
        print('-------test3 start---------')
        print(TestClassMethod.METHOD)
        print('test3')
        print(id)
        print('-------test3 end---------')


if __name__ == '__main__':
    # a = TestClassMethod()
    # a.test1()
    # a.test2()
    # a.test3()
    TestClassMethod.test3("hh")
    # TestClassMethod.test2("hh")
