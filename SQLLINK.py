import pymysql

'''
#列表
# 创建链接对象
conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
# 创建游标
cursor = conn.cursor()
# 执行sql，更新单条数据，并返回受影响行数
cursor.execute("SELECT * from user_table")
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
'''


# 增
def log_add(stu_id,operation,book_id):
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO library.borrow_log (stu_id, book_id, operation, timestamp)
VALUES ('''+stu_id+''', '''+operation+''', '''+book_id+''', DEFAULT)''')
    except pymysql.err.OperationalError:
        print("输入数据有误")
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return -1
    else:
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return 0


def sql_delete():
    # 删
    # 表 条件
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM library.user_table WHERE id = 3")
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


# 查
def sql_select():
    # 表，搜索条件
    # 创建链接对象
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    cursor.execute("SELECT * from user_table where id=2")
    result = cursor.fetchall()
    print(result)
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return result


def book_status_change():
    # 改
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    cursor.execute('''UPDATE library.user_table t SET t.passwd = 'passwor' WHERE t.id = 2''')
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


if __name__ == '__main__':
    sql_add()
