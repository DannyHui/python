import sys

# 用户是否锁定
isLock = False
# 用户是否存在
isExist = False
# 用户名和密码是否验证正确
isOk = False
# 输入密码的次数
times = 0
while not isLock:
    if not isExist:
        name = input("请输入用户名：")
        # 检查用户是否存在
        with open('users.txt', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                uname = line.split('/')[0]
                if uname == name:
                    isExist = True
                    break
        if not isExist:
            print("您好，该用户不存在，请输入正确的用户名！")
            continue
    # 检查用户是否锁定
    with open('users.txt', 'r', encoding='utf-8') as f1:
        for line in f1.readlines():
            uname = line.split('/')[0]
            lock = int(line.split('/')[2])
            if uname == name and lock == 1:
                isLock = True
                break
    if isLock:
        print("您好，该用户已被锁定，请联系管理员进行解锁操作！")
        sys.exit()
    # 验证用户名和密码的是否正确
    pwd = input("请输入密码：")
    with open('users.txt', 'r', encoding='utf-8') as f2:
        for line in f2.readlines():
            _name = line.split('/')[0]
            _pwd = line.split('/')[1]
            if _name == name and _pwd == pwd:
                isOk = True
                break
    if isOk:
        print("登录成功！")
        sys.exit()
    else:
        times += 1
        # 提示警告信息
    if times == 2:
        print("您好，请仔细输入，您还有最后一次输入密码的机会，否则系统将锁定该用户！")

    # 输入密码错误3次，锁定该用户
    if times == 3:
        # 将文件读取到内存中
        with open("users.txt", "r", encoding="utf-8") as f3:
            lines = f3.readlines()
        # 写的方式打开文件
        with open("users.txt", "w", encoding="utf-8") as f4:
            for line in lines:
                _name = line.split('/')[0]
                if _name == name:
                    # 替换
                    old_str = line.strip()
                    new_str = line[:-2] + "1"
                    line = line.replace(old_str, new_str)
                f4.write(line)
