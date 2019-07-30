from zhuce import *
from denglu import *
from quqian import *
from cunqian import *
import csv
from login import denglu
flog=False

def xuanze():
    print('1.注册2.登录3.存钱4.取钱5.退出')
    while True:
        choice=int(input("输入选项序号："))
        global flog

        if choice==1:

            register()

        elif choice==2 :
            denglu()
            flog=True
            return flog
        elif choice == 3 :
            if flog:
                cunqian()
            else:
                print('未登录')
        elif choice == 4 :
            if flog:
                quqian()
            else:
                print('未登录')


        else:
            print('退出')
            break