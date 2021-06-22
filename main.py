# This is a sample Python script.
import sys

from PyQt5 import QtWidgets
from gui import WelcomeForm

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = WelcomeForm()
    my_pyqt_form.show()
    sys.exit(app.exec_())

