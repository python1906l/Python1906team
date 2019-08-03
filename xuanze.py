from digit import 注册, 登录, 存钱, 取钱
from zhuce import *
from login import denglu
from quqian import *
from cunqian import *
import csv




def xuanze():
    print('1.注册2.登录3.存钱4.取钱5.退出')
    while True:
        choice = int(input("输入选项序号："))
        global flog

        if choice == 注册:

            register()

        elif choice == 登录:
            denglu()

        elif choice == 存钱:
            if denglu():
                cunqian()
            else:
                print('未登录')
        elif choice ==取钱:
            if denglu():
                qu()
            else:
                print('未登录')


        else:
            print('退出')
            break
