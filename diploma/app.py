import sys
import json

from typing import Optional, Union, List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from copy import deepcopy
from random import randint as r
from PIL import Image
from pathlib import Path
from dataclasses import dataclass, field

from experiments.experiments import signal_thread


class DataApp:
    with open("../diploma/experiments/data.json", 'r') as f:
        json_data = json.load(f)
    data = json_data

class Ui_choosing_variables(object):
    def setupUi(self, choosing_variables):
        choosing_variables.setObjectName("choosing_variables")
        choosing_variables.resize(812, 404)
        font = QtGui.QFont()
        font.setPointSize(8)
        choosing_variables.setFont(font)
        self.centralwidget = QtWidgets.QWidget(choosing_variables)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 327, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, -10, 811, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-30, 50, 1061, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(465, 60, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(390, 60, 20, 265))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-40, 315, 1061, 21))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 130, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(90, 130, 41, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 170, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 170, 41, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 210, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 250, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(430, 130, 301, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(430, 170, 381, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(430, 210, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(430, 250, 291, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(98, 210, 41, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(98, 250, 41, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(460, 130, 41, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(460, 170, 41, 21))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(470, 210, 41, 21))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_8.setGeometry(QtCore.QRect(470, 250, 41, 21))
        self.lineEdit_8.setObjectName("lineEdit_8")
        choosing_variables.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(choosing_variables)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        choosing_variables.setMenuBar(self.menubar)

        self.retranslateUi(choosing_variables)
        QtCore.QMetaObject.connectSlotsByName(choosing_variables)

    def retranslateUi(self, choosing_variables):
        _translate = QtCore.QCoreApplication.translate
        choosing_variables.setWindowTitle(_translate("choosing_variables", "chosing_variables"))
        self.pushButton.setText(_translate("choosing_variables", "Далее"))
        self.label.setText(_translate("choosing_variables", "Задать переменные"))
        self.label_2.setText(_translate("choosing_variables", "Для матрицы"))
        self.label_3.setText(_translate("choosing_variables", "Для Генетического Алгоритма"))
        self.label_4.setText(_translate("choosing_variables", "m =         количество заданий."))
        self.label_5.setText(_translate("choosing_variables", "n =          количество процессоров."))
        self.label_6.setText(_translate("choosing_variables", "T1 =          левая граница задания."))
        self.label_7.setText(_translate("choosing_variables", "T2 =          правая граница задания."))
        self.label_8.setText(_translate("choosing_variables", "z =          количество особей в поколении."))
        self.label_9.setText(_translate("choosing_variables", "k =          количество повторов для выхода из цикла."))
        self.label_10.setText(_translate("choosing_variables", "Pk =           вероятность кроссовера в %."))
        self.label_11.setText(_translate("choosing_variables", "Pm =          вероятность мутации в %."))
        self.lineEdit.setText(_translate("choosing_variables", "10"))
        self.lineEdit_2.setText(_translate("choosing_variables", "5"))
        self.lineEdit_3.setText(_translate("choosing_variables", "20"))
        self.lineEdit_4.setText(_translate("choosing_variables", "30"))
        self.lineEdit_5.setText(_translate("choosing_variables", "100"))
        self.lineEdit_6.setText(_translate("choosing_variables", "30"))
        self.lineEdit_7.setText(_translate("choosing_variables", "99"))
        self.lineEdit_8.setText(_translate("choosing_variables", "99"))


class Ui_generate_matrix(object):
    def setupUi(self, generate_matrix):
        generate_matrix.setObjectName("generate_matrix")
        generate_matrix.resize(812, 398)
        font = QtGui.QFont()
        font.setPointSize(8)
        generate_matrix.setFont(font)
        self.centralwidget = QtWidgets.QWidget(generate_matrix)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 120, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 300, 120, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 300, 120, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(30, 10, 401, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(414, 5, 391, 341))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, -10, 20, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        generate_matrix.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(generate_matrix)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        generate_matrix.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(generate_matrix)
        # self.statusbar.setObjectName("statusbar")
        # generate_matrix.setStatusBar(self.statusbar)

        self.retranslateUi(generate_matrix)
        QtCore.QMetaObject.connectSlotsByName(generate_matrix)

    def retranslateUi(self, generate_matrix):
        _translate = QtCore.QCoreApplication.translate
        generate_matrix.setWindowTitle(_translate("generate_matrix", "generate_matrix"))
        self.pushButton.setText(_translate("generate_matrix", "Готовый вариант"))
        self.pushButton_2.setText(_translate("generate_matrix", "Новая матрица"))
        self.pushButton_3.setText(_translate("generate_matrix", "Вернуться"))
        self.label.setText(_translate("generate_matrix", "Использовать готовую матрицу или сгенерировать новую?"))


class Ui_number_of_repetitons(object):
    def setupUi(self, number_of_repetitons):
        self.global_data = DataApp()
        number_of_repetitons.setObjectName("number_of_repetitons")
        number_of_repetitons.resize(812, 398)
        font = QtGui.QFont()
        font.setPointSize(8)
        number_of_repetitons.setFont(font)
        self.centralwidget = QtWidgets.QWidget(number_of_repetitons)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-50, 300, 901, 121))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(414, 5, 391, 341))
        font = QtGui.QFont()
        font.setPointSize(self.global_data.data["ui_matrix_size"])
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, -50, 20, 411))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 240, 61, 21))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        number_of_repetitons.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(number_of_repetitons)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        number_of_repetitons.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(number_of_repetitons)
        #self.statusbar.setObjectName("statusbar")
        # number_of_repetitons.setStatusBar(self.statusbar)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(85, 310, 101, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        #self.pushButton_2.setFont(font1)
        # self.pushButton_2.setWindowIcon(QtGui.QIcon('../diploma/experiments/back1.png'))
        # self.pushButton_2.setIconSize(QSize(101, 28))
        self.pushButton_2.setGeometry(QtCore.QRect(215, 310, 101, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(number_of_repetitons)
        QtCore.QMetaObject.connectSlotsByName(number_of_repetitons)

    def retranslateUi(self, number_of_repetitons):
        _translate = QtCore.QCoreApplication.translate
        number_of_repetitons.setWindowTitle(_translate("number_of_repetitons", "NumberOfRepeats"))
        self.label.setText(_translate("number_of_repetitons", "Задайте количество повторов генетического алгоритма"))
        self.label_2.setText(_translate("number_of_repetitons", f"{self.global_data.data['matrix']}"))
        self.pushButton.setText(_translate("number_of_repetitions", "Далее"))
        self.pushButton_2.setText(_translate("number_of_repetitions", "Вернуться"))
        self.lineEdit.setText(_translate("number_of_repetitons", "100"))


class Ui_chose_of_one_or_all_methods(object):
    def setupUi(self, chose_of_one_or_all_methods):
        self.global_data = DataApp
        chose_of_one_or_all_methods.setObjectName("GenethicAlgorythm")
        chose_of_one_or_all_methods.resize(812, 398)
        font = QtGui.QFont()
        font.setPointSize(8)
        chose_of_one_or_all_methods.setFont(font)
        self.centralwidget = QtWidgets.QWidget(chose_of_one_or_all_methods)
        self.centralwidget.setObjectName("centralwidget")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(410, -50, 20, 411))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 300, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 300, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 300, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 281))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(414, 5, 391, 341))
        font = QtGui.QFont()
        font.setPointSize(self.global_data.data['ui_matrix_size'])
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        chose_of_one_or_all_methods.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chose_of_one_or_all_methods)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        chose_of_one_or_all_methods.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(chose_of_one_or_all_methods)
        # self.statusbar.setObjectName("statusbar")
        # chose_of_one_or_all_methods.setStatusBar(self.statusbar)

        self.retranslateUi(chose_of_one_or_all_methods)
        QtCore.QMetaObject.connectSlotsByName(chose_of_one_or_all_methods)

    def retranslateUi(self, chose_of_one_or_all_methods):
        _translate = QtCore.QCoreApplication.translate
        chose_of_one_or_all_methods.setWindowTitle(_translate("chose_of_one_or_all_methods", "chose_of_one_or_all_methods"))
        self.pushButton.setText(_translate("chose_of_one_or_all_methods", "Все методы"))
        self.pushButton_2.setText(_translate("chose_of_one_or_all_methods", "Конкретный метод"))
        self.pushButton_3.setText(_translate("chose_of_one_or_all_methods", "Вернуться"))
        self.label.setText(_translate("chose_of_one_or_all_methods", "Выбрать все или конкретный метод формирования (разбиения) начального поколения"))
        self.label_2.setText(_translate("chose_of_one_or_all_methods", f"{self.global_data.data['matrix']}"))


