import os
import json
import subprocess

import numpy as np

from tqdm import tqdm
from colorama import Fore, init, Style
from PyQt5.Qt import QThread, pyqtSignal

from diploma.algorithms.GA import genetic_algorithm
from diploma.algorithms.utils import writing_in_files
from diploma.algorithms.GA_utils import generate_individ, count_load, best_load
from diploma.algorithms.optimization_methods import min_elem_method, plotnikov_zverev_method, barrier_method

init(autoreset=True)


class signal_thread(QThread):
    _signal = pyqtSignal(int)
    _signal_method = pyqtSignal(str)
    _signal_bound = pyqtSignal(int)

    def __init__(self):
        super(signal_thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):

        progress = 0
        bound_progress = 1

        # Считывание data.txt
        with open(os.path.abspath('experiments_results/data.json'), 'r', encoding='UTF-8') as f:
            data = json.load(f)
        m, n, T1, T2 = data['m'], data['n'], data["T1"], data["T2"]
        z, k, Pk, Pm = data['z'], data['k'], data["Pk"], data["Pm"]
        matrix = np.fromstring(data["matrix"], sep=' ', dtype=int).reshape(m, n).tolist()
        repeat = int(data["repetitions"])
        bounds_dict = {
            "Слева": 0,
            "Справа": 1,
            "По центру": 2,
            "Рандомно": 3,
            "По всем": 4
        }
        bounds = bounds_dict[data["bound"]]
        splitting_values = data["splitting_values"]
        amount_of_methods = data["amount_of_methods"]
        methods_chosen = []
        if amount_of_methods == 4:
            methods_chosen.append(data["1method"])
            methods_chosen.append(data["2method"])
            methods_chosen.append(data["3method"])
            methods_chosen.append(data["4method"])
        if amount_of_methods == 3:
            methods_chosen.append(data["1method"])
            methods_chosen.append(data["2method"])
            methods_chosen.append(data["3method"])
        elif amount_of_methods == 2:
            methods_chosen.append(data["1method"])
            methods_chosen.append(data["2method"])
        else:
            methods_chosen.append(data["1method"])

        # Методы формирования
        # Метод минимальных элементов
        result_min, min_elem_idx = min_elem_method(matrix, m, n)
        # Метод Плотникова-Зверева
        result_pltzvr, plt_zvr_idx = plotnikov_zverev_method(matrix, m, n)
        # Метод барьера
        result_marrier, barrier_idx = barrier_method(matrix, m, n, result_min)

        # Преднеобходимое (методы + коллекции для вывода)
        methods = {
            "Метод минимальных элементов": min_elem_idx,
            "Метод Плотникова-Зверева": plt_zvr_idx,
            "Метод Барьера": barrier_idx,
            "Метод рандомного формирования": 1
        }
        str_methods = (
            Fore.BLUE + "The method of minimal elements | Метод минмальных элементов:" + Style.RESET_ALL,
            Fore.BLUE + "The Plotnikov-Zverev method | Метод Плотникова-Зверева:" + Style.RESET_ALL,
            Fore.BLUE + "The barrier method | Метод барьера:" + Style.RESET_ALL
        )
        repeat_str = Fore.LIGHTYELLOW_EX + str(repeat) + Style.RESET_ALL
        print(
            f"Performing a study based on {repeat_str} iterations | Выполняем исследование на основе {repeat_str} итераций"
        )

        # Переводчик для вывода
        way_of_forming_genes = {
            0: "left_bound",
            1: "right_bound",
            2: "central_bound",
            3: "random_bound",
        }
        if bounds in range(4):
            way_of_forming_genes = {bounds: way_of_forming_genes[bounds]}

        sorted_ = "sorted_up" if data["sorted_up"] else "sorted_down"

        # Генерация особей и последующее выполнение ГА
        for bound in way_of_forming_genes.keys():

            self._signal_bound.emit(bound_progress)
            bound_progress += 1
            work_time, results = [], []
            print(Fore.LIGHTCYAN_EX + way_of_forming_genes[bound] + Style.RESET_ALL)


            # Открываем файлы для записи:
            txt_file = os.path.abspath(f'experiments_results/bounds_data/{sorted_}/repetitions_results/{way_of_forming_genes[bound]}_analysis.txt')
            f = open(txt_file, 'w', encoding="utf-8")
            result_file = open(
                os.path.abspath(
                    f'experiments_results/bounds_data/{sorted_}/summary_results/result_{way_of_forming_genes[bound]}.txt'),
                'w', encoding="utf-8")
            result_file.write(
                f"Way of forming | Способ формирования:\n{way_of_forming_genes[bound]}\n")

            with tqdm(range(repeat), ncols=100, desc=f"{way_of_forming_genes[bound]}") as t:
                for _ in t:
                    individuals = []
                    if amount_of_methods == 4:
                        for value, method in zip(splitting_values, methods_chosen):
                            for _ in range(value):
                                if method == "Метод рандомного формирования":
                                    individuals.append(generate_individ(m, n, 1))
                                    continue
                                individuals.append(generate_individ(methods[method], n, 0, bound))
                    if amount_of_methods == 3:
                        for value, method in zip(splitting_values, methods_chosen):
                            for _ in range(value):
                                if method == "Метод рандомного формирования":
                                    individuals.append(generate_individ(m, n, 1))
                                    continue
                                individuals.append(generate_individ(methods[method], n, 0, bound))
                    if amount_of_methods == 2:
                        for value, method in zip(splitting_values, methods_chosen):
                            for _ in range(value):
                                if method == "Метод рандомного формирования":
                                    individuals.append(generate_individ(m, n, 1))
                                    continue
                                individuals.append(generate_individ(methods[method], n, 0, bound))
                    if amount_of_methods == 1:
                        for value, method in zip(splitting_values, methods_chosen):
                            if method == "Метод рандомного формирования":
                                individuals = [generate_individ(m, n, 1) for _ in range(z)]
                                continue
                            individuals = [generate_individ(methods[methods_chosen[0]], n, 0, bound) for _ in range(z)]

                    # Особи нулевого поколения (родители для будущего поколения):
                    listMax = []
                    for i, individual in enumerate(individuals):
                        load = count_load(individual, n, matrix)
                        listMax.append(load)
                    best_result, bestLoad_index = best_load(listMax)  # лучшая загрузка и (индекс лучшей особи - 1)
                    best_of_all_generations_result = best_result

                    # Генетический алгоритм
                    best_result = genetic_algorithm(
                        n=n, k=k, z=z, Pk=Pk, Pm=Pm,
                        best_result=best_result,
                        best_of_all_generations_result=best_of_all_generations_result,
                        matrix=matrix,
                        individuals=individuals
                    )

                    f.write(f"{best_result} ")
                    progress += 1
                    self._signal.emit(progress)

                f.close()
                with open(txt_file, 'r', encoding="utf-8") as f:
                    all_repeats_result = [int(elem) for elem in f.readline().split()]
                    results.append(
                        Fore.YELLOW + str(sum(all_repeats_result) / len(all_repeats_result)) + Style.RESET_ALL)
                work_time.append(Fore.GREEN + str(t.format_interval(t.format_dict['elapsed'])) + Style.RESET_ALL)
                # time.sleep(2)
            # Writing in files
            writing_in_files(
                result_file=result_file,
                work_time=work_time,
                results=results,
            )
            result_file.close()
    # Делаем гистограммы
    subprocess.call(['python', os.path.abspath('histogram.py')])

# signal_thread().start()
