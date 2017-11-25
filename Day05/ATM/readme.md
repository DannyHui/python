### ATM
```
 ATM/   主程序目录
    │  ATM.png  ATM流程图文件
    │  readme.md    ATM程序说明文档
    │  test.md  测试说明文档
    │  __init__.py
    │
    ├─bin   程序启动目录
    │      atm.py   ATM入口
    │      __init__.py
    │
    ├─conf  配置目录
    │      settings.py  配置文件
    │      __init__.py
    │
    ├─core  主要业务逻辑
    │      account.py   账户操作模块
    │      auth.py  用户认证模块
    │      db_handle.py 数据库访问模块
    │      log.py   日志操作模块
    │      main.py  主业务逻辑交互模块
    │      product.py   商品模块
    │      shopping.py  购物模块
    │      transaction.py 交易模块
    │      __init__.py
    │
    ├─db    数据存储目录
    │  │  __init__.py
    │  │
    │  ├─accounts   账户目录
    │  │      zyh.json  账户数据文件
    │  │      __init__.py
    │  │
    │  ├─product    商品目录
    │  │      products.json 商品数据文件
    │  │      __init__.py
    │  │
    │  └─shoplist   购物目录
    │          shoplists.json   购物数据文件
    │          __init__.py
    │
    └─log   日志目录
            access.log  登录日志文件
            transaction.log 交易日志文件
            __init__.py
```