class Ui_formation_partitioning(object):
    def setupUi(self, formation_partitioning):
        self.global_data = DataApp()
        formation_partitioning.setObjectName("formation_partitioning")
        formation_partitioning.resize(812, 398)
        font = QtGui.QFont()
        font.setPointSize(8)
        formation_partitioning.setFont(font)
        self.centralwidget = QtWidgets.QWidget(formation_partitioning)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 0, 471, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(414, 5, 391, 341))
        font = QtGui.QFont()
        font.setPointSize(self.global_data.data['ui_matrix_size'])
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, -10, 20, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(20, 180, 161, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 210, 271, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 240, 271, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 270, 251, 20))
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(125, 320, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(245, 320, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        formation_partitioning.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(formation_partitioning)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        formation_partitioning.setMenuBar(self.menubar)
        #self.statusbar = QtWidgets.QStatusBar(formation_partitioning)
        #self.statusbar.setObjectName("statusbar")
        #formation_partitioning.setStatusBar(self.statusbar)

        self.retranslateUi(formation_partitioning)
        QtCore.QMetaObject.connectSlotsByName(formation_partitioning)

    def retranslateUi(self, GenethicAlgorythm):
        _translate = QtCore.QCoreApplication.translate
        GenethicAlgorythm.setWindowTitle(_translate("formation_partitioning", "formation_partitioning"))
        self.label.setText(_translate("formation_partitioning", "Способ формирования (разбиения) начального поколения"))
        self.label_2.setText(_translate("formation_partitioning", f"{self.global_data.data['matrix']}"))
        self.radioButton.setText(_translate("formation_partitioning", "100% рандомно"))
        self.radioButton_2.setText(_translate("formation_partitioning", "25% Рандомно + 75% детерминированно"))
        self.radioButton_3.setText(_translate("formation_partitioning", "75% Рандомно + 25% детерминированно"))
        self.radioButton_4.setText(_translate("formation_partitioning", "50% Плотников-Зверев + 50% Барьер"))
        self.pushButton.setText(_translate("formation_partitioning", "Дальше"))
        self.pushButton_2.setText(_translate("formation_partitioning", "Вернуться"))


class Ui_chosing_of_border(object):
    def setupUi(self, chosing_of_border):
        self.global_data = DataApp
        chosing_of_border.setObjectName("GenethicAlgorythm")
        chosing_of_border.resize(812, 398)
        font = QtGui.QFont()
        font.setPointSize(8)
        chosing_of_border.setFont(font)
        self.centralwidget = QtWidgets.QWidget(chosing_of_border)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 300, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(10, 10, 411, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(445, 5, 391, 341))
        font = QtGui.QFont()
        font.setPointSize(self.global_data.data['ui_matrix_size'])
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 300, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(230, 300, 101, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 300, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 10, 40, 40))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setFont(font1)
        #self.pushButton_5.setStyleSheet("border-image: url(../diploma/experiments/back2.jpg) stretch;");
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(460, -10, 20, 381))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 150, 421, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        chosing_of_border.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(chosing_of_border)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 26))
        self.menubar.setObjectName("menubar")
        chosing_of_border.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(chosing_of_border)
        # self.statusbar.setObjectName("statusbar")
        # chosing_of_border.setStatusBar(self.statusbar)

        self.retranslateUi(chosing_of_border)
        QtCore.QMetaObject.connectSlotsByName(chosing_of_border)

    def retranslateUi(self, chosing_of_border):
        _translate = QtCore.QCoreApplication.translate
        chosing_of_border.setWindowTitle(_translate("chosing_of_border", "chosing_of_border"))
        self.pushButton.setText(_translate("chosing_of_border", "По центру"))
        self.label.setText(_translate("chosing_of_border", "Способы формирования генов"))
        self.label_2.setText(_translate("chosing_of_border", f"{self.global_data.data['matrix']}"))
        self.pushButton_2.setText(_translate("chosing_of_border", "Слева"))
        self.pushButton_3.setText(_translate("chosing_of_border", "Справа"))
        self.pushButton_4.setText(_translate("chosing_of_border", "Рандомно"))
        self.pushButton_5.setText(_translate("chosing_of_border", "<"))
        self.label_3.setText(_translate("chosing_of_border", "Относительно левой и правой границы в процессоре"))


