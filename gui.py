import sys

from PyQt5.QtCore import QThread

import MQTTLINKR
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication

import SQLDATA
import SQLLINK
from password import Ui_Password
from welcome import Ui_Welcome
from student import Ui_StuInfo
from confirm import Ui_Confirm
from admin import Ui_Admin
from student_admin import Ui_StudentSearch
from book_admin import Ui_BookInfo

payloads = []


class WorkThread(QThread):
    # 定义一个信号
    trigger = QtCore.pyqtSignal(str)

    def __init__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        MQTTLINKR.run()


class WelcomeForm(QWidget, Ui_Welcome):
    thread = WorkThread()

    def __init__(self):
        super(WelcomeForm, self).__init__()
        self.setupUi(self)
        self.label_3.setVisible(False)
        self.work = WorkThread()
        self.work.trigger.connect(self.start_student)
        self.thread.start()

    def start_student(self):
        data = [-1, -1]
        if len(payloads) > 0:
            data = MQTTLINKR.legit_data(payloads[len(payloads) - 1])
            print(data[1])
        if data[0] == "P":
            self.label_3.setVisible(False)
            self.pf = PasswordForm()
            self.pf.show_pf(0, data[1])
        else:
            self.label_3.setText("未检测到卡！")
            self.label_3.setVisible(True)

    def listen(self):
        if (str(MQTTLINKR.subscribe(MQTTLINKR.connect_mqtt())) != ""):
            self.mqtt_signal.emit()

    def close_wf(self):
        self.close()

    def adminButton_Click(self):
        self.pf = PasswordForm()
        self.pf.show_pf(1, "")


class PasswordForm(QWidget, Ui_Password):
    def __init__(self):
        super(PasswordForm, self).__init__()
        self.identity = -1
        self.setupUi(self)
        self.label_2.setVisible(False)

    def show_pf(self, identity, stu_id):
        self.identity = identity
        if (self.identity == 0):
            self.label_2.setText("您正在以学生身份登录")
            self.label_2.setVisible(True)
        elif (self.identity == 1):
            self.label_2.setText("您正在以管理员身份登录")
            self.label_2.setVisible(True)
        self.stu_id = stu_id
        self.label.setText("请输入" + self.stu_id + "的密码")
        self.show()

    def yesButton_Click(self):
        if self.identity == 0:
            passwd_result = SQLLINK.search_passwd(0, self.stu_id)
            if len(passwd_result) > 0:
                if self.lineEdit.text() == passwd_result[0]['passwd']:
                    self.sf = StudentForm()
                    self.sf.show()
                    self.close()
                else:
                    self.label_2.setStyleSheet("font-color:red")
                    self.label_2.setText("密码错误！")
        elif self.identity == 1:
            passwd_result = SQLLINK.search_passwd(1, "root")
            if len(passwd_result) > 0:
                if self.lineEdit.text() == passwd_result[0]['passwd']:
                    self.af = AdminForm()
                    self.af.show()
                    self.close()
                else:
                    self.label_2.setStyleSheet("font-color:red")
                    self.label_2.setText("密码错误！")

    def noButton_Click(self):
        self.close()


class StudentForm(QWidget, Ui_StuInfo):
    def __init__(self):
        super(StudentForm, self).__init__()
        self.setupUi(self)

    def show_sf(self):
        self.show()

    def optButton_Click(self):
        self.cf = ConfirmForm()
        self.cf.cf_show(1)

    def backButton_Click(self):
        self.close()


class AdminForm(QWidget, Ui_Admin):
    def __init__(self):
        super(AdminForm, self).__init__()
        self.setupUi(self)

    def stuSearch_Click(self):
        self.ssf = StudentSearchForm()
        self.ssf.show()

    def bookSearch_Click(self):
        self.bsf = BookSearchForm()
        self.bsf.show()

    def backButton_Click(self):
        self.close()


class BookSearchForm(QWidget, Ui_BookInfo):
    def __init__(self):
        super(BookSearchForm, self).__init__()
        self.setupUi(self)

    def searchButton_Click(self):
        None

    def backButton_Click(self):
        self.close()


class StudentSearchForm(QWidget, Ui_StudentSearch):
    def __init__(self):
        super(StudentSearchForm, self).__init__()
        self.setupUi(self)

    def backButton_Click(self):
        self.close()

    def searchButton_Click(self):
        None




class ConfirmForm(QWidget, Ui_Confirm):
    def __init__(self):
        super(ConfirmForm, self).__init__()
        self.setupUi(self)

    def cf_show(self, opt):
        if opt == 1:
            self.opt = "借出"
        elif opt == 0:
            self.opt = "归还"
        self.label.setText("确认" + self.opt + "书籍？")
        self.show()

    def yesButton_Click(self):
        self.close()

    def noButton_Click(self):
        self.close()


def gui_start():
    app = QApplication(sys.argv)
    my_pyqt_form = WelcomeForm()
    my_pyqt_form.show()
    sys.exit(app.exec_())
