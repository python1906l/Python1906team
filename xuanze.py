#from 注册 import ×
#from 登录 import ×
#from 取钱 import ×
#from 存钱 import ×
import csv
flog=False
def xuanze():
    print('1.注册2.登录3.存钱4.取钱5.退出')
    while True:
        choice=int(input("输入选项序号："))
        global flog

        if choice==1:

            register()
            return True
        elif choice==2 and flog:
            denglu()

        elif choice == 3 and flog:
            cunqian()
        elif choice == 4 and flog:
            quqian()

        else:
            print('退出')
            break