import datetime

import pymysql


# 增,添加借书记录
def log_add(stu_id, book_id):
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO library.borrow_log (stu_id, book_id, , timestamp)
VALUES (''' + stu_id + ''', ''' + book_id + ''' , DEFAULT, null)''')
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
    cursor.execute("DELETE FROM library.book_table WHERE book_id = 5")
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


def search_borrow_log(stu_id):  # 查询借书记录，输入学生学号,返回书的id和书的名字
    sql_select(" book_table.book_id,book_table.book_name,borrow_log.borrow_time,borrow_log.return_time", "borrow_log "
                                                                                                         "inner join "
                                                                                                         " book_table",
               "borrow_log.book_id = book_table.book_id and borrow_log.stu_id = " + stu_id)


def search_needretrun(stu_id):  # 输入学号查询待还书籍
    sql_select("borrow_log.book_id,book_table.book_name", "borrow_log inner join book_table",
               "borrow_log.return_time is null and borrow_log.book_id = book_table.book_id and borrow_log.stu_id = " + stu_id)


def search_borrow_state(book_id):  # 查询书的状态，输入书的ID，被借出返回借阅者学号，未被借出返回0
    result = sql_select("*", "borrow_log", "book_id = " + book_id)
    if len(result) > 0:
        stu_id = result[len(result) - 1]['stu_id']
        return_time = result[len(result) - 1]['return_time']
        if return_time is None:
            return stu_id
        else:
            return 0
    else:
        return -1


def borrow_book(stu_id, book_id):
    # 改
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    try:
        cursor.execute('''INSERT INTO borrow_log (stu_id, book_id, borrow_time, return_time)
VALUES (''' + stu_id + ''', ''' + book_id + ''', DEFAULT, null)''')
        cursor.execute("UPDATE book_table SET is_borrowed = 1 WHERE book_id = " + book_id)
    except pymysql.err.OperationalError:
        return -1
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()


def return_book(stu_id, book_id):
    conn = pymysql.connect(host='la.hisui.tech', port=3306, user='root', passwd='Yz1UBRM3>qx2_Q+7j#zZ', db='library')
    cursor = conn.cursor()
    return_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获得时间数组
    try:
        cursor.execute("UPDATE borrow_log  SET return_time = \"" + return_time + "\" WHERE book_id = " + book_id + " and stu_id = " + stu_id + " and return_time is null")
        cursor.execute("UPDATE book_table SET is_borrowed = 0 WHERE book_id = " + book_id)
    except pymysql.err.OperationalError:
        return -1
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


#if __name__ == '__main__':
#    borrow_book("1800300722","1")
    #return_book("1800300722","3")