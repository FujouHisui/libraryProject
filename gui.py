import sys

from PyQt5.QtWidgets import QWidget, QApplication

from password import Ui_Password
from welcome import Ui_Welcome


class WelcomeForm(QWidget, Ui_Welcome):
    def __init__(self):
        super(WelcomeForm, self).__init__()
        self.setupUi(self)

    def close_wf(self):
        self.close()

    def adminButton_Click(self):
        self.pf = PasswordForm()
        self.pf.show()


class PasswordForm(QWidget, Ui_Password):
    def __init__(self):
        super(PasswordForm, self).__init__()
        self.setupUi(self)

    def show_pf(self):
        self.show()

    def yesButton_Click(self):
        self.close()

    def noButton_Click(self):
        self.close()
