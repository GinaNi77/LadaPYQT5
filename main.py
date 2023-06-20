import sys
from PyQt5 import QtWidgets, QtSql
from getpass import getpass
from mysql.connector import connect, Error
from PyQt5.QtWidgets import QDialog, QApplication
import menu, employee_info, customer_info, car_info, service_info, order_info
import config, db_table, db_procedures, db_triggers, create_db
from datetime import date

class Main(QtWidgets.QMainWindow, menu.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def car_info(self):
        self.car_info = CarInfo()
        self.car_info.show()
        self.hide()

    def order_info(self):
        self.order_info = OrderInfo()
        self.order_info.show()
        self.hide()

    def service_info(self):
        self.service_info = ServiceInfo()
        self.service_info.show()
        self.hide()

    def customer_info(self):
        self.customer_info = CustomerInfo()
        self.customer_info.show()
        self.hide()

    def employee_info(self):
        self.employee__info = EmployeeInfo()
        self.employee__info.show()
        self.hide()

    def create_db(self):
        self.create_db = CreateDB()
        self.create_db.show()
        self.hide()

    def init(self):
        self.pushButton.clicked.connect(self.customer_info)
        self.pushButton_2.clicked.connect(self.employee_info)
        self.pushButton_3.clicked.connect(self.car_info)
        self.pushButton_5.clicked.connect(self.service_info)
        self.pushButton_4.clicked.connect(self.order_info)
        self.pushButton_6.clicked.connect(self.create_db)

class CustomerInfo(QtWidgets.QMainWindow, customer_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from customers"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        phone = self.lineEdit_5.text()
        email = self.lineEdit_6.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO customers (first_name, last_name, address, phone, email) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(first_name, last_name, address, phone, email)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from customers where customer_id = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class EmployeeInfo(QtWidgets.QMainWindow, employee_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from employees"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        first_name = self.lineEdit.text()
        last_name = self.lineEdit_3.text()
        position = self.lineEdit_4.text()
        salary = self.lineEdit_5.text()
        hire_date = self.lineEdit_6.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO employees (first_name, last_name, position, salary, hire_date) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(first_name, last_name, position, salary, hire_date, )]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from employees where employee_id = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class CarInfo(QtWidgets.QMainWindow, car_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from cars"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 7):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        brand = self.lineEdit.text()
        model = self.lineEdit_3.text()
        production_year = self.lineEdit_4.text()
        engine_power = self.lineEdit_5.text()
        trunk_volume = self.lineEdit_6.text()
        price = self.lineEdit_7.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO cars (brand, model, production_year, engine_power, trunk_volume, price) VALUES (%s, %s, %s, %s, %s, %s)"
                insert_tuple = [(brand, model, production_year, engine_power, trunk_volume, price)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_4.setText("")
                    self.lineEdit_7.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from cars where car_id = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class CreateDB(QtWidgets.QMainWindow, create_db.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()

    def init(self):
        #назначаем действия по кнопкам
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.create_table)
        self.pushButton_2.clicked.connect(self.create_triggers)
        self.pushButton_3.clicked.connect(self.create_procedures)

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

    def create_table(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
        ) as connection:
            query = db_table.script
            with connection.cursor() as cursor:
                cursor.execute(query)

    def create_procedures(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database = config.db,
        ) as connection:
            query = db_procedures.procedures
            with connection.cursor() as cursor:
                cursor.execute(query)

    def create_triggers(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database = config.db,
        ) as connection:
            query = db_triggers.triggers
            with connection.cursor() as cursor:
                cursor.execute(query)

class OrderInfo(QtWidgets.QMainWindow, order_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from orders"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        customer_id = self.lineEdit.text()
        car_id = self.lineEdit_3.text()
        order_date = self.lineEdit_4.text()
        status = self.lineEdit_5.text()
        total_cost = self.lineEdit_6.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO orders (customer_id, car_id, order_date, status, total_cost) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(customer_id, car_id, order_date, status, total_cost)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from orders where order_id = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

class ServiceInfo(QtWidgets.QMainWindow, service_info.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init()
        self.showdb()

    def init(self):
        self.pushButton_4.clicked.connect(self.back)
        self.pushButton.clicked.connect(self.add)
        self.pushButton_2.clicked.connect(self.delete)   
        
    def showdb(self):
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                select_query = "select * from service"
                with connection.cursor() as cursor:
                    cursor.execute(select_query)
                    result = cursor.fetchall()
                    self.tableWidget.setRowCount(len(result))
                    b = list()
                    for row in result:
                        for i in row:
                            b.append(i)

                    k = 0
                    for j in range(0, len(result)):
                        for i in range(0, 6):
                            self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(b[k])))
                            k += 1

    def add(self):
        car_id = self.lineEdit.text()
        employee_id = self.lineEdit_3.text()
        service_date = self.lineEdit_4.text()
        description = self.lineEdit_5.text()
        cost = self.lineEdit_6.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
            ) as connection:
                insert_query = "INSERT INTO service (car_id, employee_id, service_date, description, cost) VALUES (%s, %s, %s, %s, %s)"
                insert_tuple = [(car_id, employee_id, service_date, description, cost)]
                with connection.cursor() as cursor:
                    cursor.execute(insert_query, insert_tuple[0])
                    connection.commit()
        
                    self.lineEdit.setText("")
                    self.lineEdit_3.setText("")
                    self.lineEdit_5.setText("")
                    self.lineEdit_6.setText("")
                    self.lineEdit_4.setText("")
                    self.showdb()

    def delete(self):
        id = self.lineEdit_2.text()
        with connect(
                host="localhost",
                user=config.user,
                password=config.password,
                database=config.db,
        ) as connection:
            delete_query = "DELETE from service where service_id = %s"
            delete_tuple = [(id,)]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, delete_tuple[0])
                connection.commit()
        
                self.lineEdit_2.setText("")
                self.showdb()

    def back(self):
        self.createDB = Main()
        self.createDB.show()
        self.hide()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    app.exec_()

if __name__ == '__main__':
    main()
