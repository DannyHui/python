# -------------------------------
# Task Name：三级菜单
# Description ：
# 1、运行程序,输出一级菜单；
# 2、选择一级菜单某项，输出二级菜单，同理输出三级菜单；
# 3、允许用户选择是否退出；
# 4、可以返回上一级菜单；
# Author ： Danny
# date： 2017/10/31
# -------------------------------
import json

# 读取菜单文件的数据
with open("menu.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print("输入提醒：\n‘r’表示返回上一级菜单；\n‘q’表示退出程序；")
# 存储当前菜单的上一级数据
listMenu = []
while True:
    for key in data:
        print(key)
    choice = input("请选择进入：").strip()
    if choice in data:
        # 当data数据为list类型时，已到达最下级菜单
        if type(data) == list:
            print("您已进入最下级菜单，请返回上一级菜单！")
            continue
        # 选择菜单同级的数据保存到列表listMenu，返回上一级使用
        listMenu.append(data)
        # 获取选择菜单的下一级
        data = data[choice]
    elif choice == "r":
        # 当列表listMenu为空时，已到达最上级菜单
        if len(listMenu) == 0:
            print("您已抵达最上级菜单，请选择菜单进入！")
            continue
        # 获取上一级菜单的数据
        data = listMenu[-1]
        # 删除菜单数据列表listMenu的最后一个元素
        listMenu.pop()
    elif choice == "q":
        exit()
    else:
        print("输入错误，请您重新输入！")
        continue