class Ui_ga_loader(object):
    def setupUi(self, ga_loader):
        ga_loader.setObjectName("ga_loader")
        ga_loader.resize(822, 404)
        font = QtGui.QFont()
        font.setPointSize(9)
        font1 = QtGui.QFont()
        font1.setPointSize(11)
        ga_loader.setFont(font)
        self.centralwidget = QtWidgets.QWidget(ga_loader)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 325, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(750, 10, 40, 40))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(font1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(250, -5, 300, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Bebas Neue Regular")
        font.setPointSize(22)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setIndent(-1)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 50, 1061, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 295, 781, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(21, 225, 80, 30))
        # font = QtGui.QFont()
        # font.setPointSize(9)
        # self.label_3.setFont(font)
        # self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        # self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 250, 735, 29))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("background-color: black; color: lightgreen")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(20, 190, 735, 29))
        # self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 220, 735, 29))
        self.label_5.setObjectName("label_2")
        self.label_5.setStyleSheet("background-color: black; color: lightgreen")
        self.label_6 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 190, 735, 29))
        self.label_6.setObjectName("label_2")
        self.label_6.setStyleSheet("background-color: black; color: lightgreen")
        self.label_7 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 160, 735, 29))
        self.label_7.setObjectName("label_2")
        self.label_7.setStyleSheet("background-color: black; color: lightgreen")
        ga_loader.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ga_loader)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 26))
        self.menubar.setObjectName("menubar")
        ga_loader.setMenuBar(self.menubar)

        self.retranslateUi(ga_loader)
        QtCore.QMetaObject.connectSlotsByName(ga_loader)

    def retranslateUi(self, ga_loader):
        _translate = QtCore.QCoreApplication.translate
        ga_loader.setWindowTitle(_translate("ga_loader", "ga_loader"))
        self.pushButton.setText(_translate("ga_loader", "Cтарт"))
        self.pushButton_2.setText(_translate("ga_loader", "<"))
        self.pushButton_3.setText(_translate("ga_loader", ">"))
        self.label.setText(_translate("ga_loader", "Генетический Алгоритм"))
        # self.label_3.setText(_translate("ga_loader", f""))
        # self.label_4.setText(_translate("ga_loader", f""))
        self.label_2.setPlainText(_translate("ga_loader", 'Нажмите "Старт", чтобы запустить алгоритм'))


