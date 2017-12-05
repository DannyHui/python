# -------------------------------
# Task Name：管理员服务类
# Description ：
# Author ： Danny
# date： 2017/12/3
# -------------------------------
from core.models.ResponseResult import ResponseResult
from core.models.Admin import Admin
from core.models.School import School
from core.models.Teacher import Teacher
from core.models.Course import Course
from core.models.CourseTeacher import CourseTeacher
from core.models.Classes import Classes
from core.models.Student import Student
from prettytable import PrettyTable


class AdminService(object):
    msg = '''
            0:选项
            1:创建学校
            2:查看学校
            3:创建老师
            4:查看老师
            5:创建课程
            6:查看课程
            7:关联老师与课程
            8:创建班级
            9:查看班级
            10:创建学生
            11:查看学生
            12:退出
        '''

    def create_school(self):
        try:
            name = input('请输入学校名字: ').strip()
            address = input('请输入学校地址: ').strip()
            school_list = [(s.name, s.address) for s in School.get_all_list()]
            if (name, address) in school_list:
                raise Exception('[%s] [%s]校区 已经存在,不可重复创建' % (name, address))
            obj_school = School(name, address)
            obj_school.save()
            msg = '[%s] [%s]校区 创建成功' % (obj_school.name, obj_school.address)
            res_result = ResponseResult(True, msg, "")
        except Exception as e:
            res_result = ResponseResult(False, str(e), "")
        return res_result

    def show_school(self):
        # 数据格式化输出
        title = ["学校名称", "地址", "创建日期"]
        x = PrettyTable(title)
        x.align["学校名称"] = "l"  # 以第一个字段左对齐
        x.padding_width = 1
        for s in School.get_all_list():
            x.add_row([s.name, s.address, s.create_time])
        print(x)

    def create_teacher(self):
        try:
            name = input('请输入老师名字: ').strip()
            level = input('请输入老师级别: ').strip()
            teacher_list = [t.name for t in Teacher.get_all_list()]
            if name in teacher_list:
                raise Exception('老师[%s] 已经存在,不可重复创建' % (name))
            obj_teacher = Teacher(name, level)
            obj_teacher.save()
            msg = '老师[%s] 级别[%s] 创建成功' % (obj_teacher.name, obj_teacher.level)
            res_result = ResponseResult(True, msg, "")
        except Exception as e:
            res_result = ResponseResult(False, str(e), "")
        return res_result

    def show_teacher(self):
        # 数据格式化输出
        title = ["老师姓名", "级别", "创建日期"]
        x = PrettyTable(title)
        x.align["老师姓名"] = "l"  # 以第一个字段左对齐
        x.padding_width = 1
        for t in Teacher.get_all_list():
            x.add_row([t.name, t.level, t.create_time])
        print(x)

    def create_course(self):
        try:
            print('创建课程'.center(60, '*'))
            school_list = School.get_all_list()
            for index, s in enumerate(school_list):
                print(index, s.name, s.address)
            while True:
                sid = input('请选择学校: ').strip()
                if sid.isdigit() and int(sid) in range(0, len(school_list)):
                    break
                else:
                    print("\033[1;31;40m选项错误，请重新输入!\033[0m")
                    continue
            obj_school = school_list[int(sid)]
            name = input('请输入课程名: ').strip()
            price = input('请输入课程价格: ').strip()
            period = input('请输入课程周期: ').strip()
            course_list = [(c.name, c.school_id) for c in Course.get_all_list()]
            if (name, obj_school.id) in course_list:
                raise Exception('课程[%s] 已经存在,不可重复创建' % (name))
            obj_course = Course(name, price, period, obj_school.id)
            obj_course.save()
            msg = '课程[%s] 价格[%s] 周期[%s] 创建成功' % (obj_course.name, obj_course.price, obj_course.period)
            res_result = ResponseResult(True, msg, "")
        except Exception as e:
            res_result = ResponseResult(False, str(e), "")
        return res_result

    def show_course(self):
        # 数据格式化输出
        title = ["课程名称", "价格", "周期", "学校"]
        x = PrettyTable(title)
        x.align["课程名称"] = "l"  # 以第一个字段左对齐
        x.padding_width = 1
        for c in Course.get_all_list():
            school_obj = School.get_obj_by_id(c.school_id)
            school_name = "XXX"
            if not school_obj is None:
                school_name = school_obj.name
            x.add_row([c.name, c.price, c.period, school_name])
        print(x)

    def create_course_teacher(self):
        try:
            print('关联老师与课程'.center(60, '*'))
            # 选择老师
            teacher_list = Teacher.get_all_list()
            for index, t in enumerate(teacher_list):
                print(index, t.name)
            while True:
                tid = input('请选择老师: ').strip()
                if tid.isdigit() and int(tid) in range(0, len(teacher_list)):
                    break
                else:
                    print("\033[1;31;40m选项错误，请重新输入!\033[0m")
                    continue
            obj_teacher = teacher_list[int(tid)]
            # 选择课程
            course_list = Course.get_all_list()
            for index, c in enumerate(course_list):
                print(index, c.name)
            while True:
                cid = input('请选择课程: ').strip()
                if cid.isdigit() and int(cid) in range(0, len(course_list)):
                    break
                else:
                    print("\033[1;31;40m选项错误，请重新输入!\033[0m")
                    continue
            obj_course = course_list[int(cid)]
            course_teacher_list = [(ct.teacher_id, ct.course_id) for ct in CourseTeacher.get_all_list()]
            if (obj_teacher.id, obj_course.id) in course_teacher_list:
                raise Exception('课程[%s] 老师[%s] 关联关系已经存在,不可重复创建' % (obj_course.name, obj_teacher.name))
            obj_course_teacher = CourseTeacher(obj_course.id, obj_teacher.id)
            obj_course_teacher.save()
            msg = '课程[%s] 老师[%s] 关联关系 创建成功' % (obj_course.name, obj_teacher.name)
            res_result = ResponseResult(True, msg, "")
        except Exception as e:
            res_result = ResponseResult(False, str(e), "")
        return res_result

    def create_classes(self):
        try:
            print('创建班级'.center(60, '*'))
            # 选择学校
            school_list = School.get_all_list()
            for index, s in enumerate(school_list):
                print(index, s.name, s.address)
            while True:
                sid = input('请选择学校: ').strip()
                if sid.isdigit() and int(sid) in range(0, len(school_list)):
                    break
                else:
                    print("\033[1;31;40m选项错误，请重新输入!\033[0m")
                    continue
            obj_school = school_list[int(sid)]
            name = input('请输入班级名称: ').strip()
            # 选择课程-老师
            course_teacher_list = CourseTeacher.get_all_list()
            for index, ct in enumerate(course_teacher_list):
                course_obj = Course.get_obj_by_id(ct.course_id)
                teacher_obj = Teacher.get_obj_by_id(ct.teacher_id)
                print(index, course_obj.name, teacher_obj.name)
            while True:
                ctid = input('请选择课程-老师: ').strip()
                if ctid.isdigit() and int(ctid) in range(0, len(course_teacher_list)):
                    break
                else:
                    print("\033[1;31;40m选项错误，请重新输入!\033[0m")
                    continue
            course_teacher = course_teacher_list[int(ctid)]
            c_obj = Course.get_obj_by_id(course_teacher.course_id)
            t_obj = Teacher.get_obj_by_id(course_teacher.teacher_id)
            classes_list = [(c.name, c.school_id, c.course_teacher_id) for c in Classes.get_all_list()]
            if (name, obj_school.id, course_teacher.id) in classes_list:
                raise Exception(
                    '班级[%s] 学校[%s] 课程[%s] 老师[%s] 已经存在,不可重复创建'
                    % (name, obj_school.name, c_obj.name, t_obj.name))
            obj_classes = Classes(name, obj_school.id, course_teacher.id)
            obj_classes.save()
            msg = '学校[%s] 班级[%s] 课程[%s] 老师[%s] 创建成功' % (obj_school.name, name, c_obj.name, t_obj.name)
            res_result = ResponseResult(True, msg, "")
        except Exception as e:
            res_result = ResponseResult(False, str(e), "")
        return res_result

    def show_classes(self):
        # 数据格式化输出
        title = ["班级名称", "学校名称", "课程", "老师"]
        x = PrettyTable(title)
        x.align["班级名称"] = "l"  # 以第一个字段左对齐
        x.padding_width = 1
        for c in Classes.get_all_list():
            # 学校名称
            school_obj = School.get_obj_by_id(c.school_id)
            course_teacher = CourseTeacher.get_obj_by_id(c.course_teacher_id)
            c_obj = Course.get_obj_by_id(course_teacher.course_id)
            t_obj = Teacher.get_obj_by_id(course_teacher.teacher_id)
            x.add_row([c.name, school_obj.name, c_obj.name, t_obj.name])
        print(x)

    def create_student(self):
        try:
            name = input('请输入学生名字: ').strip()
            age = input('请输入学生年龄: ').strip()
            sex = input('请输入学生性别: ').strip()
            # 选择班级
            classes_list = Classes.get_all_list()
            for index, s in enumerate(classes_list):
                # 学校名称
                school_obj = School.get_obj_by_id(s.school_id)
                print(index, s.name, school_obj.name)
            while True:
                cid = input('请选择班级: ').strip()
                if cid.isdigit() and int(cid) in range(0, len(classes_list)):
                    break
                else:
                    print("\033[1;31;40m选项错误，请重新输入!\033[0m")
                    continue
            obj_classes = classes_list[int(cid)]
            student_list = [s.name for s in Student.get_all_list()]
            if name in student_list:
                raise Exception('学生[%s] 班级[%s] 已经存在,不可重复创建' % (name, obj_classes.name))
            obj_student = Student(name, age, sex, obj_classes.id)
            obj_student.save()
            msg = '学生[%s] 年龄[%s] 性别[%s] 班级[%s] 创建成功' % (
                obj_student.name, obj_student.age, obj_student.sex, obj_classes.name)
            res_result = ResponseResult(True, msg, "")
        except Exception as e:
            res_result = ResponseResult(False, str(e), "")
        return res_result

    def show_student(self):
        # 数据格式化输出
        title = ["学生姓名", "年龄", "性别", "创建日期", "班级"]
        x = PrettyTable(title)
        x.align["学生姓名"] = "l"  # 以第一个字段左对齐
        x.padding_width = 1
        for s in Student.get_all_list():
            # 班级名称
            classes_obj = Classes.get_obj_by_id(s.classes_id)
            x.add_row([s.name, s.age, s.sex, s.create_time, classes_obj.name])
        print(x)

    def show(self):
        print(self.msg)

    def main(self):
        choice_dic = {
            '0': self.show,
            '1': self.create_school,
            '2': self.show_school,
            '3': self.create_teacher,
            '4': self.show_teacher,
            '5': self.create_course,
            '6': self.show_course,
            '7': self.create_course_teacher,
            '8': self.create_classes,
            '9': self.show_classes,
            '10': self.create_student,
            '11': self.show_student,
            '12': exit
        }
        while True:
            self.show()
            choice = input('请选择操作项<<<:').strip()
            if choice in choice_dic:
                res_result = choice_dic[choice]()
                if not res_result is None:
                    if res_result.status:
                        print(("\033[1;32;40m%s\033[0m" % res_result.msg).center(60, '-'))
                    else:
                        print(("\033[1;31;40m%s\033[0m" % res_result.msg).center(60, '-'))
            else:
                print("\033[1;31;40m选项错误，请重新输入!\033[0m")

    def login(self):
        res_data = Admin.login()
        if res_data:
            if res_data['status']:
                print(res_data['data'].center(60, '-'))
                self.main()
            else:
                print(res_data['error'].center(60, '-'))
