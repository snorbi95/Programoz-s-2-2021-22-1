# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab9CqEtyS.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from worker_class import *
import re


class Ui_MainWindow(object):

    workers = []

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 531)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(10, 10, 61, 31))
        font = QFont()
        font.setPointSize(14)
        self.name_label.setFont(font)
        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(70, 19, 451, 21))
        self.id_label = QLabel(self.centralwidget)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(10, 50, 81, 31))
        self.id_label.setFont(font)
        self.address_label = QLabel(self.centralwidget)
        self.address_label.setObjectName(u"address_label")
        self.address_label.setGeometry(QRect(10, 90, 81, 31))
        self.address_label.setFont(font)
        self.phone_label = QLabel(self.centralwidget)
        self.phone_label.setObjectName(u"phone_label")
        self.phone_label.setGeometry(QRect(10, 130, 141, 31))
        self.phone_label.setFont(font)
        self.email_label = QLabel(self.centralwidget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(10, 170, 61, 31))
        self.email_label.setFont(font)
        self.id_input = QLineEdit(self.centralwidget)
        self.id_input.setObjectName(u"id_input")
        self.id_input.setGeometry(QRect(90, 60, 431, 21))
        self.address_input = QLineEdit(self.centralwidget)
        self.address_input.setObjectName(u"address_input")
        self.address_input.setGeometry(QRect(90, 100, 431, 21))
        self.phone_input = QLineEdit(self.centralwidget)
        self.phone_input.setObjectName(u"phone_input")
        self.phone_input.setGeometry(QRect(150, 140, 371, 21))
        self.email_input = QLineEdit(self.centralwidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(70, 180, 451, 21))
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(10, 220, 81, 31))
        self.edit_button = QPushButton(self.centralwidget)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(110, 220, 81, 31))
        self.modify_button = QPushButton(self.centralwidget)
        self.modify_button.setObjectName(u"modify_button")
        self.modify_button.setGeometry(QRect(210, 220, 81, 31))
        self.delete_button = QPushButton(self.centralwidget)
        self.delete_button.setObjectName(u"delete_button")
        self.delete_button.setGeometry(QRect(310, 220, 81, 31))
        self.worker_label = QLabel(self.centralwidget)
        self.worker_label.setObjectName(u"worker_label")
        self.worker_label.setGeometry(QRect(10, 260, 141, 31))
        self.worker_label.setFont(font)
        self.worker_list = QListWidget(self.centralwidget)
        self.worker_list.setObjectName(u"worker_list")
        self.worker_list.setGeometry(QRect(10, 300, 511, 211))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.add_button.clicked.connect(self.add_or_modify_worker)
        self.edit_button.clicked.connect(self.edit_worker)
        self.modify_button.clicked.connect(self.add_or_modify_worker)
        self.delete_button.clicked.connect(self.delete_worker)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Workers", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"ID code:", None))
        self.address_label.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.phone_label.setText(QCoreApplication.translate("MainWindow", u"Phone number:", None))
        self.email_label.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.phone_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+36301234567", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.edit_button.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.modify_button.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.delete_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.worker_label.setText(QCoreApplication.translate("MainWindow", u"List of persons:", None))
    # retranslateUi

    def add_or_modify_worker(self):
        id = int(self.id_input.text())
        name = self.name_input.text()
        address = self.address_input.text()
        phone_number = self.phone_input.text()
        email = self.email_input.text()
        try:
            if len(name) == 0:
                raise MissingDataException('Name')
            if not re.match('^(\+36)\d{8,9}$', phone_number):
                raise PhoneNumberFormatException(phone_number)
            if not re.match('[\w\.-]+@[a-z]{1}[a-z\.-]+(\.[a-z]{2,3})$', email):
                raise EmailFormatException(email)
        except MissingDataException as mde:
            msg = QMessageBox()
            msg.setWindowTitle('Waring!')
            msg.setText(mde.__str__())
            msg.exec_()
        except PhoneNumberFormatException as pnfe:
            msg = QMessageBox()
            msg.setWindowTitle('Waring!')
            msg.setText(pnfe.__str__())
            msg.exec_()
        except EmailFormatException as efe:
            msg = QMessageBox()
            msg.setWindowTitle('Waring!')
            msg.setText(efe.__str__())
            msg.exec_()
        else:
            if self.id_input.isReadOnly():
                for worker in self.workers:
                    if worker.id == id:
                        worker.name = name
                        worker.address = address
                        worker.phone_number = phone_number
                        worker.email = email
                self.print_worker()
                self.save_to_file()
                self.id_input.setReadOnly(False)
            else:
                worker = Worker(id, name, address, phone_number, email)
                if worker not in self.workers:
                    self.workers.append(worker)
                    self.print_worker()
                    self.save_to_file()
            self.clear_input_fields()


    def edit_worker(self):
        if self.worker_list.currentItem():
            text = self.worker_list.currentItem().text()
            data = text.split(',')
            self.id_input.setText(data[0])
            self.name_input.setText(data[1])
            self.address_input.setText(data[2])
            self.phone_input.setText(data[3])
            self.email_input.setText(data[4])
            self.id_input.setReadOnly(True)
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setText('Please select a worker!')
            msg.exec_()

    def delete_worker(self):
        if self.worker_list.currentItem():
            text = self.worker_list.currentItem().text()
            id = int(text.split(',')[0])
            for worker in self.workers:
                if worker.id == id:
                    self.workers.remove(worker)
            self.print_worker()
            self.save_to_file()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setText('Please select a worker!')
            msg.exec_()

    def print_worker(self):
        self.worker_list.clear()
        for worker in self.workers:
            self.worker_list.addItem(worker.__str__())

    def save_to_file(self):
        with open('workers.txt', 'w') as out_file:
            for worker in self.workers:
                print(worker.__str__(), file=out_file)

    def load_database(self):
        with open('workers.txt', 'r') as in_file:
            for line in in_file:
                data = line.split(',')
                id = int(data[0])
                name = data[1]
                address = data[2]
                phone_number = data[3]
                email = data[4].strip()
                worker = Worker(id, name, address, phone_number, email)
                self.workers.append(worker)
        self.print_worker()

    def clear_input_fields(self):
        self.id_input.clear()
        self.name_input.clear()
        self.address_input.clear()
        self.phone_input.clear()
        self.email_input.clear()

import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.load_database()
MainWindow.show()
sys.exit(app.exec_())