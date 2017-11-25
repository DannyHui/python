# -------------------------------
# Task Name：模拟计算器
# Description ：
# Author ： Danny
# date： 2017/11/25
# -------------------------------
import re


def is_operator(expr):
    """
    判断是否是运算符
    :param expr: 字符
    :return:
    """
    operator = ['+', '-', '*', '/', '(', ')']
    return True if expr in operator else False


def calculate(num1, operator, num2):
    """
    计算数字
    :param num1: 数字1
    :param operator: 运算符
    :param num2: 数字2
    :return:
    """
    result = eval(num1 + operator + num2)
    return str(result)


def compare_operator_level(last_oper, cur_oper):
    """
    比较运算符优先级
    :param last_oper: 运算符1
    :param cur_oper: 运算符2
    :return:
    """
    operator1 = ["+", "-"]
    operator2 = ["*", "/"]
    if last_oper == "(" and cur_oper == ")":
        return "="
    elif cur_oper == "(" or last_oper == "(":
        return "<"
    elif last_oper in operator1 and cur_oper in operator2:
        return "<"
    else:
        return ">"


def execute_expression(expression):
    """
    执行表达式
    :param expression: 表达式
    :return:
    """
    # 定义数字栈和运算符栈
    number_stack = []
    operator_stack = []
    for index, expr in enumerate(expression):
        is_oper = is_operator(expr)
        # 数字添加到数字栈
        if not is_oper:
            number_stack.append(expr)
        else:
            while True:
                if len(operator_stack) == 0:
                    if index + 1 < len(expression):
                        operator_stack.append(expr)
                    break
                # 比较运算符优先级
                level = compare_operator_level(operator_stack[-1], expr)
                if level == "=":
                    operator_stack.pop()
                    if index + 1 == len(expression):
                        continue
                    else:
                        break
                elif level == "<":
                    operator_stack.append(expr)
                    break
                elif level == ">":
                    if len(number_stack) == 1:
                        break
                    else:
                        num2 = number_stack.pop()
                        num1 = number_stack.pop()
                        oper = operator_stack.pop()
                        number_stack.append(calculate(num1, oper, num2))
    return number_stack[0]


def parse_expression(expression):
    """
    解析表达式
    :param expression: 表达式
    :return:
    """
    # 去除空格
    expr = re.sub(' ', '', expression)
    # 根据运算符号[+-*/()]进行分割
    init_expr = [ex for ex in re.split('([\+\-\*\/\(\)])', expr) if ex]
    # 区分负数和运算符减号
    expr_new = []
    while True:
        if len(init_expr) == 0:
            break
        expr_char = init_expr.pop(0)
        if len(expr_new) == 0 and expr_char == "-":
            expr_new.append(expr_char + init_expr.pop(0))
            continue
        elif len(expr_new) > 0 and re.search('[\+\-\*\/\(]$', str(expr_new[-1])) and expr_char == "-":
            expr_new.append(expr_char + init_expr.pop(0))
            continue
        expr_new.append(expr_char)
    return expr_new


if __name__ == "__main__":
    expression = "  1 - 2 * ( (60-30 +(-40/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    # 解析表达式
    expr_list = parse_expression(expression)
    # 执行解析的表达式
    result = execute_expression(expr_list)
    # 打印输出结果
    print("eval计算结果：%s" % str(eval(expression)))
    print("程序计算结果：%s" % result)
    print("二者是否相等：%s" % (str(eval(expression)) == result))
