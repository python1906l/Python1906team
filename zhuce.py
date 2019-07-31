import csv


def register():
    print('--------用户注册--------------')
    while True:
        username = input('用户名:')
        password = input('密码:')
        repassword = input('确认密码:')

        if password == repassword:
            try:
                # 读取文件
                with open(r'lib.csv', mode='r') as rstream:
                    users = csv.reader(rstream)  # ['zhiqiang#666666\n',.....]
                    if list(users) == []:
                        with open(r'lib.csv', mode='w', newline='') as wstream:
                            writer_csv = csv.writer(wstream)
                            user = [username, password, 0]
                            writer_csv.writerow(user)
                    else:
                        for user in users:
                            uname = user[0]
                            # print('---->uname', uname)
                            # 进行比较判断
                            if username == uname:
                                print('此用户已注册！')
                                return
                            with open(r'lib.csv', mode='a', newline='') as wstream:
                                writer_csv = csv.writer(wstream)
                                user = [username, password, 0]
                                writer_csv.writerow(user)

            except:
                print('注册失败')
            else:
                print('注册成功！')
                break
        else:
            print('两次密码不一致')
if __name__=="__main__":
    register()