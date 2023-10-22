from PyQt6 import QtCore, QtGui, QtWidgets
from taskModule.taskPublishedWidget import TaskPublishedWidget
from taskModule.taskComplete import TaskCompleteWidget
import sys

class StaffRoleWindow(QtWidgets.QWidget):
    def __init__(self, user, db):
        super().__init__()
        self.db = db
        self.user = user
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.setFixedSize(731, 379)
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
        self.toolBox = QtWidgets.QToolBox(parent=self)
        self.toolBox.setGeometry(QtCore.QRect(0, 50, 721, 311))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 721, 235))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 721, 235))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.title_lbl = QtWidgets.QLabel(parent=self)
        self.title_lbl.setGeometry(QtCore.QRect(0, 0, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.title_lbl.setFont(font)
        self.title_lbl.setStyleSheet("color: rgb(255, 255, 255);")
        self.title_lbl.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_lbl.setObjectName("title_lbl")
        self.taskMeneger()

        self.retranslateUi()
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Задачи"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Form", "Не выполенные"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Form", "Выполненные"))
        self.title_lbl.setText(_translate("Form", "Мои задачи"))

    def taskMeneger(self):
        tasks = self.db.getTasks(self.user["idUser"], 2)
        if tasks == False:
            self.setEmpty()
        else:
            complete_tasks = []
            not_complete_tasks = []
            for i in tasks:
                if i[6]:
                    complete_tasks.append(i)
                else:
                    not_complete_tasks.append(i)
            if len(complete_tasks) == 0:
                self.setEmpty(nct=1)
            else:
                self.appendTasksComplete(db=self.db, tasks=complete_tasks)
            if len(not_complete_tasks) == 0:
                self.setEmpty(ct=1)
            else:
                self.appendTasksNotComplete(db=self.db, tasks=not_complete_tasks)

    def setEmpty(self, ct = 0, nct = 0):
        if ct == 0:
            vbox = QtWidgets.QVBoxLayout()
            lbl = QtWidgets.QLabel("<center>Вам не поручили задач</center>")
            vbox.addWidget(lbl)
            self.page.setLayout(vbox)
        if nct == 0:
            vbox2 = QtWidgets.QVBoxLayout()
            lbl2 = QtWidgets.QLabel("<center>Вы не выполняли еще задачи</center>")       
            vbox2.addWidget(lbl2)
            self.page_2.setLayout(vbox2)

    def appendTasksComplete(self, db, tasks):
        tasks_widgets = []
        for i in tasks:
            tasks_widgets.append(TaskCompleteWidget(2, db, i))
        vbox = QtWidgets.QVBoxLayout()
        for i in tasks_widgets:
            vbox.addWidget(i)
        self.page_2.setLayout(vbox)


    def appendTasksNotComplete(self, db, tasks):
        tasks_widgets = []
        for i in tasks:
            tasks_widgets.append(TaskPublishedWidget(2, db, i))
        vbox = QtWidgets.QVBoxLayout()
        for i in tasks_widgets:
            vbox.addWidget(i)
        self.page.setLayout(vbox)   

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    taskRoleTwo = StaffRoleWindow()
    taskRoleTwo.show()
    app.exec()