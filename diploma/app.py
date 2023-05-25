import sys

from PIL import Image
from PyQt5.Qt import QObject, pyqtSignal
from PyQt5 import QtGui, QtWidgets

from experiments import signal_thread

from diploma.Data import DataApp
from diploma.algorithms.utils import json_open
from diploma.algorithms.GA_utils import generate_matrix

from diploma.UI.ga_loader import Ui_ga_loader
from diploma.UI.chosing_of_border import Ui_chosing_of_border
from diploma.UI.hystograms_choose import Ui_hystograms_choose
from diploma.UI.choosing_variables import Ui_choosing_variables
from diploma.UI.number_of_repetitons import Ui_number_of_repetitons
from diploma.UI.formation_partitioning import Ui_formation_partitioning
from diploma.UI.generate_matrix_window import Ui_generate_matrix_window
from diploma.UI.chose_of_one_or_all_methods import Ui_chose_of_one_or_all_methods


class choosing_variables(QtWidgets.QMainWindow, Ui_choosing_variables):
    def __init__(self, parent=None):
        super(choosing_variables, self).__init__(parent)
        self.setupUi(self)


class generate_matrix_window(QtWidgets.QMainWindow, Ui_generate_matrix_window):
    def __init__(self, parent=None):
        super(generate_matrix_window, self).__init__(parent)
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


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        self.global_data = DataApp()
        super().__init__()

        self.stacked = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked)

        self.window_choosing_variables = choosing_variables(self)
        self.window_generate_matrix = generate_matrix_window(self)
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
            namefile="../diploma/experiments_results/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(1)

    def generate_or_new_matrix(self):
        T1, T2 = self.global_data.data["T1"], self.global_data.data["T2"]
        button = self.sender()
        print(button.text())
        if button.text() == 'Новая матрица':
            self.global_data.data["matrix"] = generate_matrix(int(self.m.text()), int(self.n.text()), T1, T2)
            matrix = self.global_data.data["matrix"]
            data = json_open(
                namefile="../diploma/experiments_results/data.json",
                write_method='r'
            )
            data["matrix"] = '\n'.join(' '.join(map(str, elem)) for elem in matrix)
            json_open(
                namefile="../diploma/experiments_results/data.json",
                write_method='w',
                data=data
            )
        else:
            data = json_open(
                namefile="../diploma/experiments_results/data.json",
                write_method='r'
            )
            self.global_data.data["matrix"] = []
            [self.global_data.data["matrix"].append(list(map(int, row.split()))) for row in data["matrix"]]
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
            namefile="../diploma/experiments_results/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(3)

    def is_create(self):
        button = self.sender()
        repetitions = self.global_data.data["repetitions"]
        methods_amount = self.global_data.data["methods_amount"]
        self.global_data.data["is_create_way"] = button.text()
        is_create_way = self.global_data.data["is_create_way"]
        self.global_data.data["ways_of_formation"] = 0 if is_create_way == "Конкретный метод" else 3
        ways_of_formation = self.global_data.data["ways_of_formation"]
        data = {
            "is_create_way": is_create_way
        }
        json_open(
            namefile="../diploma/experiments_results/data.json",
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
        if create_way == "50% Плотников-Зверев + 50% Барьер":
            self.progress_bar.setMaximum(self.progress_bar.maximum() // 3)
        data = {"create_way": create_way}
        json_open(
            namefile="../diploma/experiments_results/data.json",
            write_method='w',
            data=data
        )
        self.stacked.setCurrentIndex(5)

    def bound(self):
        button = self.sender()
        bounds = button.text()
        print(bounds)
        data = {
            "bounds": bounds
        }
        json_open(
            namefile="../diploma/experiments_results/data.json",
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
        img = Image.open(f'experiments_results/{translate[self.sender().objectName()]}')
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
    window.setFixedSize(812, 360)
    window.setWindowTitle('Генетический алгоритм')
    window.setWindowIcon(QtGui.QIcon('assets/icon2.png'))
    window.show()
    sys.exit(app.exec_())
