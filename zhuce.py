import csv
import pymysql
conn=pymysql.connect(host='49.232.42.221',port=3306,user='root',password='123456',charset='utf8',database='bank')
curse=conn.cursor()

def register():
    print('--------用户注册--------------')
    while True:
        name = input('用户名:')
        word = input('密码:')
        repassword = input('确认密码:')

        if word == repassword:
            try:
                result=curse.execute('insert into inf(username,password) values (%s,%s);',(name,word))
                conn.commit()


                # 读取文件


            except Exception as e:
                print('注册失败',e)
                conn.rollback()
            else:
                print('注册成功！')
                break
        else:
            print('两次密码不一致')
if __name__=="__main__":
    register()