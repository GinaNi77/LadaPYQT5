from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 400)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

         # кнопка для возвращения на предыдущую форму 

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 340, 111, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
         # таблица
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 600, 300))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnWidth(4,150)
        self.tableWidget.setColumnWidth(5,150)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)

         # заголовки

        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        self.label_0.setGeometry(QtCore.QRect(650, 10, 200, 30))
        self.label_0.setObjectName("label")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(880, 10, 200, 30))
        self.label_8.setObjectName("label")

         # поля ввода для добавления данных в бд
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(650, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 45, 100, 16))
        self.label.setObjectName("label")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(650, 115, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(650, 95, 100, 16))
        self.label_3.setObjectName("label")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(650, 165, 113, 20))
        self.lineEdit_4.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(650, 140, 100, 16))
        self.label_4.setObjectName("label")

        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(650, 215, 113, 20))
        self.lineEdit_5.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(650, 190, 100, 16))
        self.label_5.setObjectName("label")

        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(650, 265, 113, 20))
        self.lineEdit_6.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(650, 240, 100, 16))
        self.label_6.setObjectName("label")

        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(650, 315, 113, 20))
        self.lineEdit_7.setObjectName("lineEdit")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(650, 290, 100, 16))
        self.label_7.setObjectName("label")

        # кнопка для добавления данных в бд
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(650, 355, 111, 23))
        self.pushButton.setObjectName("pushButton")

        # кнопка для удаления данных из бд
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(880, 110, 111, 23))
        self.pushButton_2.setObjectName("pushButton_2")

        # поле для ввода номера для удаления данных из бд
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(880, 70, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 45, 61, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Машины"))
        
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Код машины"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Марка"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Год выпуска"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Мощность двигателя"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Объем багажника"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Цена"))

        self.label_0.setText(_translate("MainWindow", "Добавление машины"))
        self.label_0.setFont(QFont('Arial', 14))

        self.label_8.setText(_translate("MainWindow", "Удаление машины"))
        self.label_8.setFont(QFont('Arial', 14))

        self.label.setText(_translate("MainWindow", "Марка"))
        self.label_3.setText(_translate("MainWindow", "Модель"))
        self.label_4.setText(_translate("MainWindow", "Год выпуска"))
        self.label_5.setText(_translate("MainWindow", "Мощность двигателя"))
        self.label_6.setText(_translate("MainWindow", "Объем багажника"))
        self.label_7.setText(_translate("MainWindow", "Цена"))
        self.pushButton.setText(_translate("MainWindow", "Добавить"))

        self.label_2.setText(_translate("MainWindow", "Код"))
        self.pushButton_2.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_4.setText(_translate("MainWindow", "Назад"))
        