class Ui_hystograms_choose(object):
    def setupUi(self, hystograms_choose):
        hystograms_choose.setObjectName("hystograms_choose")
        hystograms_choose.setEnabled(True)
        hystograms_choose.resize(822, 404)
        font = QtGui.QFont()
        font.setPointSize(9)
        hystograms_choose.setFont(font)
        self.centralwidget = QtWidgets.QWidget(hystograms_choose)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 327, 161, 31))
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 120, 411, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(410, 120, 411, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(0, 0, 411, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(410, 0, 411, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(400, 0, 20, 265))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        # self.line_2 = QtWidgets.QFrame(self.centralwidget)
        # self.line_2.setGeometry(QtCore.QRect(0, 315, 821, 21))
        # self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_2.setObjectName("line_2")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(0, 240, 410, 31))
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(409, 240, 412, 31))
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        hystograms_choose.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hystograms_choose)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 822, 26))
        self.menubar.setObjectName("menubar")
        self.lpic1 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic1.setGeometry(QtCore.QRect(0, 160, 81, 71))
        self.lpic1.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/central_bound/Result_25r+75d.png);'
        )
        #self.lpic1.setMinimumSize(QtCore.QSize(0, 0))
        #self.lpic1.setMaximumSize(QtCore.QSize(731, 16777215))
        #self.lpic1.setText("")
        #self.lpic1.setIcon(QtGui.QIcon("../diploma/experiments/histograms/central_bound/Result_25r+75d.png"))
        #self.lpic1.setIconSize(QSize(self.lpic1.width(), self.lpic1.height()))
        #self.lpic1.setScaledContents(True)
        #self.lpic1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lpic1.setObjectName("lpic1")
        self.lpic2 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic2.setGeometry(QtCore.QRect(80, 160, 81, 71))
        self.lpic2.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/central_bound/Result_50r+50d.png);'
        )
        self.lpic2.setObjectName("lpic2")
        self.lpic3 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic3.setGeometry(QtCore.QRect(160, 160, 81, 71))
        self.lpic3.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/central_bound/Result_75r+25d.png);'
        )
        self.lpic3.setObjectName("lpic3")
        self.lpic4 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic4.setGeometry(QtCore.QRect(240, 160, 81, 71))
        self.lpic4.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/central_bound/Result_50pz+50b.png);'
        )
        self.lpic4.setObjectName("lpic4")
        self.lpic5 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic5.setGeometry(QtCore.QRect(320, 160, 81, 71))
        self.lpic5.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/central_bound/Result_all.png);'
        )
        self.lpic5.setObjectName("lpic5")
        self.lpic6 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic6.setGeometry(QtCore.QRect(420, 40, 81, 71))
        self.lpic6.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/right_bound/Result_25r+75d.png);'
        )
        self.lpic6.setObjectName("lpic6")
        self.lpic7 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic7.setGeometry(QtCore.QRect(660, 40, 81, 71))
        self.lpic7.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/right_bound/Result_50pz+50b.png);'
        )
        self.lpic7.setObjectName("lpic7")
        self.lpic8 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic8.setGeometry(QtCore.QRect(500, 40, 81, 71))
        self.lpic8.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/right_bound/Result_50r+50d.png);'
        )
        self.lpic8.setObjectName("lpic8")
        self.lpic9 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic9.setGeometry(QtCore.QRect(740, 40, 81, 71))
        self.lpic9.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/right_bound/Result_all.png);'
        )
        self.lpic9.setObjectName("lpic9")
        self.lpic10 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic10.setGeometry(QtCore.QRect(580, 40, 81, 71))
        self.lpic10.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/right_bound/Result_75r+25d.png);'
        )
        self.lpic10.setObjectName("lpic10")
        self.lpic11 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic11.setGeometry(QtCore.QRect(0, 40, 81, 71))
        self.lpic11.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/left_bound/Result_25r+75d.png);'
        )
        self.lpic11.setObjectName("lpic11")
        self.lpic12 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic12.setGeometry(QtCore.QRect(240, 40, 81, 71))
        self.lpic12.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/left_bound/Result_50pz+50b.png);'
        )
        self.lpic12.setObjectName("lpic12")
        self.lpic13 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic13.setGeometry(QtCore.QRect(80, 40, 81, 71))
        self.lpic13.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/left_bound/Result_50r+50d.png);'
        )
        self.lpic13.setObjectName("lpic13")
        self.lpic14 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic14.setGeometry(QtCore.QRect(320, 40, 81, 71))
        self.lpic14.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/left_bound/Result_all.png);'
        )
        self.lpic14.setObjectName("lpic14")
        self.lpic15 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic15.setGeometry(QtCore.QRect(160, 40, 81, 71))
        self.lpic15.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/left_bound/Result_75r+25d.png);'
        )
        self.lpic15.setObjectName("lpic15")
        self.lpic16 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic16.setGeometry(QtCore.QRect(420, 160, 81, 71))
        self.lpic16.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/random_bound/Result_25r+75d.png);'
        )
        self.lpic16.setObjectName("lpic16")
        self.lpic17 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic17.setGeometry(QtCore.QRect(660, 160, 81, 71))
        self.lpic17.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/random_bound/Result_50pz+50b.png);'
        )
        self.lpic17.setObjectName("lpic17")
        self.lpic18 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic18.setGeometry(QtCore.QRect(500, 160, 81, 71))
        self.lpic18.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/random_bound/Result_50r+50d.png);'
        )
        self.lpic18.setObjectName("lpic18")
        self.lpic19 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic19.setGeometry(QtCore.QRect(740, 160, 81, 71))
        self.lpic19.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/random_bound/Result_all.png);'
        )
        self.lpic19.setObjectName("lpic19")
        self.lpic20 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic20.setGeometry(QtCore.QRect(580, 160, 81, 71))
        self.lpic20.setStyleSheet(
            'border-image: url(../diploma/experiments/histograms/random_bound/Result_75r+25d.png);'
        )
        self.lpic20.setObjectName("lpic20")
        self.lpic21 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic21.setGeometry(QtCore.QRect(155, 280, 81, 71))
        self.lpic21.setStyleSheet(
            'border-image: url(../diploma/experiments/all_bounds_results.png);'
        )
        self.lpic21.setObjectName("lpic21")
        self.lpic22 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic22.setGeometry(QtCore.QRect(575, 280, 81, 71))
        self.lpic22.setStyleSheet(
            'border-image: url(../diploma/experiments/all_methods_results.png);'
        )
        self.lpic22.setObjectName("lpic22")
        hystograms_choose.setCentralWidget(self.centralwidget)
        hystograms_choose.setMenuBar(self.menubar)

        self.retranslateUi(hystograms_choose)
        QtCore.QMetaObject.connectSlotsByName(hystograms_choose)

    def retranslateUi(self, hystograms_choose):
        _translate = QtCore.QCoreApplication.translate
        hystograms_choose.setWindowTitle(_translate("hystograms_choose", "hystograms_choose"))
        self.pushButton.setText(_translate("hystograms_choose", "Вернуться"))
        self.plainTextEdit.setPlainText(_translate("hystograms_choose", "                         Центральная граница"))
        self.plainTextEdit_2.setPlainText(_translate("hystograms_choose", "                           Рандомная граница"))
        self.plainTextEdit_3.setPlainText(_translate("hystograms_choose", "                             Левая граница"))
        self.plainTextEdit_4.setPlainText(_translate("hystograms_choose", "                             Правая граница"))
        self.plainTextEdit_6.setPlainText(_translate("hystograms_choose", "                              Все границы"))
        self.plainTextEdit_5.setPlainText(_translate("hystograms_choose", "                                Все методы"))


