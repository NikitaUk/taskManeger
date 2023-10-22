from PyQt6 import QtCore, QtGui, QtWidgets
import sys

class TaskCompleteWidget(QtWidgets.QWidget):
    def __init__(self, role, db, tasks = [1, 'Задача', QtCore.QDate(2023, 10, 17), QtCore.QDate(2023, 10, 25), 1, 1, True, QtCore.QDate(2023, 10, 20)]):
        super().__init__()
        self.name = tasks[1]
        self.autor = db.getNameUserById(tasks[5])
        self.days = tasks[2].daysTo(tasks[7])
        self.executer = tasks[5]
        self.guarantor = tasks[4]
        self.role = role
        self.setupUi(1)

    def setupUi(self, r):
        self.setObjectName("task")
        self.setFixedSize(661, 61)
        self.taskWidget = QtWidgets.QWidget(parent=self)
        self.taskWidget.setGeometry(QtCore.QRect(0, 0, 661, 61))
        self.taskWidget.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.taskWidget.setObjectName("taskWidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(parent=self.taskWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 0, 631, 61))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.hbox = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.hbox.setContentsMargins(0, 0, 0, 0)
        self.hbox.setObjectName("hbox")
        self.name_lbl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name_lbl.setFont(font)
        self.name_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.name_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.name_lbl.setObjectName("name_lbl")
        self.hbox.addWidget(self.name_lbl)
        if self.role == 1:
            self.autor_lbl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
            self.autor_lbl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
            self.autor_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
            self.autor_lbl.setStyleSheet("color: rgb(255, 255, 255);")
            self.autor_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.autor_lbl.setObjectName("autor_lbl")
            self.hbox.addWidget(self.autor_lbl)
        self.days_lbl = QtWidgets.QLabel(parent=self.horizontalLayoutWidget_2)
        self.days_lbl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.days_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.days_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.days_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.days_lbl.setObjectName("days_lbl")
        self.hbox.addWidget(self.days_lbl)
        self.indicator_lbl = QtWidgets.QLabel(parent=self.taskWidget)
        self.indicator_lbl.setGeometry(QtCore.QRect(0, 0, 31, 61))
        self.indicator_lbl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.indicator_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.indicator_lbl.setStyleSheet("background-color: rgb(60, 181, 88);")
        self.indicator_lbl.setText("")
        self.indicator_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.indicator_lbl.setObjectName("indicator_lbl")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("task", "Form"))
        self.name_lbl.setText(_translate("task", self.name))
        if self.role == 1:
            self.autor_lbl.setText(_translate("task", self.autor))
        days = ""
        if self.days == 0:
            days = "сегодня"
        elif self.days == 1:
            days = f"за 1 день"
        elif self.days == 2 or 3 or 4:
            days = f"за {self.days} дня"
        else:
            days = f"за {self.days} дней"
        self.days_lbl.setText(_translate("task", f"Выполнено {days}"))

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    taskCompleteWidget = TaskCompleteWidget()
    taskCompleteWidget.show()
    app.exec()