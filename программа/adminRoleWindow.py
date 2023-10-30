from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from tasksWindow import TasksWindow
from staffWindow import StaffWindow

class AdminRoleWindow(QtWidgets.QWidget):
    def __init__(self, user, db):
        super().__init__()
        tasks = db.getTasks(user["idUser"], 1)
        tasksWindow = TasksWindow(db, tasks, user["idUser"])
        staffWindow = StaffWindow(db, user)
        self.setupUi(tasksWindow, staffWindow)
    
    def setupUi(self, tasks, staffs):
        self.setObjectName("Form")
        self.setFixedSize(760, 439)
        self.setStyleSheet("* {\n"
"    background-color: rgb(49, 51, 56);\n"
"}\n"
"QTabBar::tab {\n"
"    background: #16181d;\n"
"    color: #8a8a8a;\n"
"}\n"
"QTabBar::tab:selected {\n"
"    background-color: #2c313f;\n"
"     color: #8a8a8a;\n"
"}\n"
"QLabel {\n"
"    background-color: #23272a;\n"
"    font-size: 22px;\n"
"    padding-left: 5px;\n"
"    color: white;\n"
"}")
        self.tabWidget = QtWidgets.QTabWidget(parent=self)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 801, 441))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("border: none;")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.West)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = tasks
        self.tab.setStyleSheet("border: none;")
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = staffs
        self.tab_2.setStyleSheet("border: none;")
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi()
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Главное окно"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Задачи"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Сотрудники"))

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = AdminRoleWindow()
    mainWindow.show()
    app.exec()
