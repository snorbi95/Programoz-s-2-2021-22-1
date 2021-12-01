# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minta_zh_guieIhNeG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from student_class import *
import re


class Ui_MainWindow(object):

    student_list = []

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(487, 731)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 101, 41))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 131, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 101, 41))
        self.label_3.setFont(font)
        self.name_input = QLineEdit(self.centralwidget)
        self.name_input.setObjectName(u"name_input")
        self.name_input.setGeometry(QRect(70, 20, 391, 20))
        self.neptun_input = QLineEdit(self.centralwidget)
        self.neptun_input.setObjectName(u"neptun_input")
        self.neptun_input.setGeometry(QRect(140, 60, 321, 20))
        self.email_input = QLineEdit(self.centralwidget)
        self.email_input.setObjectName(u"email_input")
        self.email_input.setGeometry(QRect(90, 100, 371, 20))
        self.student_add = QPushButton(self.centralwidget)
        self.student_add.setObjectName(u"student_add")
        self.student_add.setGeometry(QRect(60, 150, 91, 41))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.student_add.setFont(font1)
        self.student_delete = QPushButton(self.centralwidget)
        self.student_delete.setObjectName(u"student_delete")
        self.student_delete.setGeometry(QRect(310, 150, 91, 41))
        self.student_delete.setFont(font1)
        self.student_list_widget = QListWidget(self.centralwidget)
        self.student_list_widget.setObjectName(u"student_list_widget")
        self.student_list_widget.setGeometry(QRect(10, 210, 461, 191))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 410, 101, 41))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 410, 111, 41))
        self.label_5.setFont(font)
        self.subject_input = QLineEdit(self.centralwidget)
        self.subject_input.setObjectName(u"subject_input")
        self.subject_input.setGeometry(QRect(120, 420, 113, 20))
        self.mark_input = QLineEdit(self.centralwidget)
        self.mark_input.setObjectName(u"mark_input")
        self.mark_input.setGeometry(QRect(360, 420, 113, 20))
        self.marks_list_widget = QListWidget(self.centralwidget)
        self.marks_list_widget.setObjectName(u"marks_list_widget")
        self.marks_list_widget.setGeometry(QRect(10, 510, 461, 191))
        self.mark_add = QPushButton(self.centralwidget)
        self.mark_add.setObjectName(u"mark_add")
        self.mark_add.setGeometry(QRect(180, 460, 121, 41))
        self.mark_add.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.student_add.clicked.connect(self.add_student)
        self.student_delete.clicked.connect(self.delete_student)
        self.student_list_widget.itemClicked.connect(self.student_clicked)
        self.mark_add.clicked.connect(self.add_mark)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"N\u00e9v:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Neptun k\u00f3d:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.student_add.setText(QCoreApplication.translate("MainWindow", u"Hozzáad", None))
        self.student_delete.setText(QCoreApplication.translate("MainWindow", u"Töröl", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tant\u00e1rgy:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00c9rdemjegy:", None))
        self.mark_add.setText(QCoreApplication.translate("MainWindow", u"Jegy Hozzáad", None))
    # retranslateUi

    def add_student(self):
        name = self.name_input.text()
        neptun = self.neptun_input.text()
        email = self.email_input.text()
        student = Student(name, neptun, email)
        try:
            if not re.match('[A-Z0-9]{6}$', neptun):
                raise NeptunCodeFormatException(neptun)
        except NeptunCodeFormatException as ncfe:
            msg = QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setText(ncfe.__str__())
            msg.exec_()
        else:
            if student not in self.student_list:
                self.student_list.append(student)
                self.print_students()
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Warning!')
                msg.setText('A megadott neptun kód már létezik!')
                msg.exec_()

    def delete_student(self):
        if self.student_list_widget.currentItem():
            neptun = self.student_list_widget.currentItem().text().split(',')[1]
            print(neptun)
            for student in self.student_list:
                if student.neptun == neptun:
                    self.student_list.remove(student)
            self.print_students()
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setText('Kérem válaszzon ki egy tanulót törlésre!')
            msg.exec_()

    def add_mark(self):
        if self.student_list_widget.currentItem():
            neptun = self.student_list_widget.currentItem().text().split(',')[1]
            subject = self.subject_input.text()
            mark = self.mark_input.text()
            for student in self.student_list:
                if student.neptun == neptun:
                    student.marks[subject] = mark
                    self.marks_list_widget.addItem(f'{subject} - {mark}')
        else:
            msg = QMessageBox()
            msg.setWindowTitle('Warning!')
            msg.setText('Kérem válaszzon ki egy tanulót a jegy hozzáadásához!')
            msg.exec_()

    def student_clicked(self, item):
        self.marks_list_widget.clear()
        neptun = item.text().split(',')[1]
        for student in self.student_list:
            if student.neptun == neptun:
                for key, value in student.marks.items():
                    self.marks_list_widget.addItem(f'{key} - {value}')

    def print_students(self):
        self.student_list_widget.clear()
        for worker in self.student_list:
            self.student_list_widget.addItem(worker.__str__())


import sys
app = QApplication()
main_window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(main_window)
main_window.show()
sys.exit(app.exec_())