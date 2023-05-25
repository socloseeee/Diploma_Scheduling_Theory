import os.path
import sys
import numpy as np

from PIL import Image

from PyQt5.QtWidgets import QComboBox, QMessageBox
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import QObject, pyqtSignal, Qt
from superqt import QRangeSlider

from diploma.Data import DataApp
from diploma.experiments import signal_thread
from diploma.algorithms.utils import json_open
from diploma.UI.start_window import Ui_MainWindow
from diploma.algorithms.GA_utils import generate_matrix
from diploma.UI.genetic_algorithm import Ui_Genetic_window
from diploma.algorithms.Qt import RangeSlider, LabelStretcher


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
        self.n = self.start_window.plainTextEdit_2
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
        self.horizontalSlider.setMinimum(-1)
        self.horizontalSlider.setMaximum(101)
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.sliderMoved.connect(self.changeValue1)
        self.start_window.verticalLayout_18.removeWidget(self.start_window.horizontalSlider)
        self.horizontalSlider.setParent(None)

        self.start_window.label_13.setText(
            ''.join([elem + ' ' + '&nbsp;' * 80 + '\n' for elem in self.data.data["matrix"].split('\n')])
        )
        # Алгоритм расстояния Ньютона для сохранения текста внутри QLabel
        LabelStretcher(self.start_window.label_13)

        self.start_window.label_13.setText(self.data.data["matrix"])

        self.start_window.pushButton.clicked.connect(self.start_ga)

        self.ga_window.label_29.setStyleSheet("color: lightgreen")
        self.ga_window.label_30.setStyleSheet("color: lightgreen")
        self.ga_window.label_31.setStyleSheet("color: lightgreen")
        self.ga_window.label_32.setStyleSheet("color: lightgreen")

        self.coords_top = [((int(11 + (114 * i)), int(117 + (114 * i))), (70, 180)) for i in range(10)]
        self.coords_center = [((int(11 + (114 * i)), int(117 + (114 * i))), (250, 360)) for i in range(10)]
        self.coords_bottom = [((10, 120), (430, 530)), ((1030, 1140), (430, 530))]

        self.ga_window.lpic1.mousePressEvent = self.openPic
        self.ga_window.lpic2.mousePressEvent = self.openPic
        self.ga_window.lpic3.mousePressEvent = self.openPic
        self.ga_window.lpic4.mousePressEvent = self.openPic
        self.ga_window.lpic5.mousePressEvent = self.openPic
        self.ga_window.lpic6.mousePressEvent = self.openPic
        self.ga_window.lpic7.mousePressEvent = self.openPic
        self.ga_window.lpic8.mousePressEvent = self.openPic
        self.ga_window.lpic9.mousePressEvent = self.openPic
        self.ga_window.lpic10.mousePressEvent = self.openPic
        self.ga_window.lpic11.mousePressEvent = self.openPic
        self.ga_window.lpic12.mousePressEvent = self.openPic
        self.ga_window.lpic13.mousePressEvent = self.openPic
        self.ga_window.lpic14.mousePressEvent = self.openPic
        self.ga_window.lpic15.mousePressEvent = self.openPic
        self.ga_window.lpic16.mousePressEvent = self.openPic
        self.ga_window.lpic17.mousePressEvent = self.openPic
        self.ga_window.lpic18.mousePressEvent = self.openPic
        self.ga_window.lpic19.mousePressEvent = self.openPic
        self.ga_window.lpic20.mousePressEvent = self.openPic
        self.ga_window.lpic21.mousePressEvent = self.openPic
        self.ga_window.lpic22.mousePressEvent = self.openPic

    def start_ga(self):
        if self.start_window.radioButton.isChecked() or self.start_window.radioButton_2.isChecked() or self.start_window.radioButton_3.isChecked() or self.start_window.radioButton_4.isChecked() or self.start_window.radioButton_5.isChecked():
            data = {
                'm': int(self.m.toPlainText()),
                'n': int(self.n.toPlainText()),
                'T1': int(self.T1.toPlainText()),
                'T2': int(self.T2.toPlainText()),
                'z': int(self.z.toPlainText()),
                'k': int(self.k.toPlainText()),
                'Pk': int(self.Pk.toPlainText()),
                'Pm': int(self.Pm.toPlainText()),
                'repetitions': int(self.r.toPlainText()),
                '1method': self.combo_box1.currentText(),
                'matrix': self.start_window.label_13.text(),
            }

            if self.start_window.comboBox.currentText() == 'Один метод':
                data["amount_of_methods"] = 1
                data["splitting_values"] = (100,)

            if self.start_window.comboBox.currentText() == 'Два метода':
                data["2method"] = self.combo_box2.currentText()
                data["amount_of_methods"] = 2
                val = self.horizontalSlider.value()
                data["splitting_values"] = (val, 100 - val)

            if self.start_window.comboBox.currentText() == 'Три метода':
                data["2method"] = self.combo_box2.currentText()
                data["3method"] = self.combo_box3.currentText()
                data["amount_of_methods"] = 3
                high_val = self.slider.high()
                low_val = self.slider.low()
                data["splitting_values"] = (low_val, high_val - low_val, 100 - high_val)

            if self.start_window.comboBox.currentText() == 'Четыре метода':
                data["amount_of_methods"] = 4
                data["2method"] = self.combo_box2.currentText()
                data["3method"] = self.combo_box3.currentText()
                data["4method"] = self.combo_box4.currentText()
                values = self.range_slider.value()
                data["splitting_values"] = (values[0], values[1] - values[0], values[2] - values[1], 100 - values[2])

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
            self.thread_progress = signal_thread()
            self.thread_progress._signal.connect(self.progress_signal_accept)
            self.thread_progress._signal_bound.connect(self.bound_signal_accept)
            self.thread_progress.start()
            OUTPUT_LOGGER_STDOUT.emit_write.connect(self.append_log)
            OUTPUT_LOGGER_STDERR.emit_write.connect(self.append_log)
            if self.start_window.comboBox.currentText() == "Четыре метода":
                self.ga_window.label_29.setTextFormat(Qt.RichText)
                font = QtGui.QFont()
                font.setPointSize(9)
                font.setBold(True)
                font.setWeight(75)
                self.ga_window.label_29.setFont(font)
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
                self.ga_window.label_29.setStyleSheet("""
                                            padding-top: 10px;
                                        """)
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
            if self.start_window.comboBox.currentText() == "Три метода":
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
            if self.start_window.comboBox.currentText() == "Два метода":
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
            if self.start_window.comboBox.currentText() == "Один метод":
                self.ga_window.label_29.setText(
                    f'{data["1method"]}(<font color="blue">∎</font>): 100% '
                )
                val = 100 * '|'
                self.ga_window.label_30.setText(
                    f'<font color="blue">{val}</font>'
                )

            self.stacked.setCurrentIndex(1)
        else:
            QMessageBox.warning(self, "Предупреждение", "Пожалуйста выберите метод формирования относительно границ.")

    def append_log(self, text, severity):
        text = repr(text)

        if severity == OutputLogger.Severity.ERROR:
            text = '{}'.format(text)[3:]

        self.ga_window.label_32.setText(text)
        # font = QtGui.QFont()
        # font.setPointSize(7)
        # self.ga_window.label_32.setFont(font)

    def progress_signal_accept(self, msg):
        self.ga_window.progressBar.setValue(int(msg))
        if self.start_window.radioButton_5.isChecked():
            self.ga_window.progressBar.setMaximum(int(self.r.toPlainText()) * 4)
        else:
            self.ga_window.progressBar.setMaximum(int(self.r.toPlainText()))
        if self.ga_window.progressBar.value() == self.ga_window.progressBar.maximum():
            print("ok")

    def bound_signal_accept(self, msg):
        ways_of_formation = self.data.data["ways_of_formation"]
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
        matrix = np.fromstring(self.matrix.text(), sep=' ', dtype=int).reshape(int(self.m.toPlainText()),
                                                                               int(self.n.toPlainText()))
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
        matrix = np.fromstring(self.matrix.text(), sep=' ', dtype=int).reshape(int(self.m.toPlainText()),
                                                                               int(self.n.toPlainText()))
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
            int(self.m.toPlainText()),
            int(self.n.toPlainText()),
            int(self.T1.toPlainText()),
            int(self.T2.toPlainText())
        )
        matrix = '\n'.join(' '.join(map(str, elem)) for elem in matrix)
        self.start_window.label_13.setText(matrix)

    def change_method(self):
        value = self.horizontalSlider.value()
        if self.start_window.comboBox.currentText() in "Один метод":
            self.start_window.label_17.setText(
                "/\\ \n"
                "|\n"
                "Выберите количество методов, \n"
                "чтоб создать разбиение начального\n"
                "поколения"
            )
        if self.start_window.comboBox.currentText() in "Два метода":
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

    def changeValue1(self):
        value = self.horizontalSlider.value()
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
        # print(self.start_window.comboBox.currentText())
        # print(self.start_window.verticalLayout_29.count())

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
                f'{self.combo_box1.currentText()} {0}%\n'
                f'{self.combo_box2.currentText()} {100}%'
            )
            if self.start_window.verticalLayout_18.indexOf(self.range_slider) != -1:
                self.start_window.verticalLayout_18.removeWidget(self.range_slider)
                self.range_slider.setParent(None)
                self.start_window.verticalLayout_29.removeWidget(self.combo_box4)
                self.combo_box4.setParent(None)
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
        # print(x, y)
        if y <= 180:
            for i, elem in enumerate(self.coords_top):
                if x < elem[0][1]:
                    choice = i
                    break
        elif y <= 360:
            for i, elem in enumerate(self.coords_center):
                if x < elem[0][1]:
                    choice = 10 + i
                    break
        elif y <= 530:
            for i, elem in enumerate(self.coords_bottom):
                if x < elem[0][1]:
                    choice = 20 + i
                    break
        # print(choice)
        translate = [
            'histograms/central_bound/Result_25r+75d.png',
            'histograms/central_bound/Result_50r+50d.png',
            'histograms/central_bound/Result_75r+25d.png',
            'histograms/central_bound/Result_50pz+50b.png',
            'histograms/central_bound/Result_all.png',
            'histograms/right_bound/Result_25r+75d.png',
            'histograms/right_bound/Result_50pz+50b.png',
            'histograms/right_bound/Result_50r+50d.png',
            'histograms/right_bound/Result_all.png',
            'histograms/right_bound/Result_75r+25d.png',
            'histograms/left_bound/Result_25r+75d.png',
            'histograms/left_bound/Result_50pz+50b.png',
            'histograms/left_bound/Result_50r+50d.png',
            'histograms/left_bound/Result_all.png',
            'histograms/left_bound/Result_75r+25d.png',
            'histograms/random_bound/Result_25r+75d.png',
            'histograms/random_bound/Result_50pz+50b.png',
            'histograms/random_bound/Result_50r+50d.png',
            'histograms/random_bound/Result_all.png',
            'histograms/random_bound/Result_75r+25d.png',
            'all_bounds_results.png',
            'all_methods_results.png'
        ]
        img = Image.open(os.path.abspath(f'../diploma/experiments_results/{translate[choice]}'))
        img.show()


if __name__ == '__main__':

    try:
        # Включить в блок try/except, для Mac/Linux
        from PyQt5.QtWinExtras import QtWin  # !!!

        myappid = 'mycompany.myproduct.subproduct.version'  # !!!
        QtWin.setCurrentProcessExplicitAppUserModelID(myappid)  # !!!
    except ImportError:
        pass
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('assets/icon2.png'))
    window = MainWindow()
    window.setFixedSize(1150, 594)
    window.setWindowTitle('Генетический алгоритм')
    window.setWindowIcon(QtGui.QIcon('assets/icon2.png'))
    window.show()
    sys.exit(app.exec_())
