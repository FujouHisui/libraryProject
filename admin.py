# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName("Admin")
        Admin.resize(900, 700)
        self.layoutWidget = QtWidgets.QWidget(Admin)
        self.layoutWidget.setGeometry(QtCore.QRect(290, 200, 331, 281))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(Admin)
        self.pushButton_3.setGeometry(QtCore.QRect(690, 580, 92, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Admin)
        self.pushButton.clicked.connect(Admin.stuSearch_Click)
        self.pushButton_2.clicked.connect(Admin.bookSearch_Click)
        self.pushButton_3.clicked.connect(Admin.backButton_Click)
        QtCore.QMetaObject.connectSlotsByName(Admin)

    def retranslateUi(self, Admin):
        _translate = QtCore.QCoreApplication.translate
        Admin.setWindowTitle(_translate("Admin", "Admin"))
        self.pushButton.setText(_translate("Admin", "查学号"))
        self.pushButton_2.setText(_translate("Admin", "查书"))
        self.pushButton_3.setText(_translate("Admin", "返回主页"))
