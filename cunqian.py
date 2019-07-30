import csv


def cunqian():
    print('------------存款功能-------------------')

    no=input('卡号：')
    pwd=input('密码：')


    with open(r'lib.csv',mode='r') as rstream:
        users=csv.reader(rstream)
        for user in users:
            no=user[0]
            pwd=user[1]
            money=user[2]

            cun=int(input('请输入存款金额：'))
            money+=cun
            user[2]=int(money)
            with open(r'lib.csv',mode='w',newline='')as wstream:
                writer=csv.writer(wstream)
                writer.writerrow(user)
                print('剩余金额{}'.format(user[2]))






