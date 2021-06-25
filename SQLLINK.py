import pymysql



# 增,添加借书记录
def log_add(stu_id, operation, book_id):
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO library.borrow_log (stu_id, book_id, operation, timestamp)
VALUES (''' + stu_id + ''', ''' + operation + ''', ''' + book_id + ''', DEFAULT)''')
        conn.commit()
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
def sql_select(target, table, search):
    # 表，搜索条件
    # 创建链接对象
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library',
                           cursorclass=pymysql.cursors.DictCursor)
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT " + target + " from " + table + " where " + search)
    except pymysql.err.OperationalError:
        return -1
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
    cursor.execute('''UPDATE library.user_table t SET t.passwd = 'password' WHERE t.id = 2''')
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()



def search_stu_date(stu_id):  # 输入学号查用户详情，返回用户名和学号
    sql_select("uname,passwd,stu_id", "user_table", "stu_id = " + stu_id)


def search_borrow_log(stu_id):  # 查询借书记录，输入学生学号,返回书的id和书的名字
    sql_select("borrow_log.book_id,book_table.book_name", "borrow_log inner join book_table",
               "borrow_log.stu_id = " + stu_id)


def search_needretrun(stu_id):  # 输入学号查询代还书籍
    sql_select("borrow_log.book_id,book_table.book_name", "borrow_log inner join book_table",
               "book.table.is_borrowed = 1 and borrow_log.stu_id = " + stu_id)


def search_borrow_state(book_id):  # 查询书的状态，输入书的ID，返回1为被借出，返回0为未被借出
    sql_select("is_borrowed", "book_table", "book = " + book_id)


def search_passwd(identity, user):
    if identity == 0:
        return sql_select("passwd", "user_table", "is_admin = 0 and stu_id = " + user)
    elif identity == 1:
        return sql_select("passwd", "user_table", "is_admin = 1 and uname = " + "\""+user+"\"")


if __name__ == '__main__':
    print(search_passwd(1, "root")[0]['passwd'])
