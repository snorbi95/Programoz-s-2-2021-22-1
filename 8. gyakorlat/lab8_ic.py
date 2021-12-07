# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab8lsxorC.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import lab6


class Ui_MainWindow(object):

    train_dict = dict()

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(609, 586)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.train_label = QLabel(self.centralwidget)
        self.train_label.setObjectName(u"train_label")
        self.train_label.setGeometry(QRect(50, 30, 51, 21))
        font = QFont()
        font.setPointSize(10)
        self.train_label.setFont(font)
        self.train_list = QListWidget(self.centralwidget)
        self.train_list.setObjectName(u"train_list")
        self.train_list.setGeometry(QRect(50, 60, 521, 151))
        self.stops_label = QLabel(self.centralwidget)
        self.stops_label.setObjectName(u"stops_label")
        self.stops_label.setGeometry(QRect(50, 230, 51, 21))
        self.stops_label.setFont(font)
        self.stops_list = QListWidget(self.centralwidget)
        self.stops_list.setObjectName(u"stops_list")
        self.stops_list.setGeometry(QRect(50, 260, 521, 161))
        self.id_label = QLabel(self.centralwidget)
        self.id_label.setObjectName(u"id_label")
        self.id_label.setGeometry(QRect(50, 440, 51, 21))
        self.id_label.setFont(font)
        self.id_input = QLineEdit(self.centralwidget)
        self.id_input.setObjectName(u"id_input")
        self.id_input.setGeometry(QRect(110, 440, 131, 21))
        self.from_label = QLabel(self.centralwidget)
        self.from_label.setObjectName(u"from_label")
        self.from_label.setGeometry(QRect(50, 480, 51, 21))
        self.from_label.setFont(font)
        self.from_input = QLineEdit(self.centralwidget)
        self.from_input.setObjectName(u"from_input")
        self.from_input.setGeometry(QRect(110, 480, 131, 21))
        self.name_label = QLabel(self.centralwidget)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(370, 440, 51, 21))
        self.name_label.setFont(font)
        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(440, 440, 131, 21))
        self.to_label = QLabel(self.centralwidget)
        self.to_label.setObjectName(u"to_label")
        self.to_label.setGeometry(QRect(380, 480, 51, 21))
        self.to_label.setFont(font)
        self.to_input = QLineEdit(self.centralwidget)
        self.to_input.setObjectName(u"to_input")
        self.to_input.setGeometry(QRect(440, 480, 131, 21))
        self.load_trains_button = QPushButton(self.centralwidget)
        self.load_trains_button.setObjectName(u"load_trains_button")
        self.load_trains_button.setGeometry(QRect(50, 530, 111, 41))
        self.add_train_button = QPushButton(self.centralwidget)
        self.add_train_button.setObjectName(u"add_train_button")
        self.add_train_button.setGeometry(QRect(460, 530, 111, 41))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.add_train_button.clicked.connect(self.add_new_train)
        self.load_trains_button.clicked.connect(self.load_trains)
        self.train_list.itemClicked.connect(self.load_stops)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.train_label.setText(QCoreApplication.translate("MainWindow", u"Trains:", None))
        self.stops_label.setText(QCoreApplication.translate("MainWindow", u"Stops:", None))
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.from_label.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.to_label.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.load_trains_button.setText(QCoreApplication.translate("MainWindow", u"Load trains", None))
        self.add_train_button.setText(QCoreApplication.translate("MainWindow", u"Add new train", None))
    # retranslateUi

    def add_new_train(self):
        id = self.id_input.text()
        name = self.name_input.text()
        arrival = self.from_input.text()
        destination = self.to_input.text()
        ic = lab6.IC(id, name, arrival, destination)
        if ic.get_id() not in self.train_dict:
            self.train_dict[ic.get_id()] = ic
            self.train_list.addItem(f'{ic.get_id()} - {ic.get_name()}')

    def load_trains(self):
        filename, _ = QFileDialog.getOpenFileName(None, 'Select file...', '*.txt')
        with open(filename, 'r') as in_file:
            for line in in_file:
                data = line.split(';')
                id = int(data[0])
                name = data[1]
                arrival = data[2]
                destination = data[3].rstrip()
                ic = lab6.IC(id, name, arrival, destination)
                if ic.get_id() not in self.train_dict:
                    self.train_dict[ic.get_id()] = ic
                    self.train_list.addItem(f'{ic.get_id()} - {ic.get_name()}')

    def load_stops(self, item):
        self.stops_list.clear()
        data = item.text()
        id = int(data.split(' ')[0])
        for stop in self.train_dict[id].get_stops():
            self.stops_list.addItem(stop.__str__())


import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())