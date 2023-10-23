from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5 import QtCore

class Database():
    def __init__(self):
        self.db = QSqlDatabase.addDatabase("QPSQL")
        self.db.setDatabaseName("task")
        self.db.setUserName("postgres")
        self.db.setPassword("student")
        self.db.setPort(5432)
        self.db.setHostName("localhost")
        self.query = QSqlQuery()
        self.db.open()

    def login(self, l, p):
        self.query.exec(f"SELECT * FROM public.account INNER JOIN public.user ON public.account.user_id = public.user.id WHERE login = '{l}' AND password = '{p}'")
        if self.query.first():
            values = []
            j = 0
            while True:
                if self.query.isNull(j):
                    break
                else:
                    values.append(self.query.value(j))
                    j += 1
            return {
                "idAc": values[0],
                "login": values[1],
                "password": values[2],
                "idUser": values[4],
                "name": values[5],
                "secondname": values[6],
                "thirstname": values[7],
                "pos": values[8],
                "roleId": values[9],
            }
        else:
            return False
        
    def getTasks(self, staff_id, role):
        self.query.clear()
        if role == 1:
            self.query.exec(f"SELECT * FROM public.task WHERE guarantor = '{staff_id}'")
        elif role == 2:
            self.query.exec(f"SELECT * FROM public.task WHERE executor = '{staff_id}'")
        if self.query.first():
            values = []
            while True:
                value = []
                j = 0
                while True:
                    if self.query.isNull(j):
                        values.append(value)
                        break
                    else:
                        value.append(self.query.value(j))
                        j += 1
                if self.query.next():
                    continue
                else:
                    break
            return values
        else:
            return False
        
    def getNameUserById(self, id):
        self.query.clear()
        self.query.exec(f"SELECT * FROM public.user WHERE id = '{id}'")
        if self.query.first():
            values = []
            while True:
                values.append(self.query.value(1))
                if self.query.next() == False:
                    break
            return values[0]
        else:
            return False
        
    def taskComplete(self, id, date):
        self.query.clear()
        self.query.exec(f"UPDATE public.task SET iscomplete = 'true', datecomplete = '{date}' WHERE id = '{id}'")

    def getStaffsNames(self):
        self.query.clear()
        self.query.exec(f"SELECT id, name, secondname, thirstname FROM public.user")
        if self.query.first():
            value = []
            while True:
                values = {
                    "id": self.query.value(0),
                    "name": self.query.value(1),
                    "secondname": self.query.value(2),
                    "thirstname": self.query.value(3),
                }
                value.append(values)
                if self.query.next() == False:
                    break
            return value
        else:
            return False
        
    def appendTask(self, name, datestart, dateend, guarantor, executor):
        self.query.clear()
        self.query.exec(f"INSERT INTO public.task (name, datestart, dateend, guarantor, executor, iscomplete) VALUES ('{name}', '{datestart}', '{dateend}', '{guarantor}', '{executor}', 'false')")

    def getStaffs(self):
        query = QSqlQueryModel()
        query.setQuery("SELECT public.user.id, public.user.name, secondname, thirstname, position, role.name FROM public.user INNER JOIN public.role ON public.user.role_id = role.id")
        query.setHeaderData(0, QtCore.Qt.Orientation.Horizontal, "№")
        query.setHeaderData(1, QtCore.Qt.Orientation.Horizontal, "Имя")
        query.setHeaderData(2, QtCore.Qt.Orientation.Horizontal, "Фамилия")
        query.setHeaderData(3, QtCore.Qt.Orientation.Horizontal, "Отчество")
        query.setHeaderData(4, QtCore.Qt.Orientation.Horizontal, "Должность")
        query.setHeaderData(5, QtCore.Qt.Orientation.Horizontal, "Роль")
        return query
    
    def updateUser(self, idUs, idAc, n, sn, tn, lg, psw):
        self.query.clear()
        self.query.exec(f"UPDATE public.user SET name = '{n}', secondname = '{sn}', thirstname = '{tn}' WHERE id = '{idUs}'")
        self.query.clear()
        self.query.exec(f"UPDATE public.account SET login = '{lg}', password = '{psw}' WHERE id = '{idAc}'")

    def closeDb(self):
        self.db.close()

    def appendStaff(self, name, sname, tname, pos, role, login, password):
        self.query.clear()
        self.query.exec(f"INSERT INTO public.user (name, secondname, thirstname, position, role_id) VALUES ('{name}', '{sname}', '{tname}', '{pos}', '{role}')")
        idUs = self.query.lastInsertId()
        self.query.clear()
        self.query.exec(f"INSERT INTO public.account (login, password, user_id) VALUES ('{login}', '{password}', '{idUs}')")

    def getLastTask(self):
        self.query.clear()
        self.query.exec(f"SELECT * FROM public.task ORDER BY id DESC LIMIT 1")
        if self.query.first():
            values = []
            while True:
                value = []
                j = 0
                while True:
                    if self.query.isNull(j):
                        values.append(value)
                        break
                    else:
                        value.append(self.query.value(j))
                        j += 1
                if self.query.next():
                    continue
                else:
                    break
            return values
        else:
            return False
