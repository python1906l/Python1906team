import xuanze
import csv

def denglu():
    print('-----用户登录------')
    username = input('用户名:')
    password = input('密码:')

    # 读取文件
    with open(r'lib.csv', mode='r') as rstream:
        users = rstream.readlines()
        print('users',users)
        for user in users:
            uname = user[0]
            pwd = user[1]
            money = user[-1]
            print('money',money)
            # print(uname, pwd)
            # 进行比较判断
            if username == uname and password == pwd:
                print('用户登录成功,余额：{}'.format(money))
                break
            else:
                print('输入错误！')


if __name__ == '__main__':

    denglu()
