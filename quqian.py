import csv
import xuanze



def qu():
    with open(r'lib.csv', mode='r') as rstream:
        users = rstream.readlines()
        for user in users:
            money = int(user[2])
    qu = int(input('输入取出数量：'))
    if qu > int(user[2]):
        print('超过余额')

    else:
        money -= qu
        user[2] = int(money)
        with open(r'lib.csv', mode='a', newline='') as wstream:
            writer_csv = csv.writer(wstream)
            writer_csv.writerow(user)
            print('剩余余额{}'.format(user[2]))