class choosing_variables(QtWidgets.QMainWindow, Ui_choosing_variables):
    def __init__(self, parent=None):
        super(choosing_variables, self).__init__(parent)
        self.setupUi(self)


class generate_matrix(QtWidgets.QMainWindow, Ui_generate_matrix):
    def __init__(self, parent=None):
        super(generate_matrix, self).__init__(parent)
        self.setupUi(self)


class number_of_repetitons(QtWidgets.QMainWindow, Ui_number_of_repetitons):
    def __init__(self, parent=None):
        super(number_of_repetitons, self).__init__(parent)
        self.setupUi(self)


class chose_of_one_or_all_methods(QtWidgets.QMainWindow, Ui_chose_of_one_or_all_methods):
    def __init__(self, parent=None):
        super(chose_of_one_or_all_methods, self).__init__(parent)
        self.setupUi(self)


class formation_partitioning(QtWidgets.QMainWindow, Ui_formation_partitioning):
    def __init__(self, parent=None):
        super(formation_partitioning, self).__init__(parent)
        self.setupUi(self)


class chosing_of_border(QtWidgets.QMainWindow, Ui_chosing_of_border):
    def __init__(self, parent=None):
        super(chosing_of_border, self).__init__(parent)
        self.setupUi(self)


class ga_loader(QtWidgets.QMainWindow, Ui_ga_loader):
    def __init__(self, parent=None):
        super(ga_loader, self).__init__(parent)
        self.setupUi(self)


class hystograms_choose(QtWidgets.QMainWindow, Ui_hystograms_choose):
    def __init__(self, parent=None):
        super(hystograms_choose, self).__init__(parent)
        self.setupUi(self)


