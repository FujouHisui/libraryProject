# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'student.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StuInfo(object):
    def setupUi(self, StuInfo):
        StuInfo.setObjectName("StuInfo")
        StuInfo.resize(692, 569)
        self.tableView = QtWidgets.QTableView(StuInfo)
        self.tableView.setGeometry(QtCore.QRect(60, 130, 581, 341))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(StuInfo)
        self.label.setGeometry(QtCore.QRect(70, 90, 191, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(StuInfo)
        self.label_2.setGeometry(QtCore.QRect(110, 500, 311, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(StuInfo)
        self.pushButton.setGeometry(QtCore.QRect(520, 500, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(StuInfo)
        self.label_3.setGeometry(QtCore.QRect(370, 95, 161, 21))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(StuInfo)
        self.pushButton.clicked.connect(StuInfo.backButton_Click)
        QtCore.QMetaObject.connectSlotsByName(StuInfo)

    def retranslateUi(self, StuInfo):
        _translate = QtCore.QCoreApplication.translate
        StuInfo.setWindowTitle(_translate("StuInfo", "StuInfo"))
        self.label.setText(_translate("StuInfo", "学号："))
        self.label_2.setText(_translate("StuInfo", "借书还书请刷书！"))
        self.pushButton.setText(_translate("StuInfo", "返回主页"))
        self.label_3.setText(_translate("StuInfo", "姓名："))