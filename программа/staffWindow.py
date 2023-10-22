from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from appendStaffWindow import AppendStaffWindow
from profile import ProfileWindow

class StaffWindow(QtWidgets.QWidget):
    def __init__(self, db, user):
        super().__init__()
        self.db = db
        self.user = user
        self.setupUi(db)

    def setupUi(self, db):
        self.setObjectName("staffWindow")
        self.resize(735, 447)
        self.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.title_lbl = QtWidgets.QLabel(parent=self)
        self.title_lbl.setGeometry(QtCore.QRect(230, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color: rgb(255, 255, 255); background-color: none;")
        self.title_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.profile_lbl = QtWidgets.QLabel(parent=self)
        self.profile_lbl.setGeometry(QtCore.QRect(10, 50, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.profile_lbl.setFont(font)
        self.profile_lbl.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.profile_lbl.setStyleSheet("color: rgb(255, 255, 255); background-color: none;")
        self.profile_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.profile_lbl.setObjectName("profile_lbl")
        self.profile_btn = QtWidgets.QPushButton(parent=self)
        self.profile_btn.setGeometry(QtCore.QRect(10, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.profile_btn.setFont(font)
        self.profile_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.profile_btn.setStyleSheet("background-color: rgb(88, 101, 242);\n"
"color: rgb(185, 185, 185);")
        self.profile_btn.setObjectName("profile_btn")
        self.staff_lbl = QtWidgets.QLabel(parent=self)
        self.staff_lbl.setGeometry(QtCore.QRect(10, 160, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.staff_lbl.setFont(font)
        self.staff_lbl.setStyleSheet("color: rgb(255, 255, 255); background-color: none;")
        self.staff_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.staff_lbl.setObjectName("staff_lbl")
        self.append_btn = QtWidgets.QPushButton(parent=self)
        self.append_btn.setGeometry(QtCore.QRect(180, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.append_btn.setFont(font)
        self.append_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.append_btn.setStyleSheet("background-color: rgb(88, 101, 242);\n"
"color: rgb(185, 185, 185);")
        self.append_btn.setObjectName("append_btn")
        self.tableView = QtWidgets.QTableView(parent=self)
        self.tableView.setGeometry(QtCore.QRect(20, 210, 701, 221))
        self.tableView.setFont(font)
        self.tableView.setStyleSheet(
"QTableView::item  {"
    "color: rgb(213, 210, 216);\n"
    "background-color: #29307f;"
"}"
".QHeaderView::section {\n"
        "background-color: #484f9d;\n"
        "color: rgb(195, 195, 195);\n"
"}\n")
        self.tableView.setObjectName("tableView")
        self.setStaffs(db)
        self.append_btn.clicked.connect(self.append_btn_clicked)
        self.profile_btn.clicked.connect(self.profile_btn_clicked)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("staffWindow", "Сотрудники"))
        self.title_lbl.setText(_translate("staffWindow", "Сотрудники"))
        self.profile_lbl.setText(_translate("staffWindow", "Мой профиль"))
        self.profile_btn.setText(_translate("staffWindow", "Изменить"))
        self.staff_lbl.setText(_translate("staffWindow", "Сотрудники"))
        self.append_btn.setText(_translate("staffWindow", "Добавить"))

    def setStaffs(self, db):
        self.tableView.setModel(db.getStaffs())
        self.tableView.verticalHeader().setVisible(False)
        self.tableView.setColumnWidth(5, 150)
        self.tableView.setColumnWidth(4, 150)
        self.tableView.setColumnWidth(0, 50)

    def append_btn_clicked(self):
        self.appendStaffWindow = AppendStaffWindow(self.db)
        self.appendStaffWindow.show()

    def profile_btn_clicked(self):
        self.profile = ProfileWindow(self.db, self.user)
        self.profile.show()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    staffWindow = StaffWindow()
    staffWindow.show()
    app.exec()