class OutputLogger(QObject):
    emit_write = pyqtSignal(str, int)

    class Severity:
        DEBUG = 0
        ERROR = 1

    def __init__(self, io_stream, severity):
        super().__init__()

        self.io_stream = io_stream
        self.severity = severity

    def write(self, text):
        self.io_stream.write(text)
        self.emit_write.emit(text, self.severity)

    def flush(self):
        self.io_stream.flush()


OUTPUT_LOGGER_STDOUT = OutputLogger(sys.stdout, OutputLogger.Severity.DEBUG)
OUTPUT_LOGGER_STDERR = OutputLogger(sys.stderr, OutputLogger.Severity.ERROR)

sys.stdout = OUTPUT_LOGGER_STDOUT
sys.stderr = OUTPUT_LOGGER_STDERR


def json_open(namefile: Optional[Union[str, Path]], write_method: str, data: dict = None):
    if write_method == 'r':
        with open(namefile, 'r') as file:
            return json.load(file)
    new_data = deepcopy(data)
    with open(namefile, 'r') as file:
        try:
            json_dict = json.load(file)
            json_dict.update(new_data)
        except Exception as e:
            print(e)
    with open(namefile, write_method) as file:
        json.dump(json_dict, file, indent=4, ensure_ascii=False)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.global_data = DataApp()
        super().__init__()

        self.stacked = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked)

        self.window_choosing_variables = choosing_variables(self)
        self.window_generate_matrix = generate_matrix(self)
        self.window_number_of_repetitions = number_of_repetitons(self)
        self.window_chose_of_one_or_all_methods = chose_of_one_or_all_methods(self)
        self.window_formation_partitioning = formation_partitioning(self)
        self.window_chosing_of_border = chosing_of_border(self)
        self.window_ga_loader = ga_loader(self)
        self.window_hystograms_choose = hystograms_choose(self)

        self.stacked.addWidget(self.window_choosing_variables)
        self.stacked.addWidget(self.window_generate_matrix)
        self.stacked.addWidget(self.window_number_of_repetitions)
        self.stacked.addWidget(self.window_chose_of_one_or_all_methods)
        self.stacked.addWidget(self.window_formation_partitioning)
        self.stacked.addWidget(self.window_chosing_of_border)
        self.stacked.addWidget(self.window_ga_loader)
        self.stacked.addWidget(self.window_hystograms_choose)

        self.next_btn_0 = self.window_choosing_variables.pushButton
        self.next_btn_0.clicked.connect(self.choice_of_variables)
        self.m = self.window_choosing_variables.lineEdit
        self.n = self.window_choosing_variables.lineEdit_2
        self.T1 = self.window_choosing_variables.lineEdit_3
        self.T2 = self.window_choosing_variables.lineEdit_4
        self.z = self.window_choosing_variables.lineEdit_5
        self.k = self.window_choosing_variables.lineEdit_6
        self.Pk = self.window_choosing_variables.lineEdit_7
        self.Pm = self.window_choosing_variables.lineEdit_8

        self.ready_btn = self.window_generate_matrix.pushButton
        self.new_btn = self.window_generate_matrix.pushButton_2
        self.ready_btn.clicked.connect(self.generate_or_new_matrix)
        self.new_btn.clicked.connect(self.generate_or_new_matrix)
        self.back_btn1 = self.window_generate_matrix.pushButton_3
        self.back_btn1.clicked.connect(self.back)

        self.repets = self.window_number_of_repetitions.lineEdit
        self.next_btn = self.window_number_of_repetitions.pushButton
        self.next_btn.clicked.connect(self.repetitions)
        self.back_btn2 = self.window_number_of_repetitions.pushButton_2
        self.back_btn2.clicked.connect(self.back)

        self.all_mthds_btn = self.window_chose_of_one_or_all_methods.pushButton
        self.one_mthd_btn = self.window_chose_of_one_or_all_methods.pushButton_2
        self.all_mthds_btn.clicked.connect(self.is_create)
        self.one_mthd_btn.clicked.connect(self.is_create)
        self.back_btn3 = self.window_chose_of_one_or_all_methods.pushButton_3
        self.back_btn3.clicked.connect(self.back)

        self.next_btn_2 = self.window_formation_partitioning.pushButton
        self.radio_btn_cntr = self.window_formation_partitioning.radioButton
        self.radio_btn_left = self.window_formation_partitioning.radioButton_2
        self.radio_btn_right = self.window_formation_partitioning.radioButton_3
        self.radio_btn_rndm = self.window_formation_partitioning.radioButton_4
        self.radio_btn_cntr.toggled.connect(self.way_of_create)
        self.radio_btn_left.toggled.connect(self.way_of_create)
        self.radio_btn_right.toggled.connect(self.way_of_create)
        self.radio_btn_rndm.toggled.connect(self.way_of_create)
        self.next_btn_2.clicked.connect(self.way_of_create_btn)
        self.back_btn4 = self.window_formation_partitioning.pushButton_2
        self.back_btn4.clicked.connect(self.back)

        self.cntr_btn = self.window_chosing_of_border.pushButton
        self.left_btn = self.window_chosing_of_border.pushButton_2
        self.right_btn = self.window_chosing_of_border.pushButton_3
        self.random_btn = self.window_chosing_of_border.pushButton_4
        self.cntr_btn.clicked.connect(self.bound)
        self.left_btn.clicked.connect(self.bound)
        self.right_btn.clicked.connect(self.bound)
        self.random_btn.clicked.connect(self.bound)
        self.back_btn5 = self.window_chosing_of_border.pushButton_5
        self.back_btn5.clicked.connect(self.back)

        self.start_btn = self.window_ga_loader.pushButton
        self.progress_bar = self.window_ga_loader.progressBar
        self.start_btn.clicked.connect(self.start)
        self.console_text = self.window_ga_loader.label_2
        self.back_btn6 = self.window_ga_loader.pushButton_2
        self.back_btn6.clicked.connect(self.back)
        self.forward_btn = self.window_ga_loader.pushButton_3
        self.forward_btn.clicked.connect(self.forward)

        self.back_btn7 = self.window_hystograms_choose.pushButton
        self.back_btn7.clicked.connect(self.back)

        self.window_hystograms_choose.lpic1.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic2.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic3.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic4.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic5.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic6.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic7.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic8.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic9.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic10.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic12.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic13.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic14.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic15.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic16.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic17.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic18.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic19.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic20.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic21.clicked.connect(self.openPic)
        self.window_hystograms_choose.lpic22.clicked.connect(self.openPic)


    def choice_of_variables(self):
        data = {
            'm': int(self.m.text()),
            'n': int(self.n.text()),
            'T1': int(self.T1.text()),
            'T2': int(self.T2.text()),
            'z': int(self.z.text()),
            'k': int(self.k.text()),
            'Pk': int(self.Pk.text()),
            'Pm': int(self.Pm.text())
        }
        json_open(
            namefile="../diploma/experiments/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(1)

    def generate_or_new_matrix(self):
        T1, T2 = self.global_data.data["T1"], self.global_data.data["T2"]
        button = self.sender()
        print(button.text())
        if button.text() == 'Новая матрица':
            self.global_data.data["matrix"] = [[r(T1, T2) for _ in range(int(self.n.text()))] for __ in range(int(self.m.text()))]
            matrix = self.global_data.data["matrix"]
            data = json_open(
                namefile="../diploma/experiments/data.json",
                write_method='r'
            )
            data["matrix"] = '[' + ']\n['.join(', '.join(map(str, elem)) for elem in matrix) + ']'
            json_open(
                namefile="../diploma/experiments/data.json",
                write_method='w',
                data=data
            )
        else:
            data = json_open(
                namefile="../diploma/experiments/data.json",
                write_method='r'
            )
            self.global_data.data["matrix"] = [[int(elem) for elem in row[1:-1].split(", ")] for row in data["matrix"].split("\n")]
        matrix_str = data["matrix"]
        self.window_number_of_repetitions.label_2.setText(matrix_str)
        self.window_chose_of_one_or_all_methods.label_2.setText(matrix_str)
        self.window_formation_partitioning.label_2.setText(matrix_str)
        self.window_chosing_of_border.label_2.setText(matrix_str)
        self.stacked.setCurrentIndex(2)

    def repetitions(self):
        self.global_data.data["repetitions"] = int(self.repets.text())
        repetitions = self.global_data.data["repetitions"]
        data = {
            "repetitions": repetitions
        }
        json_open(
            namefile="../diploma/experiments/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(3)

    def is_create(self):
        button = self.sender()
        repetitions = self.global_data.data["repetitions"]
        ways_of_formation = self.global_data.data["ways_of_formation"]
        methods_amount = self.global_data.data["methods_amount"]
        self.global_data.data["is_create_way"] = button.text()
        is_create_way = self.global_data.data["is_create_way"]
        self.global_data.data["ways_of_formation"] = 0 if is_create_way == "Конкретный метод" else 3
        ways_of_formation = self.global_data.data["ways_of_formation"]
        data = {
            "is_create_way": is_create_way
        }
        json_open(
            namefile="../diploma/experiments/data.json",
            write_method="w",
            data=data
        )
        print(is_create_way, repetitions * methods_amount)
        self.progress_bar.setMaximum(
            {
                "Конкретный метод": (
                    int(repetitions) * methods_amount,
                    int(repetitions) * methods_amount
                )[self.global_data.data["create_way"] == "50% Плотников-Зверев + 50% Барьер"],
                "Все методы": int(repetitions) * methods_amount * ways_of_formation + int(repetitions)
            }[self.global_data.data["is_create_way"]]
        )
        self.stacked.setCurrentIndex(5) if is_create_way == 'Все методы' else self.stacked.setCurrentIndex(4)

    def way_of_create(self):
        radio_button = self.sender()

        if radio_button.isChecked():
            self.global_data.data["create_way"] = radio_button.text()
            create_way = self.global_data.data["create_way"]
            print(create_way)

    def way_of_create_btn(self):
        create_way = self.global_data.data["create_way"]
        data = {"create_way": create_way}
        json_open(
            namefile="../diploma/experiments/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(5)

    def bound(self):
        button = self.sender()

        bounds = self.global_data.data["bounds"]
        bounds = button.text()
        print(bounds)
        data = {
            "bounds": bounds
        }
        json_open(
            namefile="../diploma/experiments/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(6)

    def start(self):
        self.thread_progress = signal_thread()
        self.thread_progress._signal.connect(self.progress_signal_accept)
        self.thread_progress._signal_method.connect(self.method_signal_accept)
        self.thread_progress._signal_bound.connect(self.bound_signal_accept)
        self.thread_progress.start()
        OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
        OUTPUT_LOGGER_STDERR.emit_write.connect(self.append_log)

    def append_log(self, text, severity):
        text = repr(text)
        bounds = self.global_data.data['bounds']

        if severity == OutputLogger.Severity.ERROR:
            text = '{}'.format(text)[3:]

        self.console_text.setPlainText(text)
        self.window_ga_loader.label_7.setPlainText(f'Расположение генов между двумя границами процессоров: "{bounds}"')
        font = QtGui.QFont()
        font.setPointSize(7)
        self.console_text.setFont(font)


    def progress_signal_accept(self, msg):
        self.progress_bar.setValue(int(msg))
        if self.progress_bar.value() == self.progress_bar.maximum():
            self.stacked.setCurrentIndex(7)

    def method_signal_accept(self, msg):
        methods = (
            'Метод минимальных элементов',
            'Метод Плотникова-Зверева',
            'Метод Барьера'
        )
        self.window_ga_loader.label_5.setPlainText(
            f"{methods[int(msg[0]) - 1]} ({str(msg)})"
        )

    def bound_signal_accept(self, msg):
        ways_of_formation = self.global_data.data["ways_of_formation"]
        bound_formation = (
            '50% рандомно + 50% детерминированных особей',
            '25% рандомно + 75% детерминированных особей',
            '75% рандомно + 25% детерминированных особей',
            '50% Плт-Зврв + 50% барьерных особей'
        )
        self.window_ga_loader.label_6.setPlainText(
            f"Cпособ формирования: {bound_formation[int(msg) - 1]} ({int(msg)}/{ways_of_formation + 1})"
        )

    def back(self):
        self.stacked.setCurrentIndex(
            self.stacked.currentIndex() - 1 - (self.sender() == self.window_chosing_of_border.pushButton_5)
        )

    def forward(self):
        self.stacked.setCurrentIndex(self.stacked.currentIndex() + 1)

    def openPic(self):
        translate = {
            'lpic1': 'histograms/central_bound/Result_25r+75d.png',
            'lpic2': 'histograms/central_bound/Result_50r+50d.png',
            'lpic3': 'histograms/central_bound/Result_75r+25d.png',
            'lpic4': 'histograms/central_bound/Result_50pz+50b.png',
            'lpic5': 'histograms/central_bound/Result_all.png',
            'lpic6': 'histograms/right_bound/Result_25r+75d.png',
            'lpic7': 'histograms/right_bound/Result_50pz+50b.png',
            'lpic8': 'histograms/right_bound/Result_50r+50d.png',
            'lpic9': 'histograms/right_bound/Result_all.png',
            'lpic10': 'histograms/right_bound/Result_75r+25d.png',
            'lpic11': 'histograms/left_bound/Result_25r+75d.png',
            'lpic12': 'histograms/left_bound/Result_50pz+50b.png',
            'lpic13': 'histograms/left_bound/Result_50r+50d.png',
            'lpic14': 'histograms/left_bound/Result_all.png',
            'lpic15': 'histograms/left_bound/Result_75r+25d.png',
            'lpic16': 'histograms/random_bound/Result_25r+75d.png',
            'lpic17': 'histograms/random_bound/Result_50pz+50b.png',
            'lpic18': 'histograms/random_bound/Result_50r+50d.png',
            'lpic19': 'histograms/random_bound/Result_all.png',
            'lpic20': 'histograms/random_bound/Result_75r+25d.png',
            'lpic21': 'all_bounds_results.png',
            'lpic22': 'all_methods_results.png'
        }
        img = Image.open(f'../diploma/experiments/{translate[self.sender().objectName()]}')
        img.show()


if __name__ == '__main__':
    import sys
    try:
        # Включить в блок try/except, для Mac/Linux
        from PyQt5.QtWinExtras import QtWin  # !!!
        myappid = 'mycompany.myproduct.subproduct.version'  # !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
    except ImportError:
        pass
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('../diploma/experiments/icon2.png'))
    window = MainWindow()
    window.setFixedSize(812, 360)
    window.setWindowTitle('Генетический алгоритм')
    window.setWindowIcon(QtGui.QIcon('../diploma/experiments/icon2.png'))
    window.show()
    sys.exit(app.exec_())