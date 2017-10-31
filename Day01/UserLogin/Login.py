import sys

isLock = False
times=0
while not isLock:
    name = input("请输入用户名：")
    # 检查用户是否锁定
    with open('users.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            uname = line.split('/')[0]
            lock = int(line.split('/')[2])
            if uname == name and lock == 1:
                isLock = True
                break
    if isLock:
        print("您好，该用户已被锁定，请联系管理员进行解锁操作！")
        sys.exit()
    isOk=False
    pwd = input("请输入密码：")
    with open('users.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            _name = line.split('/')[0]
            _pwd = line.split('/')[1]
            if _name == name and _pwd == pwd:
                isOk=True
                break
    if not isOk:
        times+=1

    if times==3:
        with open('users.txt', 'w+', encoding='utf-8') as f:
            for line in f.readlines():
                _name = line.split('/')[0]
                _pwd = line.split('/')[1]
                if _name == name:
                    line.replace(line[0:len(line)],line[0:len(line)-1]+'1')
                    break