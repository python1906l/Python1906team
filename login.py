import xuanze


def denglu():
    print('-----用户登录------')
    username = input('用户名:')
    password = input('密码:')
    import pymysql
    conn = pymysql.connect(host='49.232.42.221', port=3306, user='root', password='123456', charset='utf8',
                           database='bank')
    curse = conn.cursor()
    try:
        result = curse.execute('select username,password,money from inf where username={} and password={};'.format(username,password))
        print('用户信息：用户名：{}密码：{}余额：{}'.format(username,password,result[2]))



    except Exception as e:
        print('登录失败', e)
        conn.rollback()
    else:
        print('登陆成功')
        return True

    # 读取文件





if __name__ == '__main__':

    denglu()
