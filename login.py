from PyQt6 import QtCore, QtGui, QtWidgets
from db import Database
from mainWindow import MainWindow
import sys

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.db = Database()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(375, 480)
        self.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.title_lbl = QtWidgets.QLabel(parent=self)
        self.title_lbl.setGeometry(QtCore.QRect(80, 20, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_lbl.setObjectName("title_lbl")
        self.login_lbl = QtWidgets.QLabel(parent=self)
        self.login_lbl.setGeometry(QtCore.QRect(30, 80, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.login_lbl.setFont(font)
        self.login_lbl.setStyleSheet("color: rgb(220, 220, 220);")
        self.login_lbl.setObjectName("login_lbl")
        self.password_lbl = QtWidgets.QLabel(parent=self)
        self.password_lbl.setGeometry(QtCore.QRect(30, 210, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.password_lbl.setFont(font)
        self.password_lbl.setStyleSheet("color: rgb(220, 220, 220);")
        self.password_lbl.setObjectName("password_lbl")
        self.login_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.login_lineEdit.setGeometry(QtCore.QRect(30, 140, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setStyleSheet("background-color: #1e1f22;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: rgb(229, 229, 229);")
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.password_lineEdit.setGeometry(QtCore.QRect(30, 270, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("background-color: #1e1f22;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: rgb(229, 229, 229);")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.login_lineEdit.setPlaceholderText("Ваш логин")
        self.password_lineEdit.setPlaceholderText("Ваш пароль")
        self.password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.login_btn = QtWidgets.QPushButton(parent=self)
        self.login_btn.setGeometry(QtCore.QRect(20, 380, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Magneto")
        font.setPointSize(16)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.login_btn.setStyleSheet("background-color: rgb(88, 101, 242);\n"
"color: rgb(230, 230, 230);")
        self.login_btn.setObjectName("login_btn")
        self.err_lbl = QtWidgets.QLabel(parent=self)
        self.err_lbl.setGeometry(QtCore.QRect(60, 440, 261, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.err_lbl.setFont(font)
        self.err_lbl.setStyleSheet("color: rgb(208, 90, 90);")
        self.err_lbl.setObjectName("err_lbl")
        self.err_lbl.setHidden(True)
        self.login_btn.clicked.connect(self.login_clicked)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Авторизация"))
        self.title_lbl.setText(_translate("Form", "Добро пожаловать"))
        self.login_lbl.setText(_translate("Form", "Логин"))
        self.password_lbl.setText(_translate("Form", "Пароль"))
        self.login_btn.setText(_translate("Form", "Вход"))
        self.err_lbl.setText(_translate("Form", "Неверный логин или пароль"))
    
    def login_clicked(self):
        auth = self.db.login(self.login_lineEdit.text(), self.password_lineEdit.text())
        if auth == False:
            self.err_lbl.setHidden(False)
        else:
            self.mainWindow = MainWindow(auth, self.db)
            self.mainWindow.show()
            self.close()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    appendTaskWindow = LoginWindow()
    appendTaskWindow.show()
    app.exec()
