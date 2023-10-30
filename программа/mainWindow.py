from PyQt5 import QtCore, QtGui, QtWidgets
from staffRoleWindow import StaffRoleWindow
from adminRoleWindow import AdminRoleWindow
import sys

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, user, db):
        super().__init__()
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        self.setStyleSheet(
            "background-color: rgb(49, 51, 56);"
        )
        if user["roleId"] == 1:
            self.setFixedSize(760, 439)
            adminRoleWindow = AdminRoleWindow(user, db)
            self.setCentralWidget(adminRoleWindow)
        elif user["roleId"] == 2:
            self.setFixedSize(731, 379)
            staffRoleWindow = StaffRoleWindow(user, db)
            self.setCentralWidget(staffRoleWindow)

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    app.exec()
