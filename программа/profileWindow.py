from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class ProfileWindow(QtWidgets.QWidget):
    def __init__(self, db, user, setParentUser):
        super().__init__()
        self.user = user
        self.db = db
        setParentUser
        self.setupUi(setParentUser)

    def setupUi(self, setParentUser):
        self.setObjectName("Form")
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setFixedSize(341, 545)
        self.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.title_lbl = QtWidgets.QLabel(parent=self)
        self.title_lbl.setGeometry(QtCore.QRect(70, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color: rgb(246, 245, 244);")
        self.title_lbl.setObjectName("title_lbl")
        self.thirdname_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.thirdname_lineEdit.setGeometry(QtCore.QRect(20, 270, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.thirdname_lineEdit.setFont(font)
        self.thirdname_lineEdit.setStyleSheet("color: rgb(246, 245, 244);\n"
"background-color: #1e1f22;\n"
"border: none;")
        self.thirdname_lineEdit.setObjectName("thirdname_lineEdit")
        self.thirdname_lbl = QtWidgets.QLabel(parent=self)
        self.thirdname_lbl.setGeometry(QtCore.QRect(30, 230, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.thirdname_lbl.setFont(font)
        self.thirdname_lbl.setStyleSheet("color: rgb(222, 221, 218);")
        self.thirdname_lbl.setObjectName("thirdname_lbl")
        self.secondname_lbl = QtWidgets.QLabel(parent=self)
        self.secondname_lbl.setGeometry(QtCore.QRect(30, 150, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.secondname_lbl.setFont(font)
        self.secondname_lbl.setStyleSheet("color: rgb(222, 221, 218);")
        self.secondname_lbl.setObjectName("secondname_lbl")
        self.name_lbl = QtWidgets.QLabel(parent=self)
        self.name_lbl.setGeometry(QtCore.QRect(30, 80, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.name_lbl.setFont(font)
        self.name_lbl.setStyleSheet("color: rgb(222, 221, 218);")
        self.name_lbl.setObjectName("name_lbl")
        self.secondname_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.secondname_lineEdit.setGeometry(QtCore.QRect(20, 190, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.secondname_lineEdit.setFont(font)
        self.secondname_lineEdit.setStyleSheet("color: rgb(246, 245, 244);\n"
"background-color: #1e1f22;\n"
"border: none;")
        self.secondname_lineEdit.setObjectName("secondname_lineEdit")
        self.name_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.name_lineEdit.setGeometry(QtCore.QRect(20, 110, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.name_lineEdit.setFont(font)
        self.name_lineEdit.setStyleSheet("color: rgb(246, 245, 244);\n"
"background-color: #1e1f22;\n"
"border: none;")
        self.name_lineEdit.setObjectName("name_lineEdit")
        self.enter_btn = QtWidgets.QPushButton(parent=self)
        self.enter_btn.setEnabled(True)
        self.enter_btn.setGeometry(QtCore.QRect(100, 490, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.enter_btn.setFont(font)
        self.enter_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.enter_btn.setStyleSheet("background-color: rgb(99, 97, 235);\n"
"color: rgb(222, 221, 218);")
        self.enter_btn.setObjectName("enter_btn")
        self.password_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.password_lineEdit.setGeometry(QtCore.QRect(20, 430, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.password_lineEdit.setFont(font)
        self.password_lineEdit.setStyleSheet("color: rgb(246, 245, 244);\n"
"background-color: #1e1f22;\n"
"border: none;")
        self.password_lineEdit.setObjectName("password_lineEdit")
        self.password_lbl = QtWidgets.QLabel(parent=self)
        self.password_lbl.setGeometry(QtCore.QRect(30, 390, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.password_lbl.setFont(font)
        self.password_lbl.setStyleSheet("color: rgb(222, 221, 218);")
        self.password_lbl.setObjectName("password_lbl")
        self.login_lineEdit = QtWidgets.QLineEdit(parent=self)
        self.login_lineEdit.setGeometry(QtCore.QRect(20, 350, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.login_lineEdit.setFont(font)
        self.login_lineEdit.setStyleSheet("color: rgb(246, 245, 244);\n"
"background-color: #1e1f22;\n"
"border: none;")
        self.login_lineEdit.setObjectName("login_lineEdit")
        self.login_lbl = QtWidgets.QLabel(parent=self)
        self.login_lbl.setGeometry(QtCore.QRect(30, 310, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.login_lbl.setFont(font)
        self.login_lbl.setStyleSheet("color: rgb(222, 221, 218);")
        self.login_lbl.setObjectName("login_lbl")
        self.enter_btn.clicked.connect(lambda: self.enterBtn_clicked(setParentUser))

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def enterBtn_clicked(self, setParentUser):
        self.db.updateUser(self.user['idUser'], self.user['idAc'], self.name_lineEdit.text(), self.secondname_lineEdit.text(), self.thirdname_lineEdit.text(), self.login_lineEdit.text(), self.password_lineEdit.text())
        #newUs = {"idAc": self.user['idAc'], "login": self.login_lineEdit.text(), "password": self.password_lineEdit.text(), "idUser": self.user["idUser"], "name": self.name_lineEdit.text(), "secondname": self.secondname_lineEdit.text(), "thirstname": self.thirdname_lineEdit.text(), "pos": self.user["pos"], "roleId": self.user["roleId"]}
        newUs = {"idAc": self.user['idAc'], "login": self.login_lineEdit.text(), "password": self.password_lineEdit.text(), "idUser": self.user["idUser"], "name": self.name_lineEdit.text(), "secondname": self.secondname_lineEdit.text(), "thirstname": self.thirdname_lineEdit.text(), "roleId": self.user["roleId"]}
        setParentUser(newUs) 
        self.close()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Мой профиль"))
        self.title_lbl.setText(_translate("Form", "Мой профиль"))
        self.thirdname_lineEdit.setText(_translate("Form", self.user['thirstname']))
        self.thirdname_lbl.setText(_translate("Form", "Отчество"))
        self.secondname_lbl.setText(_translate("Form", "Фамилия"))
        self.name_lbl.setText(_translate("Form", "Имя"))
        self.secondname_lineEdit.setText(_translate("Form", self.user['secondname']))
        self.name_lineEdit.setText(_translate("Form", self.user['name']))
        self.enter_btn.setText(_translate("Form", "Изменить"))
        self.password_lineEdit.setText(_translate("Form", self.user['password']))
        self.password_lbl.setText(_translate("Form", "Пароль"))
        self.login_lineEdit.setText(_translate("Form", self.user['login']))
        self.login_lbl.setText(_translate("Form", "Логин"))

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    profileWindow = ProfileWindow()
    profileWindow.show()
    app.exec()
