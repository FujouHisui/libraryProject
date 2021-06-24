import sys

from PyQt5.QtCore import QThread

import MQTTLINKR
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget, QApplication

from password import Ui_Password
from welcome import Ui_Welcome
from student import Ui_StuInfo
from confirm import Ui_Confirm
from admin import Ui_Admin


class WorkThread(QThread):
    # 定义一个信号
    trigger = QtCore.pyqtSignal(str)

    def __init__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        if str(MQTTLINKR.subscribe(MQTTLINKR.connect_mqtt())) != "":
            self.trigger.emit('test2')
        else:
            exit(1)


class WelcomeForm(QWidget, Ui_Welcome):
    mqtt_signal = QtCore.pyqtSignal()
    def __init__(self):
        super(WelcomeForm, self).__init__()
        self.setupUi(self)
        self.work = WorkThread()
        self.work.trigger.connect(self.start_student)

    def start_student(self):
        stu_id = str(MQTTLINKR.subscribe(MQTTLINKR.connect_mqtt()))
        if stu_id != "":
            self.pf = PasswordForm()
            self.pf.show_pf(0,stu_id)

    def listen(self):
        if(str(MQTTLINKR.subscribe(MQTTLINKR.connect_mqtt())) != ""):
            self.mqtt_signal.emit()

    def close_wf(self):
        self.close()

    def adminButton_Click(self):
        self.pf = PasswordForm()
        self.pf.show_pf(1,"")


class PasswordForm(QWidget, Ui_Password):
    def __init__(self):
        super(PasswordForm, self).__init__()
        self.identity = -1
        self.setupUi(self)
        self.label_2.setVisible(False)

    def show_pf(self,identity,stu_id):
        self.identity = identity
        if(self.identity == 0):
            self.label_2.setText("您正在以学生身份登录")
            self.label_2.setVisible(True)
        elif(self.identity ==1):
            self.label_2.setText("您正在以管理员身份登录")
            self.label_2.setVisible(True)
        self.stu_id = stu_id
        self.show()

    def yesButton_Click(self):
        if(self.identity == 0):
            self.label.setText("请输入学号："+self.stu_id+"的密码")
            if(self.lineEdit.toPlainText() == "password"):
                self.sf = StudentForm()
                self.sf.show()
                self.close()
            else:
                self.label_2.setStyleSheet("font-color:red")
                self.label_2.setText("密码错误！")
        elif(self.identity == 1):
            self.af = AdminForm()
            self.af.show()
            self.close()

    def noButton_Click(self):
        self.close()


class StudentForm(QWidget, Ui_StuInfo):
    def __init__(self):
        super(StudentForm, self).__init__()
        self.setupUi(self)

    def show_sf(self):
        self.show()

    def backButton_Click(self):
        self.close()


class AdminForm(QWidget, Ui_Admin):
    def __init__(self):
        super(AdminForm, self).__init__()
        self.setupUi(self)

    def stuSearch_Click(self):
        None

    def bookSearch_Click(self):
        None

class ConfirmForm(QWidget, Ui_Confirm):
    def __init__(self):
        super(ConfirmForm, self).__init__()
        self.setupUi(self)

    def yesButton_Click(self):
        self.close()

    def noButton_Click(self):
        self.close()


def gui_start():
    app = QApplication(sys.argv)
    my_pyqt_form = WelcomeForm()
    my_pyqt_form.show()

    sys.exit(app.exec_())
