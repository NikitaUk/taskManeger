from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import datetime

class AppendTaskWindow(QtWidgets.QWidget):
    def __init__(self, db, guarantor, lastTask):
        super().__init__()
        spisok = db.getStaffsNames()
        self.db = db
        self.guarantor = guarantor
        self.exspisok = []
        self.setupUi(spisok, lastTask)

    def setupUi(self, users, lastTask):
        today = datetime.date.today()
        date = QtCore.QDate(today.year, today.month, today.day)
        self.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        self.setObjectName("Form")
        self.setFixedSize(395, 484)
        self.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.label_2 = QtWidgets.QLabel(parent=self)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self)
        self.label_3.setGeometry(QtCore.QRect(140, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self)
        self.lineEdit.setGeometry(QtCore.QRect(40, 110, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #1e1f22;\n"
"border: none;\n"
"border-radius: 10px;\n"
"color: rgb(229, 229, 229);")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(parent=self)
        self.label_4.setGeometry(QtCore.QRect(160, 180, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.dateTimeEdit_2 = QtWidgets.QDateEdit(parent=self)
        self.dateTimeEdit_2.setMinimumDate(date)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(230, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setStyleSheet("color: rgb(203, 203, 203);\n"
"background-color: rgb(72, 72, 72);\n"
"border: none;")
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.label_5 = QtWidgets.QLabel(parent=self)
        self.label_5.setGeometry(QtCore.QRect(60, 210, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(182, 182, 182);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self)
        self.label_6.setGeometry(QtCore.QRect(270, 210, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(182, 182, 182);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self)
        self.label_7.setGeometry(QtCore.QRect(110, 310, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.comboBox = QtWidgets.QComboBox(parent=self)
        self.comboBox.setGeometry(QtCore.QRect(60, 350, 261, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(71, 71, 71);\n"
"color: rgb(197, 197, 197);")
        self.comboBox.setObjectName("comboBox")
        self.dateTimeEdit_3 = QtWidgets.QDateEdit(parent=self)
        self.dateTimeEdit_3.setDate(date)
        self.dateTimeEdit_3.setGeometry(QtCore.QRect(20, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dateTimeEdit_3.setFont(font)
        self.dateTimeEdit_3.setStyleSheet("color: rgb(203, 203, 203);\n"
"background-color: rgb(72, 72, 72);\n"
"border: none;")
        self.dateTimeEdit_3.setObjectName("dateTimeEdit_3")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 420, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(88, 101, 242);\n"
"color: rgb(185, 185, 185);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda: self.appendTask_clicked(lastTask))
        self.appendExecuter(users)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Добавить задачу"))
        self.label_2.setText(_translate("Form", "Добавить задачу"))
        self.label_3.setText(_translate("Form", "Название"))
        self.label_4.setText(_translate("Form", "Дата"))
        self.label_5.setText(_translate("Form", "начало"))
        self.label_6.setText(_translate("Form", "конец"))
        self.label_7.setText(_translate("Form", "Исполняющий"))
        self.pushButton_2.setText(_translate("Form", "Добавить"))

    def appendExecuter(self, executers):
        for i in executers:
            el = f"{i['name']} {i['secondname']} {i['thirstname']}"
            self.exspisok.append(i['id'])
            self.comboBox.addItem(el)

    def appendTask_clicked(self, lastTask):
        if len(self.lineEdit.text().strip()) > 1:
            dateend = f"{str(self.dateTimeEdit_2.date().day())}.{str(self.dateTimeEdit_2.date().month())}.{str(self.dateTimeEdit_2.date().year())}"
            datestart = f"{str(self.dateTimeEdit_3.date().day())}.{str(self.dateTimeEdit_3.date().month())}.{str(self.dateTimeEdit_3.date().year())}"
            taskkeys = {
                "name": self.lineEdit.text(), 
                "datestart": datestart, 
                "dateend": dateend, 
                "guarantor": self.guarantor, 
                "executor": self.exspisok[self.comboBox.currentIndex()]
                }
            self.db.appendTask(name=taskkeys["name"], datestart=taskkeys["datestart"], dateend=taskkeys["dateend"], guarantor=taskkeys["guarantor"], executor=taskkeys["executor"])
            lastTask()
            self.close()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    appendTaskWindow = AppendTaskWindow()
    appendTaskWindow.show()
    app.exec()
