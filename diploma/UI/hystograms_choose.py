from PyQt5 import QtGui, QtWidgets, QtCore


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
            'border-image: url(../diploma/experiments_results/histograms/central_bound/Result_25r+75d.png);'
        )
        # self.lpic1.setMinimumSize(QtCore.QSize(0, 0))
        # self.lpic1.setMaximumSize(QtCore.QSize(731, 16777215))
        # self.lpic1.setText("")
        # self.lpic1.setIcon(QtGui.QIcon("../diploma/experiments_results/histograms/central_bound/Result_25r+75d.png"))
        # self.lpic1.setIconSize(QSize(self.lpic1.width(), self.lpic1.height()))
        # self.lpic1.setScaledContents(True)
        # self.lpic1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.lpic1.setObjectName("lpic1")
        self.lpic2 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic2.setGeometry(QtCore.QRect(80, 160, 81, 71))
        self.lpic2.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/central_bound/Result_50r+50d.png);'
        )
        self.lpic2.setObjectName("lpic2")
        self.lpic3 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic3.setGeometry(QtCore.QRect(160, 160, 81, 71))
        self.lpic3.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/central_bound/Result_75r+25d.png);'
        )
        self.lpic3.setObjectName("lpic3")
        self.lpic4 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic4.setGeometry(QtCore.QRect(240, 160, 81, 71))
        self.lpic4.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/central_bound/Result_50pz+50b.png);'
        )
        self.lpic4.setObjectName("lpic4")
        self.lpic5 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic5.setGeometry(QtCore.QRect(320, 160, 81, 71))
        self.lpic5.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/central_bound/Result_all.png);'
        )
        self.lpic5.setObjectName("lpic5")
        self.lpic6 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic6.setGeometry(QtCore.QRect(420, 40, 81, 71))
        self.lpic6.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/right_bound/Result_25r+75d.png);'
        )
        self.lpic6.setObjectName("lpic6")
        self.lpic7 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic7.setGeometry(QtCore.QRect(660, 40, 81, 71))
        self.lpic7.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/right_bound/Result_50pz+50b.png);'
        )
        self.lpic7.setObjectName("lpic7")
        self.lpic8 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic8.setGeometry(QtCore.QRect(500, 40, 81, 71))
        self.lpic8.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/right_bound/Result_50r+50d.png);'
        )
        self.lpic8.setObjectName("lpic8")
        self.lpic9 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic9.setGeometry(QtCore.QRect(740, 40, 81, 71))
        self.lpic9.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/right_bound/Result_all.png);'
        )
        self.lpic9.setObjectName("lpic9")
        self.lpic10 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic10.setGeometry(QtCore.QRect(580, 40, 81, 71))
        self.lpic10.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/right_bound/Result_75r+25d.png);'
        )
        self.lpic10.setObjectName("lpic10")
        self.lpic11 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic11.setGeometry(QtCore.QRect(0, 40, 81, 71))
        self.lpic11.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/left_bound/Result_25r+75d.png);'
        )
        self.lpic11.setObjectName("lpic11")
        self.lpic12 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic12.setGeometry(QtCore.QRect(240, 40, 81, 71))
        self.lpic12.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/left_bound/Result_50pz+50b.png);'
        )
        self.lpic12.setObjectName("lpic12")
        self.lpic13 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic13.setGeometry(QtCore.QRect(80, 40, 81, 71))
        self.lpic13.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/left_bound/Result_50r+50d.png);'
        )
        self.lpic13.setObjectName("lpic13")
        self.lpic14 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic14.setGeometry(QtCore.QRect(320, 40, 81, 71))
        self.lpic14.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/left_bound/Result_all.png);'
        )
        self.lpic14.setObjectName("lpic14")
        self.lpic15 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic15.setGeometry(QtCore.QRect(160, 40, 81, 71))
        self.lpic15.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/left_bound/Result_75r+25d.png);'
        )
        self.lpic15.setObjectName("lpic15")
        self.lpic16 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic16.setGeometry(QtCore.QRect(420, 160, 81, 71))
        self.lpic16.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/random_bound/Result_25r+75d.png);'
        )
        self.lpic16.setObjectName("lpic16")
        self.lpic17 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic17.setGeometry(QtCore.QRect(660, 160, 81, 71))
        self.lpic17.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/random_bound/Result_50pz+50b.png);'
        )
        self.lpic17.setObjectName("lpic17")
        self.lpic18 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic18.setGeometry(QtCore.QRect(500, 160, 81, 71))
        self.lpic18.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/random_bound/Result_50r+50d.png);'
        )
        self.lpic18.setObjectName("lpic18")
        self.lpic19 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic19.setGeometry(QtCore.QRect(740, 160, 81, 71))
        self.lpic19.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/random_bound/Result_all.png);'
        )
        self.lpic19.setObjectName("lpic19")
        self.lpic20 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic20.setGeometry(QtCore.QRect(580, 160, 81, 71))
        self.lpic20.setStyleSheet(
            'border-image: url(../diploma/experiments_results/histograms/random_bound/Result_75r+25d.png);'
        )
        self.lpic20.setObjectName("lpic20")
        self.lpic21 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic21.setGeometry(QtCore.QRect(155, 280, 81, 71))
        self.lpic21.setStyleSheet(
            'border-image: url(../diploma/experiments_results/all_bounds_results.png);'
        )
        self.lpic21.setObjectName("lpic21")
        self.lpic22 = QtWidgets.QPushButton(self.centralwidget)
        self.lpic22.setGeometry(QtCore.QRect(575, 280, 81, 71))
        self.lpic22.setStyleSheet(
            'border-image: url(../diploma/experiments_results/all_methods_results.png);'
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
        self.plainTextEdit_2.setPlainText(
            _translate("hystograms_choose", "                           Рандомная граница"))
        self.plainTextEdit_3.setPlainText(_translate("hystograms_choose", "                             Левая граница"))
        self.plainTextEdit_4.setPlainText(
            _translate("hystograms_choose", "                             Правая граница"))
        self.plainTextEdit_6.setPlainText(_translate("hystograms_choose", "                              Все границы"))
        self.plainTextEdit_5.setPlainText(_translate("hystograms_choose", "                                Все методы"))
