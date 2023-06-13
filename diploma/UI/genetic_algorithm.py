# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'genetic_algorithm.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Genetic_window(object):
    def setupUi(self, Genetic_window):
        Genetic_window.setObjectName("Genetic_window")
        Genetic_window.resize(1150, 610)
        Genetic_window.setStyleSheet("\n"
".QSpinBox\n"
"{\n"
"    color:white;    \n"
"    padding: 4px;\n"
"}\n"
"\n"
"\n"
".QLabel\n"
"{\n"
"    border: 1px solid red;\n"
"}\n"
"                                 \n"
"\n"
"\n"
"QWidget\n"
"{\n"
"    background-color: black;\n"
"    color: white;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: black;\n"
"    color: white;\n"
"    border-color: #000000;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: #ff9c2b;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #ffaf5d;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #dd872f;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit\n"
"{\n"
"    background-color: #38394e;\n"
"    color: white;\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"    border-color: #4a4c68;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QTableView-----*/\n"
"QTableView, \n"
"QHeaderView, \n"
"QTableView::item \n"
"{\n"
"    background-color: #232430;\n"
"    color: white;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::item:selected \n"
"{ \n"
"    background-color: #41424e;\n"
"    color:white;\n"
"\n"
"}\n"
"\n"
"\n"
"QHeaderView::section:horizontal \n"
"{\n"
"    background-color: #232430;\n"
"    border: 1px solid #37384d;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator{\n"
"    background-color: #1d1d28;\n"
"    border: 1px solid #37384d;\n"
"\n"
"}\n"
"\n"
"\n"
"QTableView::indicator:checked{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"    background-color: #1d1d28;\n"
"\n"
"}\n"
"\n"
"/*-----QTabWidget-----*/\n"
"QTabWidget::pane \n"
"{ \n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabWidget::tab-bar \n"
"{\n"
"    left: 5px; \n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab \n"
"{\n"
"    color: white;\n"
"    min-width: 1px;\n"
"    padding-left: 25px;\n"
"    margin-left:-22px;\n"
"    height: 28px;\n"
"    border: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:selected \n"
"{\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    height: 28px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:!first \n"
"{\n"
"    margin-left: -20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:hover \n"
"{\n"
"    color: #DDD;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QScrollBar-----*/\n"
"QScrollBar:horizontal \n"
"{\n"
"    background-color: transparent;\n"
"    height: 8px;\n"
"    margin: 0px;\n"
"    padding: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal \n"
"{\n"
"    border: none;\n"
"    min-width: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal, \n"
"QScrollBar::sub-line:horizontal,\n"
"QScrollBar::add-page:horizontal, \n"
"QScrollBar::sub-page:horizontal \n"
"{\n"
"    width: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical \n"
"{\n"
"    background-color: transparent;\n"
"    width: 8px;\n"
"    margin: 0;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical \n"
"{\n"
"    border: none;\n"
"    min-height: 100px;\n"
"    background-color: #56576c;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical, \n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-page:vertical, \n"
"QScrollBar::sub-page:vertical \n"
"{\n"
"    height: 0px;\n"
"    background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QCalendarWidget\n"
"{\n"
"     border: 5px solid red;\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;\n"
"    border: 1px solid grey;\n"
"    height: 20%;\n"
"}\n"
"\n"
"QComboBox {\n"
"    color: white;\n"
"    border: 1px solid grey;\n"
"}\n"
"QRadioButton {\n"
"    color: white;\n"
"    border: 1px solid grey;\n"
"}\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: white;\n"
"    color: black;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"\n"
"QSpinBox\n"
"{\n"
"    border: 1px solid grey;\n"
"    height: 100%;\n"
"}\n"
"\n"
"/*-----QProgressBar-----*/\n"
"QProgressBar\n"
"{\n"
"    background-color: #383838;\n"
"    color: #ffffff;\n"
"    border: 1px solid #607cff;\n"
"    border-radius: 3px;\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #607cff;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk:disabled {\n"
"    background-color: #656565;\n"
"    border: 1px solid #aaa;\n"
"    color: #656565;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Genetic_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(10, 560, 1131, 41))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.progressBar = QtWidgets.QProgressBar(self.verticalLayoutWidget_6)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_6.addWidget(self.progressBar)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 981, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lpic4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lpic4.setText("")
        self.lpic4.setObjectName("lpic4")
        self.gridLayout.addWidget(self.lpic4, 0, 3, 1, 1)
        self.lpic3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lpic3.setText("")
        self.lpic3.setObjectName("lpic3")
        self.gridLayout.addWidget(self.lpic3, 0, 2, 1, 1)
        self.lpic2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lpic2.setText("")
        self.lpic2.setObjectName("lpic2")
        self.gridLayout.addWidget(self.lpic2, 0, 1, 1, 1)
        self.lpic6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lpic6.setText("")
        self.lpic6.setObjectName("lpic6")
        self.gridLayout.addWidget(self.lpic6, 0, 5, 1, 1)
        self.lpic5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lpic5.setText("")
        self.lpic5.setObjectName("lpic5")
        self.gridLayout.addWidget(self.lpic5, 0, 4, 1, 1)
        self.lpic1 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.lpic1.setText("")
        self.lpic1.setObjectName("lpic1")
        self.gridLayout.addWidget(self.lpic1, 0, 0, 1, 1)
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 200, 981, 101))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lpic13 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lpic13.setText("")
        self.lpic13.setObjectName("lpic13")
        self.gridLayout_2.addWidget(self.lpic13, 0, 2, 1, 1)
        self.lpic11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lpic11.setText("")
        self.lpic11.setObjectName("lpic11")
        self.gridLayout_2.addWidget(self.lpic11, 0, 0, 1, 1)
        self.lpic15 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lpic15.setText("")
        self.lpic15.setObjectName("lpic15")
        self.gridLayout_2.addWidget(self.lpic15, 0, 4, 1, 1)
        self.lpic12 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lpic12.setText("")
        self.lpic12.setObjectName("lpic12")
        self.gridLayout_2.addWidget(self.lpic12, 0, 1, 1, 1)
        self.lpic16 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lpic16.setText("")
        self.lpic16.setObjectName("lpic16")
        self.gridLayout_2.addWidget(self.lpic16, 0, 5, 1, 1)
        self.lpic14 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.lpic14.setText("")
        self.lpic14.setObjectName("lpic14")
        self.gridLayout_2.addWidget(self.lpic14, 0, 3, 1, 1)
        self.verticalLayoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_8.setGeometry(QtCore.QRect(50, 10, 941, 31))
        self.verticalLayoutWidget_8.setObjectName("verticalLayoutWidget_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_8)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_22 = QtWidgets.QLabel(self.verticalLayoutWidget_8)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.verticalLayoutWidget_11 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_11.setGeometry(QtCore.QRect(50, 160, 941, 31))
        self.verticalLayoutWidget_11.setObjectName("verticalLayoutWidget_11")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_11)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_24 = QtWidgets.QLabel(self.verticalLayoutWidget_11)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_11.addWidget(self.label_24)
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(1000, 10, 141, 31))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.verticalLayoutWidget_9 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setGeometry(QtCore.QRect(120, 460, 91, 101))
        self.verticalLayoutWidget_9.setObjectName("verticalLayoutWidget_9")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.radioButton_3 = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout_9.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_9.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_9.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.verticalLayoutWidget_9)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_9.addWidget(self.radioButton_6)
        self.verticalLayoutWidget_10 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_10.setGeometry(QtCore.QRect(1000, 50, 81, 101))
        self.verticalLayoutWidget_10.setObjectName("verticalLayoutWidget_10")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_10)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_10.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_10)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_10.addWidget(self.label_6)
        self.verticalLayoutWidget_12 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_12.setGeometry(QtCore.QRect(1000, 200, 81, 101))
        self.verticalLayoutWidget_12.setObjectName("verticalLayoutWidget_12")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_12)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_12)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_12.addWidget(self.label_7)
        self.verticalLayoutWidget_13 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_13.setGeometry(QtCore.QRect(1000, 160, 141, 31))
        self.verticalLayoutWidget_13.setObjectName("verticalLayoutWidget_13")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_13)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_13)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_13.addWidget(self.label_3)
        self.verticalLayoutWidget_16 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_16.setGeometry(QtCore.QRect(1090, 50, 51, 101))
        self.verticalLayoutWidget_16.setObjectName("verticalLayoutWidget_16")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_16)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_19.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_16)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_19.addWidget(self.label_13)
        self.verticalLayoutWidget_17 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_17.setGeometry(QtCore.QRect(1090, 200, 51, 101))
        self.verticalLayoutWidget_17.setObjectName("verticalLayoutWidget_17")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_17)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_14 = QtWidgets.QLabel(self.verticalLayoutWidget_17)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_23.addWidget(self.label_14)
        self.label_15 = QtWidgets.QLabel(self.verticalLayoutWidget_17)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_23.addWidget(self.label_15)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 160, 31, 31))
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_19 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_19.setGeometry(QtCore.QRect(50, 310, 941, 31))
        self.verticalLayoutWidget_19.setObjectName("verticalLayoutWidget_19")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_19)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_26 = QtWidgets.QLabel(self.verticalLayoutWidget_19)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_20.addWidget(self.label_26)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 350, 981, 101))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lpic13_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lpic13_3.setText("")
        self.lpic13_3.setObjectName("lpic13_3")
        self.gridLayout_4.addWidget(self.lpic13_3, 0, 2, 1, 1)
        self.lpic11_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lpic11_3.setText("")
        self.lpic11_3.setObjectName("lpic11_3")
        self.gridLayout_4.addWidget(self.lpic11_3, 0, 0, 1, 1)
        self.lpic15_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lpic15_3.setText("")
        self.lpic15_3.setObjectName("lpic15_3")
        self.gridLayout_4.addWidget(self.lpic15_3, 0, 4, 1, 1)
        self.lpic12_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lpic12_3.setText("")
        self.lpic12_3.setObjectName("lpic12_3")
        self.gridLayout_4.addWidget(self.lpic12_3, 0, 1, 1, 1)
        self.lpic16_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lpic16_3.setText("")
        self.lpic16_3.setObjectName("lpic16_3")
        self.gridLayout_4.addWidget(self.lpic16_3, 0, 5, 1, 1)
        self.lpic14_3 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.lpic14_3.setText("")
        self.lpic14_3.setObjectName("lpic14_3")
        self.gridLayout_4.addWidget(self.lpic14_3, 0, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 310, 31, 31))
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayoutWidget_20 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_20.setGeometry(QtCore.QRect(1000, 310, 141, 31))
        self.verticalLayoutWidget_20.setObjectName("verticalLayoutWidget_20")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_20)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_19 = QtWidgets.QLabel(self.verticalLayoutWidget_20)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        self.verticalLayout_21.addWidget(self.label_19)
        self.verticalLayoutWidget_21 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_21.setGeometry(QtCore.QRect(1000, 350, 81, 101))
        self.verticalLayoutWidget_21.setObjectName("verticalLayoutWidget_21")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_21)
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_20 = QtWidgets.QLabel(self.verticalLayoutWidget_21)
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_22.addWidget(self.label_20)
        self.label_21 = QtWidgets.QLabel(self.verticalLayoutWidget_21)
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_22.addWidget(self.label_21)
        self.verticalLayoutWidget_22 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_22.setGeometry(QtCore.QRect(1090, 350, 51, 101))
        self.verticalLayoutWidget_22.setObjectName("verticalLayoutWidget_22")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_22)
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.label_23 = QtWidgets.QLabel(self.verticalLayoutWidget_22)
        self.label_23.setAlignment(QtCore.Qt.AlignCenter)
        self.label_23.setObjectName("label_23")
        self.verticalLayout_26.addWidget(self.label_23)
        self.label_27 = QtWidgets.QLabel(self.verticalLayoutWidget_22)
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.verticalLayout_26.addWidget(self.label_27)
        self.verticalLayoutWidget_14 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_14.setGeometry(QtCore.QRect(10, 460, 101, 101))
        self.verticalLayoutWidget_14.setObjectName("verticalLayoutWidget_14")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_14)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_11 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("QLabel\n"
"{\n"
"height: 20%;\n"
"}")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_14.addWidget(self.label_11)
        self.radioButton = QtWidgets.QRadioButton(self.verticalLayoutWidget_14)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_14.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_14)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_14.addWidget(self.radioButton_2)
        self.label_16 = QtWidgets.QLabel(self.verticalLayoutWidget_14)
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_14.addWidget(self.label_16)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(220, 460, 921, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_29 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setText("")
        self.label_29.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_29.setObjectName("label_29")
        self.verticalLayout.addWidget(self.label_29)
        self.label_30 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_30.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_30.setObjectName("label_30")
        self.verticalLayout.addWidget(self.label_30)
        self.label_31 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_31.setText("")
        self.label_31.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_31.setObjectName("label_31")
        self.verticalLayout.addWidget(self.label_31)
        self.label_32 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.verticalLayout.addWidget(self.label_32)
        Genetic_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Genetic_window)
        QtCore.QMetaObject.connectSlotsByName(Genetic_window)

    def retranslateUi(self, Genetic_window):
        _translate = QtCore.QCoreApplication.translate
        Genetic_window.setWindowTitle(_translate("Genetic_window", "MainWindow"))
        self.label_22.setText(_translate("Genetic_window", "Последние 6 отсортированных по возрастанию"))
        self.label_24.setText(_translate("Genetic_window", "Последние 6 отсортированные по убыванию"))
        self.label_2.setText(_translate("Genetic_window", "Результат"))
        self.radioButton_3.setText(_translate("Genetic_window", "1 метод"))
        self.radioButton_4.setText(_translate("Genetic_window", "2 метод"))
        self.radioButton_5.setText(_translate("Genetic_window", "3 метод"))
        self.radioButton_6.setText(_translate("Genetic_window", "4 метод"))
        self.label_4.setText(_translate("Genetic_window", "Cредняя\n"
"нагрузка"))
        self.label_6.setText(_translate("Genetic_window", "Среднее\n"
"время"))
        self.label_5.setText(_translate("Genetic_window", "Средняя\n"
"нагрузка"))
        self.label_7.setText(_translate("Genetic_window", "Среднее\n"
"время"))
        self.label_3.setText(_translate("Genetic_window", "Результат"))
        self.label_12.setText(_translate("Genetic_window", "-"))
        self.label_13.setText(_translate("Genetic_window", "-"))
        self.label_14.setText(_translate("Genetic_window", "-"))
        self.label_15.setText(_translate("Genetic_window", "-"))
        self.pushButton.setText(_translate("Genetic_window", "<"))
        self.label_26.setText(_translate("Genetic_window", "Последние 6 не отсортированных"))
        self.label_19.setText(_translate("Genetic_window", "Результат"))
        self.label_20.setText(_translate("Genetic_window", "Средняя\n"
"нагрузка"))
        self.label_21.setText(_translate("Genetic_window", "Среднее\n"
"время"))
        self.label_23.setText(_translate("Genetic_window", "-"))
        self.label_27.setText(_translate("Genetic_window", "-"))
        self.label_11.setText(_translate("Genetic_window", "Лучшее"))
        self.radioButton.setText(_translate("Genetic_window", "Результат"))
        self.radioButton_2.setText(_translate("Genetic_window", "Время"))
        self.label_16.setText(_translate("Genetic_window", "00:00:00"))
        self.label_30.setText(_translate("Genetic_window", "▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉"))
