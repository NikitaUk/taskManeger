from PyQt6 import QtCore, QtGui, QtWidgets
import sys
import datetime

class TaskPublishedWidget(QtWidgets.QWidget):
    name = None
    autor = None
    def __init__(self, role, db, tasks = [1, 'Задача', QtCore.QDate(2023, 10, 17), QtCore.QDate(2023, 10, 25), 1, 1, True]):
        super().__init__()
        self.name = tasks[1]
        self.autor = db.getNameUserById(tasks[5])
        self.executer = tasks[4]
        self.guarantor = tasks[5]
        self.date_start = tasks[2]
        self.date_end = tasks[3]
        self.db = db
        self.idTask = tasks[0]
        self.role = role
        self.setupUi()

    def setupUi(self):
        self.setObjectName("taskWidget")
        self.setFixedSize(661, 61)
        self.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 0, 631, 61))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.hbox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setObjectName("hbox")
        self.name_lbl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name_lbl.setFont(font)
        self.name_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.name_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_lbl.setObjectName("name_lbl")
        self.hbox.addWidget(self.name_lbl)
        self.date_lbl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.date_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.date_lbl.setStyleSheet("color: rgb(170, 170, 170);")
        self.date_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.date_lbl.setObjectName("date_lbl")
        self.hbox.addWidget(self.date_lbl)
        if self.role == 1:
            self.autor_lbl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
            self.autor_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
            self.autor_lbl.setStyleSheet("color: rgb(170, 170, 170);")
            self.autor_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.autor_lbl.setObjectName("autor_lbl")
            self.hbox.addWidget(self.autor_lbl)
            self.submit_btn = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
            self.submit_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
            self.submit_btn.setStyleSheet("background-color: rgb(85, 170, 127);\n"
    "color: rgb(30, 30, 30);")
            self.submit_btn.setObjectName("submit_btn")
            self.hbox.addWidget(self.submit_btn)
            self.submit_btn.clicked.connect(self.submit_clicked)
        self.indicator_lbl = QtWidgets.QLabel(parent=self)
        self.indicator_lbl.setGeometry(QtCore.QRect(0, 0, 31, 61))
        self.indicator_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.indicator_lbl.setStyleSheet("background-color: rgb(170, 255, 255);")
        self.indicator_lbl.setText("")
        self.indicator_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.indicator_lbl.setObjectName("indicator_lbl")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("taskWidget", "Form"))
        self.name_lbl.setText(_translate("taskWidget", self.name))
        self.date_lbl.setText(_translate("taskWidget", f"{self.date_start.getDate()[0]}.{self.date_start.getDate()[1]}.{self.date_start.getDate()[2]}-{self.date_end.getDate()[0]}.{self.date_end.getDate()[1]}.{self.date_end.getDate()[2]}"))
        if self.role == 1:
            self.autor_lbl.setText(_translate("taskWidget", self.autor))
            self.submit_btn.setText(_translate("taskWidget", "Готово"))

    def submit_clicked(self):
        today = datetime.date.today()
        self.db.taskComplete(self.idTask, str(today))

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    taskPublishedWidget = TaskPublishedWidget()
    taskPublishedWidget.show()
    app.exec()