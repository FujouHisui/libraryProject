import datetime

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


def search_stu_date(stu_id):  # 输入学号查用户详情，返回用户名和学号
    sql_select("uname,passwd,stu_id", "user_table", "stu_id = " + stu_id)


def search_borrow_log(stu_id):  # 查询借书记录，输入学生学号,返回书的id和书的名字
    sql_select(" book_table.book_id,book_table.book_name,borrow_log.borrow_time,borrow_log.return_time", "borrow_log "
                                                                                                         "inner join "
                                                                                                         " book_table",
               "borrow_log.book_id = book_table.book_id and borrow_log.stu_id = " + stu_id)


def search_borrow_log_book(book_id):  # 查询借书记录，输入书号,返回书的id和书的名字借阅归还日期
    sql_select(" book_table.book_id,book_table.book_name,borrow_log.borrow_time,borrow_log.return_time", "borrow_log "
                                                                                                         "inner join "
                                                                                                         " book_table",
               "borrow_log.book_id = book_table.book_id and borrow_log.book_id = " + book_id)


def search_needretrun(stu_id):  # 输入学号查询代还书籍
    sql_select("borrow_log.book_id,book_table.book_name", "borrow_log inner join book_table",
               "borrow_log.return_time is null and borrow_log.book_id = book_table.book_id and borrow_log.stu_id = " + stu_id)


def search_borrow_state(book_id):  # 查询书的状态，输入书的ID，返回1为被借出，返回0为未被借出
    return sql_select("is_borrowed", "book_table", "book_id = " + book_id)[0]['is_borrowed']


def book_status_change(book_id):
    # 改
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    search_borrow_state(book_id)  # 获取状态，判断状态，为1置零，为零置1，读取数据比较处理

    if search_borrow_state(book_id):
        cursor.execute("UPDATE book_table  SET is_borrowed = '0' WHERE book_id = " + book_id)
    else:
        cursor.execute("UPDATE book_table  SET is_borrowed = '1' WHERE book_id = " + book_id)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def borrow_log_update(stu_id, book_id):
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    returntime = datetime.datetime.now()  # 获得时间数组
    if search_borrow_state(book_id):  # 判断状态，为零新增，为1修改
        book_status_change(book_id)
        cursor.execute(
            "UPDATE borrow_log  SET return_time = " + returntime + " WHERE book_id = " + book_id + "and stu_id = " + stu_id + "and return_time is null")
    else:
        book_status_change(book_id)
        cursor.execute("insert into borrow_log (stu_id,book_id)VALUES(" + stu_id + "," + book_id + ")")
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()



def search_passwd(identity, user):
    if identity == 0:
        return sql_select("passwd", "user_table", "is_admin = 0 and stu_id = " + user)
    elif identity == 1:
        return sql_select("passwd", "user_table", "is_admin = 1 and uname = " + "\"" + user + "\"")


def get_stu_name(stu_id):
    name_result = sql_select("stu_name", "stu_table", "stu_id = " + stu_id)
    if len(name_result) > 0:
        return name_result[0]['stu_name']
    else:
        return None


def get_book_name(book_id):
    name_result = sql_select("book_name", "book_table", "book_id = " + book_id)
    if len(name_result) > 0:
        return name_result[0]['book_name']
    else:
        return None


def stu_borrow_log(stu_id):
    raw_result = sql_select(" book_table.book_id,book_table.book_name,borrow_log.borrow_time,borrow_log.return_time",
                            "borrow_log inner join book_table",
                            "borrow_log.book_id = book_table.book_id and borrow_log.stu_id = " + stu_id)
    if len(raw_result) > 0:
        result = []
        for i in range(0, len(raw_result)):
            temp = []
            temp.append(raw_result[i]['book_id'])
            temp.append(raw_result[i]['book_name'])
            temp.append(str(raw_result[i]['borrow_time']))
            if raw_result[i]['return_time'] == None:
                temp.append("未还")
            else:
                temp.append(str(raw_result[i]['return_time']))
            result.append(temp)
        for row in result:
            for column in row:
                print(column)
        return result
    else:
        return None


def book_borrow_log(book_id):
    raw_result = sql_select(" stu_table.stu_id,stu_table.stu_name,borrow_log.borrow_time,borrow_log.return_time",
                            "borrow_log inner join stu_table",
                            "borrow_log.stu_id = stu_table.stu_id and borrow_log.book_id = " + book_id)
    if len(raw_result) > 0:
        result = []
        for i in range(0, len(raw_result)):
            temp = []
            temp.append(raw_result[i]['stu_id'])
            temp.append(raw_result[i]['stu_name'])
            temp.append(str(raw_result[i]['borrow_time']))
            if raw_result[i]['return_time'] == None:
                temp.append("未还")
            else:
                temp.append(str(raw_result[i]['return_time']))
            result.append(temp)
        for row in result:
            for column in row:
                print(column)
        return result
    else:
        return None


if __name__ == '__main__':
    print(search_passwd(1, "root")[0]['passwd'])
