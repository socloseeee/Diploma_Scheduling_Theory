import random
import sys
import sqlite3
import platform
import itertools
import time

import numpy as np

from PIL import Image
from io import BytesIO
from superqt import QRangeSlider
from qt_material import apply_stylesheet, QtStyleTools

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QDesktopServices
from PyQt5.QtCore import QObject, pyqtSignal, Qt, QTime, QTimer, QUrl, QSize

from diploma import histogram
from diploma.Data import DataApp
from diploma.utils.utils import json_open
from diploma.experiments import signal_thread
from diploma.UI.start_window import Ui_MainWindow
from diploma.utils.GA_utils import generate_matrix
from diploma.utils.Qt import RangeSlider, LabelStretcher
from diploma.UI.genetic_algorithm import Ui_Genetic_window
from diploma.utils.db_utils import fill_labels_with_pics_and_data, db_init

random.seed(time.time() * 1000)


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


class start_window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(start_window, self).__init__(parent)
        self.setupUi(self)


class genetic_window(QtWidgets.QMainWindow, Ui_Genetic_window):
    def __init__(self, parent=None):
        super(genetic_window, self).__init__(parent)
        self.setupUi(self)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.data = DataApp()

        self.stacked = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked)

        self.start_window = start_window(self)
        self.ga_window = genetic_window(self)

        self.stacked.addWidget(self.start_window)
        self.stacked.addWidget(self.ga_window)

        # Data
        self.m = self.start_window.plainTextEdit
        self.n = self.start_window.plainTextEdit_1
        self.T1 = self.start_window.plainTextEdit_3
        self.T2 = self.start_window.plainTextEdit_5
        self.z = self.start_window.plainTextEdit_7
        self.k = self.start_window.plainTextEdit_8
        self.Pk = self.start_window.plainTextEdit_9
        self.Pm = self.start_window.plainTextEdit_10
        self.r = self.start_window.plainTextEdit_11
        self.generate_matrix = self.start_window.pushButton_3
        self.sort_up_matrix = self.start_window.pushButton_5
        self.sort_down_matrix = self.start_window.pushButton_6
        self.matrix = self.start_window.label_13

        self.sort_up_matrix.clicked.connect(self.sort_up)
        self.sort_down_matrix.clicked.connect(self.sort_down)
        self.generate_matrix.clicked.connect(self.generate)

        self.start_window.comboBox.currentIndexChanged.connect(self.choose_methods)

        # Надстройка комбобоксов с выбором метода
        self.combo_box1 = self.start_window.combo_box1
        self.combo_box1.currentIndexChanged.connect(self.change_method)
        self.combo_box2 = QComboBox(self)
        self.combo_box2.addItem("Метод минимальных элементов")
        self.combo_box2.addItem("Метод Плотникова-Зверева")
        self.combo_box2.addItem("Метод Барьера")
        self.combo_box2.addItem("Метод рандомного формирования")
        self.combo_box2.setVisible(False)
        self.combo_box2.currentIndexChanged.connect(self.change_method)
        self.combo_box3 = QComboBox(self)
        self.combo_box3.addItem("Метод минимальных элементов")
        self.combo_box3.addItem("Метод Плотникова-Зверева")
        self.combo_box3.addItem("Метод Барьера")
        self.combo_box3.addItem("Метод рандомного формирования")
        self.combo_box3.setVisible(False)
        self.combo_box3.currentIndexChanged.connect(self.change_method)
        self.combo_box4 = QComboBox(self)
        self.combo_box4.addItem("Метод минимальных элементов")
        self.combo_box4.addItem("Метод Плотникова-Зверева")
        self.combo_box4.addItem("Метод Барьера")
        self.combo_box4.addItem("Метод рандомного формирования")
        self.combo_box4.setVisible(False)
        self.combo_box4.currentIndexChanged.connect(self.change_method)

        # Кастомный ползунок с двумя дескрипторами
        self.slider = RangeSlider(QtCore.Qt.Horizontal)
        self.slider.setMinimumHeight(30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setLow(33)
        self.slider.setHigh(66)
        self.slider.setVisible(False)
        self.slider.sliderMoved.connect(self.changeValue2)

        # Кастомный ползунок с n количеством дескрипторов
        self.range_slider = QRangeSlider()
        self.range_slider.setValue((25, 50, 75))
        self.range_slider.setOrientation(QtCore.Qt.Horizontal)
        self.range_slider.setStyleSheet("background-color: transparent;")
        self.range_slider.sliderMoved.connect(self.changeValue3)

        # Встроенный в pyqt5 ползунок с 1-м дескриптором
        self.horizontalSlider = self.start_window.horizontalSlider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.sliderMoved.connect(self.changeValue1)
        self.start_window.verticalLayout_18.removeWidget(self.start_window.horizontalSlider)
        self.horizontalSlider.setParent(None)

        # Заполнение матрицей
        self.start_window.label_13.setText(
            ''.join([elem + ' ' + '&nbsp;' * 80 + '\n' for elem in self.data.data["matrix"].split('\n')])
        )
        # Алгоритм расстояния Ньютона для сохранения текста внутри QLabel
        LabelStretcher(self.start_window.label_13)
        self.start_window.label_13.setText(self.data.data["matrix"])

        # Инициализация ГА
        self.start_window.pushButton.clicked.connect(self.start_ga)

        # Консольный визуал для окна с ГА
        self.ga_window.label_29.setStyleSheet("color: lightgreen")
        self.ga_window.label_30.setStyleSheet("color: lightgreen")
        self.ga_window.label_30.setAlignment(QtCore.Qt.AlignHCenter)
        font = self.ga_window.label_30.font()
        font.setPointSize(24)
        self.ga_window.label_30.setFont(font)
        self.ga_window.label_31.setStyleSheet("color: lightgreen")
        self.ga_window.label_32.setStyleSheet("color: lightgreen")

        # Координаты окон с гистограммами
        self.coords_top = [((int(11 + (166 * i)), int(169 + (166 * i))), (40, 140)) for i in range(6)]
        self.coords_center = [((int(11 + (166 * i)), int(169 + (166 * i))), (180, 280)) for i in range(6)]
        self.coords_bottom = [((int(11 + (166 * i)), int(169 + (166 * i))), (320, 420)) for i in range(6)]

        # Окна с гистограммами
        self.sorted_up_pics = [
            self.ga_window.lpic1,
            self.ga_window.lpic2,
            self.ga_window.lpic3,
            self.ga_window.lpic4,
            self.ga_window.lpic5,
            self.ga_window.lpic6,
        ]
        self.sorted_center_pics = [
            self.ga_window.lpic11,
            self.ga_window.lpic12,
            self.ga_window.lpic13,
            self.ga_window.lpic14,
            self.ga_window.lpic15,
            self.ga_window.lpic16,
        ]
        self.sorted_down_pics = [
            self.ga_window.lpic11_3,
            self.ga_window.lpic12_3,
            self.ga_window.lpic13_3,
            self.ga_window.lpic14_3,
            self.ga_window.lpic15_3,
            self.ga_window.lpic16_3,
        ]
        self.ga_window.lpic1.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic2.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic3.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic4.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic5.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic6.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic11.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic12.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic13.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic14.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic15.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic16.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic11_3.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic12_3.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic13_3.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic14_3.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic15_3.setStyleSheet("border-radius: 0px;")
        self.ga_window.lpic16_3.setStyleSheet("border-radius: 0px;")
        self.pics_container = []

        # Открытие гистограмм по нажатию
        self.ga_window.lpic1.mousePressEvent = self.openPic
        self.ga_window.lpic2.mousePressEvent = self.openPic
        self.ga_window.lpic3.mousePressEvent = self.openPic
        self.ga_window.lpic4.mousePressEvent = self.openPic
        self.ga_window.lpic5.mousePressEvent = self.openPic
        self.ga_window.lpic6.mousePressEvent = self.openPic
        self.ga_window.lpic11.mousePressEvent = self.openPic
        self.ga_window.lpic12.mousePressEvent = self.openPic
        self.ga_window.lpic13.mousePressEvent = self.openPic
        self.ga_window.lpic14.mousePressEvent = self.openPic
        self.ga_window.lpic15.mousePressEvent = self.openPic
        self.ga_window.lpic16.mousePressEvent = self.openPic
        self.ga_window.lpic11_3.mousePressEvent = self.openPic
        self.ga_window.lpic12_3.mousePressEvent = self.openPic
        self.ga_window.lpic13_3.mousePressEvent = self.openPic
        self.ga_window.lpic14_3.mousePressEvent = self.openPic
        self.ga_window.lpic15_3.mousePressEvent = self.openPic
        self.ga_window.lpic16_3.mousePressEvent = self.openPic

        # Секундомер в левом нижнем углу
        self.time = QTime(0, 0, 0)
        self.timer = QTimer()
        self.timer_canvas = self.ga_window.label_16

        # Прослушивание прогресса прогресс баром
        self.ga_window.progressBar.valueChanged.connect(self.start_histogram_and_db)

        # Чекбоксы для фильтрации
        self.oneMethod = self.ga_window.checkBox_2
        self.twoMethod = self.ga_window.checkBox_4
        self.threeMethod = self.ga_window.checkBox_3
        self.fourMethod = self.ga_window.checkBox
        self.bestResult = self.ga_window.checkBox_5
        self.bestTime = self.ga_window.checkBox_6
        self.oneMethod.stateChanged.connect(self.filterHistograms)
        self.twoMethod.stateChanged.connect(self.filterHistograms)
        self.threeMethod.stateChanged.connect(self.filterHistograms)
        self.fourMethod.stateChanged.connect(self.filterHistograms)
        self.bestResult.stateChanged.connect(self.filterHistograms)
        self.bestTime.stateChanged.connect(self.filterHistograms)
        self.checkboxes = [
            self.oneMethod,
            self.twoMethod,
            self.threeMethod,
            self.fourMethod,
            self.bestResult,
            self.bestTime
        ]

        # Запросы
        self.query = [
            '''
            SELECT data FROM all_method WHERE sorted_on = 'Отсортированно по возрастанию' ORDER BY id DESC LIMIT 8;
            ''',
            '''
            SELECT data FROM all_method WHERE sorted_on = 'Отсортированно по убыванию' ORDER BY id DESC LIMIT 8;
            ''',
            '''
            SELECT data FROM all_method WHERE sorted_on = 'Без сортировки' ORDER BY id DESC LIMIT 8;
            '''
        ]

        # Картинка для кнопки "назад"
        back_pic = QPixmap("assets/back.png")
        back_pic = QIcon(back_pic)
        self.ga_window.pushButton.setIcon(back_pic)
        self.ga_window.pushButton.setIconSize(self.ga_window.pushButton_2.size())
        self.ga_window.pushButton.clicked.connect(self.back)

        # Картинка для кнопки "GitHub"
        githib_pic = QPixmap("assets/github2.png")
        github_pic = QIcon(githib_pic)
        self.ga_window.pushButton_2.setIcon(github_pic)
        self.ga_window.pushButton_2.setIconSize(self.ga_window.pushButton_2.size())
        self.ga_window.pushButton_2.clicked.connect(self.GithubLink)

        # Картинка для кнопки "вперёд"
        forward_pic = QPixmap("assets/forward.png")
        forward_pic = QIcon(forward_pic)
        self.start_window.pushButton_2.setIcon(forward_pic)
        self.start_window.pushButton_2.setIconSize(self.start_window.pushButton_2.size())
        self.start_window.pushButton_2.clicked.connect(self.forward)

        # Картинка для кнопки "ДГТУ"
        forward_pic = QPixmap("assets/DSTU.png")
        forward_pic = QIcon(forward_pic)
        self.ga_window.pushButton_3.setIcon(forward_pic)
        self.ga_window.pushButton_3.setIconSize(
            QSize(
                self.start_window.pushButton_2.size().width() + 5,
                self.start_window.pushButton_2.size().height() + 40
            )
        )
        self.ga_window.pushButton_3.clicked.connect(self.DSTULink)

        # Заполнить QLabels картинками
        fill_labels_with_pics_and_data(
            self.sorted_up_pics,
            self.sorted_center_pics,
            self.sorted_down_pics,
            [
                self.ga_window.label_12,
                self.ga_window.label_13,
                self.ga_window.label_14,
                self.ga_window.label_15,
            ]
        )

        # Последняя гистограмма
        self.last_img = None

        # Инициализируем поток
        self.thread = None

        # Запускался ли таймер?
        self.timer_r = None

        # Комбо-бокс если был сделан выбор генерировать матрциу при каждом повторе
        self.start_window.checkBox.stateChanged.connect(self.regenerate)
        self.start_window.verticalLayout_30.removeWidget(self.start_window.comboBox_2)
        self.start_window.comboBox_2.setParent(None)

        # Проверка ОС, для смены системного шрифта
        if platform.system() == 'Windows':
            font = QtGui.QFont()
            font.setPointSize(7)
            font.setBold(False)
            font.setWeight(50)
            self.start_window.label_17.setFont(font)
            font = QtGui.QFont()
            font.setPointSize(9)
            font.setBold(False)
            font.setWeight(50)
            self.start_window.label_18.setFont(font)
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setWeight(50)
            self.timer_canvas.setFont(font)
            font = QtGui.QFont()
            font.setPointSize(7)
            font.setBold(True)
            font.setWeight(50)
            self.ga_window.label_29.setFont(font)
            font = QtGui.QFont()
            font.setPointSize(14)
            font.setWeight(50)
            self.ga_window.label_30.setFont(font)

    def regenerate(self):
        if self.start_window.checkBox.isChecked():
            if self.start_window.verticalLayout_30.indexOf(self.start_window.comboBox_2) == -1:
                self.start_window.verticalLayout_30.insertWidget(4, self.start_window.comboBox_2)
                self.combo_box1.setVisible(True)
        else:
            self.start_window.verticalLayout_30.removeWidget(self.start_window.comboBox_2)
            self.start_window.comboBox_2.setParent(None)

    def forward(self):
        self.stacked.setCurrentIndex(
            self.stacked.currentIndex() + 1
        )

    def back(self):
        self.stacked.setCurrentIndex(
            self.stacked.currentIndex() - 1
        )

    def GithubLink(self):
        QDesktopServices.openUrl(QUrl("https://github.com/socloseeee/Diploma_Scheduling_Theory/tree/master"))

    def DSTULink(self):
        QDesktopServices.openUrl(QUrl("https://donstu.ru/"))

    def filterHistograms(self, state):
        self.pics_container = []
        sender = self.sender()
        result_up = None
        result_down = None
        result_no_sort = None
        conn = sqlite3.connect('experiments_results/resultsdb.sqlite3')
        cursor = conn.cursor()
        for checkbox in self.checkboxes:
            checkbox.setChecked(False)

        if self.oneMethod == sender:
            self.query = [
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '1' AND sorted_on = 'Отсортированно по возрастанию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '1' AND sorted_on = 'Отсортированно по убыванию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '1' AND sorted_on = 'Без сортировки' ORDER BY id DESC;
                '''
            ]
            cursor.execute(self.query[0])
            result_up = cursor.fetchall()
            cursor.execute(self.query[1])
            result_down = cursor.fetchall()
            cursor.execute(self.query[2])
            result_no_sort = cursor.fetchall()
        if self.twoMethod == sender:
            self.query = [
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '2' AND sorted_on = 'Отсортированно по возрастанию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '2' AND sorted_on = 'Отсортированно по убыванию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '2' AND sorted_on = 'Без сортировки' ORDER BY id DESC;
                '''
            ]
            cursor.execute(self.query[0])
            result_up = cursor.fetchall()
            cursor.execute(self.query[1])
            result_down = cursor.fetchall()
            cursor.execute(self.query[2])
            result_no_sort = cursor.fetchall()
        if self.threeMethod == sender:
            self.query = [
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '3' AND sorted_on = 'Отсортированно по возрастанию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '3' AND sorted_on = 'Отсортированно по убыванию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '3' AND sorted_on = 'Без сортировки' ORDER BY id DESC;
                '''
            ]
            cursor.execute(self.query[0])
            result_up = cursor.fetchall()
            cursor.execute(self.query[1])
            result_down = cursor.fetchall()
            cursor.execute(self.query[2])
            result_no_sort = cursor.fetchall()
        if self.fourMethod == sender:
            self.query = [
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '4' AND sorted_on = 'Отсортированно по возрастанию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '4' AND sorted_on = 'Отсортированно по убыванию' ORDER BY id DESC;
                ''',
                '''
                SELECT data FROM all_method WHERE amount_of_methods = '4' AND sorted_on = 'Без сортировки' ORDER BY id DESC;
                '''
            ]
            cursor.execute(self.query[0])
            result_up = cursor.fetchall()
            cursor.execute(self.query[1])
            result_down = cursor.fetchall()
            cursor.execute(self.query[2])
            result_no_sort = cursor.fetchall()
        if self.bestResult == sender:
            self.query = [
                '''
                SELECT data, result, SUM(CAST(value AS INTEGER)) AS sum
                FROM all_method, 
                     json_each('[' || REPLACE(result, ' ', ',') || ']')
                WHERE sorted_on = 'Отсортированно по возрастанию'
                GROUP BY result
                ORDER BY sum;
                ''',
                '''
                SELECT data, result, SUM(CAST(value AS INTEGER)) AS sum
                FROM all_method, 
                     json_each('[' || REPLACE(result, ' ', ',') || ']')
                WHERE sorted_on = 'Отсортированно по убыванию'
                GROUP BY result
                ORDER BY sum;
                ''',
                '''
                SELECT data, result, SUM(CAST(value AS INTEGER)) AS sum
                FROM all_method, 
                     json_each('[' || REPLACE(result, ' ', ',') || ']')
                WHERE sorted_on = 'Без сортировки'
                GROUP BY result
                ORDER BY sum;
                '''
            ]
            cursor.execute(self.query[0])
            result_up = list(map(lambda x: (x[0],), cursor.fetchall()))
            cursor.execute(self.query[1])
            result_down = list(map(lambda x: (x[0],), cursor.fetchall()))
            cursor.execute(self.query[2])
            result_no_sort = list(map(lambda x: (x[0],), cursor.fetchall()))
        if self.bestTime == sender:
            self.query = [
                '''
                SELECT data, elapsed_time, SUM(CAST(value AS INTEGER)) AS sum
                FROM all_method, 
                     json_each('[' || REPLACE(elapsed_time, ' ', ',') || ']')
                WHERE sorted_on = 'Отсортированно по возрастанию'
                GROUP BY elapsed_time
                ORDER BY sum; 
                ''',
                '''
                SELECT data, elapsed_time, SUM(CAST(value AS INTEGER)) AS sum
                FROM all_method, 
                     json_each('[' || REPLACE(elapsed_time, ' ', ',') || ']')
                WHERE sorted_on = 'Отсортированно по убыванию'
                GROUP BY elapsed_time
                ORDER BY sum; 
                ''',
                '''
                SELECT data, elapsed_time, SUM(CAST(value AS INTEGER)) AS sum
                FROM all_method, 
                     json_each('[' || REPLACE(elapsed_time, ' ', ',') || ']')
                WHERE sorted_on = 'Без сортировки'
                GROUP BY elapsed_time
                ORDER BY sum; 
                '''
            ]
            cursor.execute(self.query[0])
            result_up = list(map(lambda x: (x[0],), cursor.fetchall()))
            cursor.execute(self.query[1])
            result_down = list(map(lambda x: (x[0],), cursor.fetchall()))
            cursor.execute(self.query[2])
            result_no_sort = list(map(lambda x: (x[0],), cursor.fetchall()))
        if result_up is not None or result_down is not None:
            for label, filtered_img in itertools.zip_longest(self.sorted_up_pics, result_up):
                if label:
                    if filtered_img:
                        image = BytesIO(filtered_img[0])
                        pixmap = QPixmap()
                        pixmap.loadFromData(image.read())
                        pixmap_scaled = pixmap.scaled(159, 99)
                        label.setPixmap(pixmap_scaled)
                        self.pics_container.append(pixmap_scaled)
                    else:
                        label.setPixmap(QPixmap())
                        self.pics_container.append(QPixmap())
            for label, filtered_img in itertools.zip_longest(self.sorted_center_pics, result_down):
                if label:
                    if filtered_img:
                        image = BytesIO(filtered_img[0])
                        pixmap = QPixmap()
                        pixmap.loadFromData(image.read())
                        pixmap_scaled = pixmap.scaled(159, 99)
                        label.setPixmap(pixmap_scaled)
                        self.pics_container.append(pixmap_scaled)
                    else:
                        label.setPixmap(QPixmap())
                        self.pics_container.append(QPixmap())
            for label, filtered_img in itertools.zip_longest(self.sorted_down_pics, result_no_sort):
                if label:
                    if filtered_img:
                        image = BytesIO(filtered_img[0])
                        pixmap = QPixmap()
                        pixmap.loadFromData(image.read())
                        pixmap_scaled = pixmap.scaled(159, 99)
                        label.setPixmap(pixmap_scaled)
                        self.pics_container.append(pixmap_scaled)
                    else:
                        label.setPixmap(QPixmap())
                        self.pics_container.append(QPixmap())
        conn.close()

    def timerEvent(self) -> None:
        if not self.timer_r:
            self.time = self.time.addSecs(1)
        self.timer_canvas.setText(self.time.toString())

    def start_histogram_and_db(self):
        if self.ga_window.progressBar.value() == self.ga_window.progressBar.maximum():
            self.last_img = histogram.run()

    def start_ga(self):
        if self.thread is None:
            if self.start_window.radioButton.isChecked() or self.start_window.radioButton_2.isChecked() or self.start_window.radioButton_3.isChecked() or self.start_window.radioButton_4.isChecked() or self.start_window.radioButton_5.isChecked():
                data = {
                    'm': int(self.m.value()),
                    'n': int(self.n.value()),
                    'T1': int(self.T1.value()),
                    'T2': int(self.T2.value()),
                    'z': int(self.z.value()),
                    'k': int(self.k.value()),
                    'Pk': int(self.Pk.value()),
                    'Pm': int(self.Pm.value()),
                    'repetitions': int(self.r.value()),
                    '1method': self.combo_box1.currentText(),
                    'matrix': self.start_window.label_13.text(),
                    'regenerate_matrix': self.start_window.checkBox.isChecked()
                }

                if self.start_window.checkBox.isChecked():
                    data['sort_regenerate_matrix'] = self.start_window.comboBox_2.currentText()

                if self.start_window.comboBox.currentText() == 'Один метод':
                    data["amount_of_methods"] = 1
                    data["splitting_values"] = (100,)

                    self.ga_window.label_29.setText(
                        f'{data["1method"]}(<font color="blue">∎</font>): 100% '
                    )
                    val = 100 * '|'
                    self.ga_window.label_30.setText(
                        f'<font color="blue">{val}</font>'
                    )

                if self.start_window.comboBox.currentText() == 'Два метода':
                    data["2method"] = self.combo_box2.currentText()
                    data["amount_of_methods"] = 2
                    val = self.horizontalSlider.value()
                    data["splitting_values"] = (val, 100 - val)

                    self.ga_window.label_29.setTextFormat(Qt.RichText)
                    self.ga_window.label_29.setText(
                        f'{data["1method"]}(<font color="blue">∎</font>): {data["splitting_values"][0]}% '
                        f'&nbsp;&nbsp;'
                        f'{data["2method"]}(<font color="red">∎</font>): {data["splitting_values"][1]}% '
                        + "&nbsp;" * 150
                    )
                    self.ga_window.label_29.setWordWrap(True)
                    self.ga_window.label_29.setAlignment(  # !!!
                        QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter  # !!!
                    )
                    self.ga_window.label_29.setStyleSheet("""
                                                    padding-top: 10px;
                                                """)
                    val1 = data["splitting_values"][0] * '|'
                    val2 = data["splitting_values"][1] * '|'
                    self.ga_window.label_30.setText(
                        f'<font color="blue">{val1}</font><font color="red">{val2}</font>'
                    )

                if self.start_window.comboBox.currentText() == 'Три метода':
                    data["2method"] = self.combo_box2.currentText()
                    data["3method"] = self.combo_box3.currentText()
                    data["amount_of_methods"] = 3
                    high_val = self.slider.high()
                    low_val = self.slider.low()
                    data["splitting_values"] = (low_val, high_val - low_val, 100 - high_val)

                    self.ga_window.label_29.setTextFormat(Qt.RichText)
                    self.ga_window.label_29.setText(
                        f'{data["1method"]}(<font color="blue">∎</font>): {data["splitting_values"][0]}% | '
                        f'{data["2method"]}(<font color="red">∎</font>): {data["splitting_values"][1]}% | '
                        f'{data["3method"]}(<font color="green">∎</font>): {data["splitting_values"][2]}% '
                        + "&nbsp;" * 100
                    )
                    self.ga_window.label_29.setWordWrap(True)
                    self.ga_window.label_29.setAlignment(  # !!!
                        QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter  # !!!
                    )
                    self.ga_window.label_29.setStyleSheet("""
                        padding-top: 10px;
                    """)
                    val1 = data["splitting_values"][0] * '|'
                    val2 = data["splitting_values"][1] * '|'
                    val3 = data["splitting_values"][2] * '|'
                    self.ga_window.label_30.setText(
                        f'<font color="blue">{val1}</font><font color="red">{val2}</font><font color="green">{val3}</font>'
                    )

                if self.start_window.comboBox.currentText() == 'Четыре метода':
                    data["amount_of_methods"] = 4
                    data["2method"] = self.combo_box2.currentText()
                    data["3method"] = self.combo_box3.currentText()
                    data["4method"] = self.combo_box4.currentText()
                    values = self.range_slider.value()
                    data["splitting_values"] = (
                        values[0], values[1] - values[0], values[2] - values[1], 100 - values[2])

                    self.ga_window.label_29.setTextFormat(Qt.RichText)
                    self.ga_window.label_29.setText(
                        f'{data["1method"][data["1method"].index(" ") + 1:].capitalize()}(<font color="blue">∎</font>): {data["splitting_values"][0]}% | '
                        f'{data["2method"][data["2method"].index(" ") + 1:].capitalize()}(<font color="red">∎</font>): {data["splitting_values"][1]}% | '
                        f'{data["3method"][data["3method"].index(" ") + 1:].capitalize()}(<font color="green">∎</font>): {data["splitting_values"][2]}% | '
                        f'{data["4method"][data["4method"].index(" ") + 1:].capitalize()}(<font color="orange">∎</font>): {data["splitting_values"][3]}% '
                        + "&nbsp;" * 200
                    )
                    self.ga_window.label_29.setWordWrap(True)
                    self.ga_window.label_29.setAlignment(  # !!!
                        QtCore.Qt.AlignJustify | QtCore.Qt.AlignVCenter  # !!!
                    )
                    self.ga_window.label_29.setStyleSheet("""padding-top: 10px;""")
                    val1 = data["splitting_values"][0] * '|'
                    val2 = data["splitting_values"][1] * '|'
                    val3 = data["splitting_values"][2] * '|'
                    val4 = data["splitting_values"][3] * '|'
                    self.ga_window.label_30.setText(
                        f'<font color="blue">{val1}</font>'
                        f'<font color="red">{val2}</font>'
                        f'<font color="green">{val3}</font>'
                        f'<font color="orange">{val4}</font>'
                    )

                if self.start_window.radioButton_2.isChecked():
                    data["bound"] = "Слева"
                if self.start_window.radioButton.isChecked():
                    data["bound"] = "Справа"
                if self.start_window.radioButton_3.isChecked():
                    data["bound"] = "По центру"
                if self.start_window.radioButton_4.isChecked():
                    data["bound"] = "Рандомно"
                if self.start_window.radioButton_5.isChecked():
                    data["bound"] = "По всем"

                json_open(
                    namefile="../diploma/experiments_results/data.json",
                    write_method='w',
                    data=data
                )

                # Запускаем ГА и Секундомер
                self.time = QTime(0, 0, 0)
                self.timer.timeout.connect(self.timerEvent)
                if self.timer_r:
                    self.time.setInterval(0)
                self.timer.start(1000)
                self.thread = signal_thread()
                self.thread._signal.connect(self.progress_signal_accept)
                self.thread._signal_bound.connect(self.bound_signal_accept)
                self.thread.start()
                self.thread.finished.connect(self.add_images)
                OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
                OUTPUT_LOGGER_STDERR.emit_write.connect(self.append_log)

                # Инициализация и проверка существования таблиц
                db_init('experiments_results/resultsdb.sqlite3')

                self.stacked.setCurrentIndex(1)
            else:
                QMessageBox.warning(self, "Предупреждение", "Пожалуйста выберите метод формирования относительно "
                                                            "границ.")
        else:
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Прерывание скрипта.")
            msgBox.setInformativeText("Пожалуйста, дождитесь пока Генетический Алгоритм не завершит свою работу.")
            msgBox.setWindowTitle("Прерывание Генетического Алгоритма.")
            msgBox.exec_()

    def add_images(self):
        conn = sqlite3.connect('experiments_results/resultsdb.sqlite3')
        cursor = conn.cursor()
        cursor.execute('''
        SELECT result, elapsed_time FROM all_method WHERE sorted_on = 'Отсортированно по возрастанию';
        ''')
        data_sorted_up = cursor.fetchall()
        cursor.execute('''
        SELECT result, elapsed_time FROM all_method WHERE sorted_on = 'Отсортированно по убыванию';
        ''')
        data_sorted_down = cursor.fetchall()
        cursor.execute('''
                SELECT result, elapsed_time FROM all_method WHERE sorted_on = 'Без сортировки';
                ''')
        data_no_sort = cursor.fetchall()
        if data_sorted_up:
            result_sorted_up = list(map(lambda x: list(map(float, x[0].split())), data_sorted_up))
            time_sorted_up = list(map(lambda x: list(map(float, x[1].split())), data_sorted_up))
            self.ga_window.label_12.setText(
                str("{:.2f}".format(sum(map(sum, result_sorted_up)) / len(result_sorted_up) / 4)))
            self.ga_window.label_13.setText(
                str("{:.2f}".format(sum(map(sum, time_sorted_up)) / len(time_sorted_up) / 4)))
        if data_sorted_down:
            result_sorted_down = list(map(lambda x: list(map(float, x[0].split())), data_sorted_down))
            time_sorted_down = list(map(lambda x: list(map(float, x[1].split())), data_sorted_down))
            # print(sum(result_sorted_down) / len(result_sorted_down))
            self.ga_window.label_14.setText(
                str("{:.2f}".format(sum(map(sum, result_sorted_down)) / len(result_sorted_down) / 4)))
            self.ga_window.label_15.setText(
                str("{:.2f}".format(sum(map(sum, time_sorted_down)) / len(time_sorted_down) / 4)))
        if data_no_sort:
            result_no_sort = list(map(lambda x: list(map(float, x[0].split())), data_no_sort))
            time_no_sort = list(map(lambda x: list(map(float, x[1].split())), data_no_sort))
            # print(sum(result_sorted_down) / len(result_sorted_down))
            self.ga_window.label_23.setText(
                str("{:.2f}".format(sum(map(sum, result_no_sort)) / len(result_no_sort) / 4)))
            self.ga_window.label_27.setText(
                str("{:.2f}".format(sum(map(sum, time_no_sort)) / len(time_no_sort) / 4)))
        cursor.execute(self.query[0])
        images_sorted_up = cursor.fetchall()
        cursor.execute(self.query[1])
        images_sorted_down = cursor.fetchall()
        cursor.execute(self.query[2])
        images_no_sort = cursor.fetchall()
        for image_data, label in zip(
                images_sorted_up, self.sorted_up_pics
        ):
            image = BytesIO(image_data[0])
            pixmap = QPixmap()
            pixmap.loadFromData(image.read())  # .scaled(width=107, height=109)
            pixmap_scaled = pixmap.scaled(159, 99)
            label.setPixmap(pixmap_scaled)
        for image_data, label in zip(
                images_sorted_down, self.sorted_center_pics
        ):
            image = BytesIO(image_data[0])
            pixmap = QPixmap()
            pixmap.loadFromData(image.read())
            pixmap_scaled = pixmap.scaled(159, 99)
            label.setPixmap(pixmap_scaled)
        for image_data, label in zip(
                images_no_sort, self.sorted_down_pics
        ):
            image = BytesIO(image_data[0])
            pixmap = QPixmap()
            pixmap.loadFromData(image.read())
            pixmap_scaled = pixmap.scaled(159, 99)
            label.setPixmap(pixmap_scaled)
        conn.close()
        self.thread.quit()
        self.thread.wait()
        self.thread = None
        self.timer.stop()

    def append_log(self, text, severity):
        text = repr(text)

        if severity == OutputLogger.Severity.ERROR:
            text = '{}'.format(text)[3:]

        if len(text) > 6:
            self.ga_window.label_32.setText(text)

    def progress_signal_accept(self, msg):
        self.ga_window.progressBar.setValue(int(msg))
        if self.start_window.radioButton_5.isChecked():
            self.ga_window.progressBar.setMaximum(int(self.r.value()) * 4)
        else:
            self.ga_window.progressBar.setMaximum(int(self.r.value()))
        if self.ga_window.progressBar.value() == self.ga_window.progressBar.maximum():
            print("ok")

    def bound_signal_accept(self, msg):
        bound_formation = (
            'По левой границе',
            'По правой границе',
            'По центральной границе',
            'Рандомно'
        )
        check = bound_formation[int(msg) - 1]
        if not self.start_window.radioButton_5.isChecked():
            if self.start_window.radioButton_2.isChecked():
                check = bound_formation[0]
            if self.start_window.radioButton.isChecked():
                check = bound_formation[1]
            if self.start_window.radioButton_3.isChecked():
                check = bound_formation[2]
            if self.start_window.radioButton_4.isChecked():
                check = bound_formation[3]

        self.ga_window.label_31.setText(
            f'Расположение генов между двумя границами процессоров: '
            f'{check} ({int(msg)}/{self.start_window.radioButton_5.isChecked() * 3 + 1})'
        )

    def sort_up(self):
        matrix = np.fromstring(self.matrix.text(), sep=' ', dtype=int).reshape(int(self.m.value()),
                                                                               int(self.n.value()))
        # считаем суммы значений по строкам
        row_sums = matrix.sum(axis=1)
        # получаем индексы строк, отсортированные по возрастанию суммы значений
        sorted_indexes = row_sums.argsort()
        # создаем новую матрицу, отсортированную по возрастанию суммы значений
        sorted_matrix = matrix[sorted_indexes]
        sorted_matrix = '\n'.join(' '.join(map(str, elem)) for elem in sorted_matrix)
        self.start_window.label_13.setText(sorted_matrix)
        json_open(
            namefile="../diploma/experiments_results/data.json",
            write_method='w',
            data={
                "sorted_up": True,
                "sorted_down": False
            }
        )

    def sort_down(self):
        matrix = np.fromstring(self.matrix.text(), sep=' ', dtype=int).reshape(int(self.m.value()),
                                                                               int(self.n.value()))
        # считаем суммы значений по строкам
        row_sums = matrix.sum(axis=1)
        # получаем индексы строк, отсортированные по убыванию суммы значений
        sorted_indexes = row_sums.argsort()[::-1]
        # создаем новую матрицу, отсортированную по убыванию суммы значений
        sorted_matrix = matrix[sorted_indexes]
        sorted_matrix = '\n'.join(' '.join(map(str, elem)) for elem in sorted_matrix)
        self.start_window.label_13.setText(sorted_matrix)
        json_open(
            namefile="../diploma/experiments_results/data.json",
            write_method='w',
            data={
                "sorted_up": False,
                "sorted_down": True
            }
        )

    def generate(self):
        matrix = generate_matrix(
            int(self.m.value()),
            int(self.n.value()),
            int(self.T1.value()),
            int(self.T2.value())
        )
        matrix = '\n'.join(' '.join(map(str, elem)) for elem in matrix)
        self.start_window.label_13.setText(matrix)

    def change_method(self):
        if self.start_window.comboBox.currentText() in "Один метод":
            self.start_window.label_17.setText(
                "/\\ \n"
                "|\n"
                "Выберите количество методов, \n"
                "чтоб создать разбиение начального\n"
                "поколения"
            )
        if self.start_window.comboBox.currentText() in "Два метода":
            value = self.start_window.horizontalSlider.value()
            self.start_window.label_17.setText(
                f'{self.combo_box1.currentText()} {value}%\n'
                f'{self.combo_box2.currentText()} {100 - value}%'
            )
        if self.start_window.comboBox.currentText() in "Три метода":
            low_value = self.slider.low()
            high_value = self.slider.high()
            self.start_window.label_17.setText(
                f'{self.combo_box1.currentText()} {low_value}%\n'
                f'{self.combo_box2.currentText()} {high_value - low_value}%\n'
                f'{self.combo_box3.currentText()} {100 - high_value}%'
            )
        if self.start_window.comboBox.currentText() in "Четыре метода":
            values = self.range_slider.value()
            self.start_window.label_17.setText(
                f'{self.combo_box1.currentText()} {values[0]}%\n'
                f'{self.combo_box2.currentText()} {values[1] - values[0]}%\n'
                f'{self.combo_box3.currentText()} {values[2] - values[1]}%\n'
                f'{self.combo_box4.currentText()} {100 - values[2]}%'
            )

    def changeValue1(self, value):
        # value = self.horizontalSlider.
        self.start_window.label_17.setText(
            f'{self.combo_box1.currentText()} {value}%\n'
            f'{self.combo_box2.currentText()} {100 - value}%'
        )

    def changeValue2(self, low_value, high_value):
        # Обновляем значение метки при изменении ползунка
        self.start_window.label_17.setText(
            f'{self.combo_box1.currentText()} {low_value}%\n'
            f'{self.combo_box2.currentText()} {high_value - low_value}%\n'
            f'{self.combo_box3.currentText()} {100 - high_value}%'
        )

    def changeValue3(self):
        values = self.range_slider.value()
        self.start_window.label_17.setText(
            f'{self.combo_box1.currentText()} {values[0]}%\n'
            f'{self.combo_box2.currentText()} {values[1] - values[0]}%\n'
            f'{self.combo_box3.currentText()} {values[2] - values[1]}%\n'
            f'{self.combo_box4.currentText()} {100 - values[2]}%'
        )

    def choose_methods(self):

        if self.start_window.comboBox.currentText() in "Один метод":
            self.start_window.label_18.setText(
                "Разбиение формируется от 2-х и более"
            )
            self.start_window.label_17.setText(
                "/\\ \n"
                "|\n"
                "Выберите количество методов, \n"
                "чтоб создать разбиение начального\n"
                "поколения"
            )
            if self.start_window.verticalLayout_18.indexOf(self.range_slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.range_slider)
                self.range_slider.setParent(None)
                self.start_window.verticalLayout_29.removeWidget(self.combo_box4)
                self.combo_box4.setParent(None)
            if self.start_window.verticalLayout_18.indexOf(self.slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.slider)
                self.slider.setParent(None)
            if self.start_window.verticalLayout_18.indexOf(self.start_window.horizontalSlider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.start_window.horizontalSlider)
                self.start_window.horizontalSlider.setParent(None)
            if self.start_window.verticalLayout_29.indexOf(self.combo_box2) != -1:
                self.start_window.verticalLayout_29.removeWidget(self.combo_box2)
                self.combo_box2.setParent(None)
            if self.start_window.verticalLayout_29.indexOf(self.combo_box3) != -1:
                self.start_window.verticalLayout_29.removeWidget(self.combo_box3)
                self.combo_box3.setParent(None)
            self.start_window.verticalLayout_29.insertWidget(0, self.combo_box1)
            self.combo_box1.setVisible(True)

        if self.start_window.comboBox.currentText() in "Два метода" and (self.start_window.verticalLayout_29.indexOf(
                self.combo_box1) == -1 or self.start_window.verticalLayout_29.indexOf(self.combo_box1) != -1):
            self.start_window.label_17.setText(
                f'{self.combo_box1.currentText()} {50}%\n'
                f'{self.combo_box2.currentText()} {50}%'
            )
            if self.start_window.verticalLayout_18.indexOf(self.range_slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.range_slider)
                self.range_slider.setParent(None)
                self.start_window.verticalLayout_29.removeWidget(self.combo_box4)
                self.combo_box4.setParent(None)
                self.start_window.verticalLayout_29.removeWidget(self.combo_box3)
                self.combo_box3.setParent(None)
            self.start_window.verticalLayout_18.addWidget(self.start_window.horizontalSlider)
            if self.start_window.verticalLayout_18.indexOf(self.slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.slider)
                self.slider.setParent(None)
                self.start_window.verticalLayout_29.removeWidget(self.combo_box3)
                self.combo_box3.setParent(None)
            if self.start_window.verticalLayout_18.indexOf(self.start_window.horizontalSlider) == -1:
                self.start_window.verticalLayout_18.addWidget(self.start_window.horizontalSlider)
            self.start_window.verticalLayout_29.insertWidget(0, self.combo_box1)
            self.combo_box1.setVisible(True)
            self.start_window.verticalLayout_29.insertWidget(1, self.combo_box2)
            self.combo_box2.setVisible(True)

        if self.start_window.comboBox.currentText() in "Три метода":
            self.start_window.label_17.setText(
                f'{self.combo_box1.currentText()} 33%\n'
                f'{self.combo_box2.currentText()} 33%\n'
                f'{self.combo_box3.currentText()} 34%'
            )
            if self.start_window.verticalLayout_18.indexOf(self.range_slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.range_slider)
                self.range_slider.setParent(None)
                self.start_window.verticalLayout_29.removeWidget(self.combo_box4)
                self.combo_box4.setParent(None)
            if self.start_window.verticalLayout_29.indexOf(self.combo_box2) == -1:
                self.start_window.verticalLayout_29.insertWidget(1, self.combo_box2)
                self.combo_box2.setVisible(True)
            self.start_window.verticalLayout_29.insertWidget(2, self.combo_box3)
            self.combo_box3.setVisible(True)
            if self.start_window.verticalLayout_29.indexOf(self.combo_box1) == -1:
                self.start_window.verticalLayout_29.insertWidget(0, self.combo_box1)
                self.combo_box1.setVisible(True)
            self.start_window.verticalLayout_18.removeWidget(self.start_window.horizontalSlider)
            self.start_window.horizontalSlider.setParent(None)
            self.start_window.verticalLayout_18.addWidget(self.slider)
            self.slider.setVisible(True)

        if self.start_window.comboBox.currentText() in "Четыре метода" and self.start_window.verticalLayout_29.indexOf(
                self.combo_box4) == -1:
            self.start_window.label_17.setText(
                f'{self.combo_box1.currentText()} 25%\n'
                f'{self.combo_box2.currentText()} 25%\n'
                f'{self.combo_box3.currentText()} 25%\n'
                f'{self.combo_box4.currentText()} 25%'
            )
            if self.start_window.verticalLayout_29.indexOf(self.combo_box2) == -1:
                self.start_window.verticalLayout_29.insertWidget(1, self.combo_box2)
                self.combo_box2.setVisible(True)
            if self.start_window.verticalLayout_29.indexOf(self.combo_box3) == -1:
                self.start_window.verticalLayout_29.insertWidget(2, self.combo_box3)
                self.combo_box3.setVisible(True)
            self.start_window.verticalLayout_29.insertWidget(3, self.combo_box4)
            self.combo_box4.setVisible(True)
            if self.start_window.verticalLayout_18.indexOf(self.horizontalSlider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.start_window.horizontalSlider)
                self.start_window.horizontalSlider.setParent(None)
            if self.start_window.verticalLayout_18.indexOf(self.slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.slider)
                self.slider.setParent(None)
            self.start_window.verticalLayout_18.addWidget(self.range_slider)
            self.range_slider.setVisible(True)

    def openPic(self, event):
        choice: int = 0
        x = int(event.windowPos().x())
        y = int(event.windowPos().y())
        conn = sqlite3.connect('experiments_results/resultsdb.sqlite3')
        print(event.windowPos())
        try:
            if 40 <= y <= 140:
                for i, elem in enumerate(self.coords_top):
                    if x < elem[0][1]:
                        choice = i
                        break
                cursor = conn.cursor()
                cursor.execute(self.query[0])
                images_sorted_up = cursor.fetchall()
                img = images_sorted_up[choice]
                img = Image.open(BytesIO(img[0]))
                img.show()
            elif 180 <= y <= 280:
                for i, elem in enumerate(self.coords_center):
                    if x < elem[0][1]:
                        choice = i
                        break
                cursor = conn.cursor()
                cursor.execute(self.query[1])
                images_sorted_down = cursor.fetchall()
                img = images_sorted_down[choice]
                img = Image.open(BytesIO(img[0]))
                img.show()
            elif 320 <= y <= 420:
                for i, elem in enumerate(self.coords_bottom):
                    if x < elem[0][1]:
                        choice = i
                        break
                cursor = conn.cursor()
                cursor.execute(self.query[2])
                images_sorted_down = cursor.fetchall()
                img = images_sorted_down[choice]
                img = Image.open(BytesIO(img[0]))
                img.show()
        except Exception as e:
            error_dialog = QMessageBox()
            error_dialog.setIcon(QMessageBox.Critical)
            error_dialog.setWindowTitle("Ошибка")
            error_dialog.setText("Произошла ошибка при открытии изображения")
            error_dialog.setInformativeText(str(e))
            error_dialog.setStandardButtons(QMessageBox.Ok)
            error_dialog.exec_()
        conn.close()


if __name__ == '__main__':

    try:
        # Включить в блок try/except, для Mac/Linux
        from PyQt5.QtWinExtras import QtWin  # !!!

        myappid = 'mycompany.myproduct.subproduct.version'  # !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
    except ImportError:
        pass
    app = QtWidgets.QApplication(sys.argv)
    # apply_stylesheet(app, theme='dark_amber.xml')
    app.setWindowIcon(QtGui.QIcon('assets/icon2.png'))
    window = MainWindow()
    window.setFixedSize(1150, 594)
    window.setWindowTitle('Генетический алгоритм')
    window.setWindowIcon(QtGui.QIcon('assets/icon2.png'))
    window.show()
    sys.exit(app.exec_())
