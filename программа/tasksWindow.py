from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from taskModule.taskComplete import TaskCompleteWidget
from taskModule.taskPublishedWidget import TaskPublishedWidget
from appendTaskWindow import AppendTaskWindow

class TasksWindow(QtWidgets.QWidget):
    def __init__(self, db, task, guarantor):
        super().__init__()
        self.db = db
        self.guarantor = guarantor
        self.setupUi(task)

    def setupUi(self, task):
        self.setObjectName("Form")
        self.setFixedSize(735, 447)
        self.setStyleSheet("background-color: rgb(49, 51, 56);")
        self.appendTask_btn = QtWidgets.QPushButton(parent=self)
        self.appendTask_btn.setGeometry(QtCore.QRect(570, 400, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.appendTask_btn.setFont(font)
        self.appendTask_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.OpenHandCursor))
        self.appendTask_btn.setStyleSheet("background-color: rgb(88, 101, 242);\n"
"color: rgb(185, 185, 185);")
        self.appendTask_btn.setObjectName("appendTask_btn")
        self.title = QtWidgets.QLabel(parent=self)
        self.title.setGeometry(QtCore.QRect(0, 10, 731, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(255, 255, 255);")
        self.title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title.setObjectName("title")
        self.toolBox = QtWidgets.QToolBox(parent=self)
        self.toolBox.setGeometry(QtCore.QRect(0, 60, 721, 311))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.toolBox.setFont(font)
        self.toolBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolBox.setObjectName("toolBox")
        self.notComplete_page = QtWidgets.QWidget()
        self.notComplete_page.setGeometry(QtCore.QRect(0, 0, 721, 235))
        self.notComplete_page.setObjectName("notComplete_page")
        self.toolBox.addItem(self.notComplete_page, "")
        self.complete_page = QtWidgets.QWidget()
        self.complete_page.setGeometry(QtCore.QRect(0, 0, 721, 235))
        self.complete_page.setObjectName("complete_page")
        self.toolBox.addItem(self.complete_page, "")
        self.taskMeneger(task)
        self.appendTask_btn.clicked.connect(self.appendTask_btn_clicked)

        self.retranslateUi()
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Задачи"))
        self.appendTask_btn.setText(_translate("Form", "Добавить задачу"))
        self.title.setText(_translate("Form", "Все задачи"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.notComplete_page), _translate("Form", "Не выполенные"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.complete_page), _translate("Form", "Выполненные"))

    def taskMeneger(self, tasks):
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
            lbl = QtWidgets.QLabel("<center>Нет выполненных задач</center>")
            vbox.addWidget(lbl)
            self.complete_page.setLayout(vbox)
        if nct == 0:
            vbox2 = QtWidgets.QVBoxLayout()
            lbl2 = QtWidgets.QLabel("<center>Вы не запланировали новые задачи</center>")       
            vbox2.addWidget(lbl2)
            self.notComplete_page.setLayout(vbox2)
            
    def appendTasksComplete(self, db, tasks):
        tasks_widgets = []
        for i in tasks:
            tasks_widgets.append(TaskCompleteWidget(1, db, i))
        vbox = QtWidgets.QVBoxLayout()
        for i in tasks_widgets:
            vbox.addWidget(i)
        self.complete_page.setLayout(vbox)

    def appendTasksNotComplete(self, db, tasks):
        tasks_widgets = []
        for i in tasks:
            tasks_widgets.append(TaskPublishedWidget(1, db, i))
        vbox = QtWidgets.QVBoxLayout()
        for i in tasks_widgets:
            vbox.addWidget(i)
        self.notComplete_page.setLayout(vbox)

    def appendTask_btn_clicked(self):
        self.appendTaskWindow = AppendTaskWindow(self.db, self.guarantor, self.lastTask)
        self.appendTaskWindow.show()
    
    def lastTask(self):
        l = self.notComplete_page.layout()
        l.addWidget(TaskPublishedWidget(1, self.db, self.db.getLastTask()[0]))
    
    def lastTaskComplete(self):
        l = self.complete_page.layout()
        TaskCompleteWidget(1, self.db)
        #l.addWidget(TaskPublishedWidget(1, self.db, self.db.getLastTask()[0]))

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv)
    tasksWindow = TasksWindow()
    tasksWindow.show()
    app.exec()
