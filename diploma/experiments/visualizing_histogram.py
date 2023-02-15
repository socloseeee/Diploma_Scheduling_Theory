import matplotlib
import matplotlib.pyplot as plt
from decimal import *
import numpy as np
from copy import deepcopy
from colorama import Fore, init, Style, Back
import os
import time as t


str_methods = (
    "The method of minimal elements | Метод минмальных элементов",
    "The Plotnikov-Zverev method | Метод Плотникова-Зверева",
    "The method of squares | Метод квадратов",
    "The barrier method | Метод барьера"
)
is_create_way = input(
    "Select all or a specific method of forming (partitioning) the initial generation | "
    "Выбрать все или конкретный метод формирования (разбиения) начального поколения(1/any) > "
)
is_create_way = int(is_create_way) if is_create_way.isdigit() else is_create_way
if is_create_way != 1:
    create_way = int(
        input(
            "Way of forming the initial generation | Способ формирования начального поколения:\n"
            "100% random species | 100% рандомных особей(0)\n"
            "50% random + 50% determinate species | 50% рандомно + 50% детерминированных особей(1)\n"
            "25% random + 75% determinate species | 25% рандомно + 75% детерминированных особей(2)\n"
            "75% random + 25% determinate species | 75% рандомно + 25% детерминированных особей(3)\n"
            "100% determinate species | 100% детерминированных особей(4)\n"
            "> "
        )
    )
    if create_way == 0:
        bounds = 4
else:
    bounds = int(
        input(Fore.LIGHTCYAN_EX +
            "Ways to form genes | Способы формирования генов:\n"
            "Clearly centered between two borders in the processor | Чётко по центру между двумя границами в процессоре(0)\n"
            "Clearly on the left border in the processor | Чётко по левой границе в процессоре(1)\n"
            "Clearly on the right border in the processor | Чётко по правой границе в процессоре(2)\n"
            "Randomly between two boundaries in the processor | Рандомно между двумя границами в процессоре(3)\n"
            "> "
            + Style.RESET_ALL
        )
    )
if is_create_way != 1:
    file_formation_init = {
        0: '100r',
        1: '50r+50d',
        2: '25r+75d',
        3: '75r+25d',
        4: '100d'
    }
    file_formation_init = {create_way: file_formation_init[create_way]}
else:
    file_formation_init = {
        1: '50r+50d',
        2: '25r+75d',
        3: '75r+25d',
        4: '100d'
    }
file_formation_genes = {
    0: 'central_bound',
    1: 'left_bound',
    2: 'right_bound',
    3: 'random_bound',
    4: 'no_bounds'
}
colors_dict = {
     'The method of minimal elements | Метод минмальных элементов': 'royalblue',
     'The Plotnikov-Zverev method | Метод Плотникова-Зверева': 'darkorange',
     'The method of squares | Метод квадратов': 'forestgreen',
     'The barrier method | Метод барьера': 'firebrick'
}
axes, bar_container, data_all, elapsed_all, labels_all, all_way_of_forming = [], [], [], [], [], []
for way in file_formation_init.keys():
    data, elapsed_time, way_of_forming = [], [], ''
    with open(f"experiment_results/{file_formation_genes[bounds]}/result_{file_formation_init[way]}.txt", 'r', encoding="UTF-8") as file:
        file_data = file.readlines()
        # print(file_data)
        for i, elem in enumerate(file_data):
            if 'Way of forming | Способ формирования:' in elem:
                way_of_forming = file_data[i + 1]
                if way_of_forming not in all_way_of_forming:
                    all_way_of_forming.append(way_of_forming)
            elif 'Result | Результат: ' in elem:
                number = float(elem[elem.index(":") + 1:elem.index("\n")])
                data.append(number)
            elif 'Elapsed time | Время работы: ' in elem:
                time = elem[elem.index(":") + 1:elem.index("\n")]
                elapsed_time.append(time)
    for i, elem in enumerate(elapsed_time):
        min_, secs = [int(i) for i in elem.split(':')]
        elapsed_time[i] = min_ * 60 + secs

    # Сортировка для того чтоб графики не наслаивались:
    if way_of_forming != '100% random species | 100% рандомных особей\n':
        elapsed_index_sorted = sorted([(elapsed_time[i], i) for i in range(len(elapsed_time))], key=lambda x: x[0], reverse=True)
        new_data, new_elapsed, new_str_methods = [], [], []
        for i in range(len(elapsed_index_sorted)):
            index = elapsed_index_sorted[i][1]
            new_elapsed.append(elapsed_index_sorted[i][0])
            new_data.append(data[index])
            new_str_methods.append(str_methods[index])

    fig, ax = plt.subplots()
    fig.set_size_inches(14, 8)
    fig.canvas.set_window_title('Result')
    if way_of_forming != '100% random species | 100% рандомных особей\n':
        bars = [ax.bar(x, y, label=z, color=colors_dict[z], width=(data[-1] - data[0])) for x, y, z in zip(new_data, new_elapsed, new_str_methods)] #
        dict_, dict__ = {}, {}
        for i, x in enumerate(new_data):
            if x in dict_:
                dict_[x] += 1
            else:
                dict_[x] = 1
            if i > 0:
                if new_data[i-1] < new_data[i] and new_data[i-1] > new_data[i] - 0.05 and new_elapsed[i - 1] == new_elapsed[i]:
                    dict__[x] = 7.2 * (new_data[i] - new_data[i - 1])
                else:
                    dict__[x] = 0
            else:
                dict__[x] = 0
        # [plt.text(x - 0.05, (y + 0.35) + 0.2 * (dict_[x] > 1), f"{x} | {y}", bbox=dict(boxstyle="square")) for x, y in zip(new_data, new_elapsed)]
        for x, y, method in zip(new_data, new_elapsed, new_str_methods):
            dict_[x] -= 1
            plt.text(x - 0.05 + dict__[x], (y + 0.35) + 0.45 * dict_[x], f"{x} | {y}", bbox=dict(boxstyle="square", facecolor=colors_dict[method], edgecolor="black"))
    else:
        f = ax.bar(data[0], elapsed_time[0], label="Random formation method | Метод рандомного формирования", width=0.075)
        [plt.text(x - 0.032, y + 0.05, f"{x} | {y}", bbox=dict(boxstyle="square")) for x, y in zip(data, elapsed_time)]

    ax.legend(loc='best')

    orientation_gene_text = file_formation_genes[bounds]
    plt.title(
        f'Результаты при начальном формировании \n{way_of_forming}' +
        (way_of_forming != 0) * f'{orientation_gene_text[:orientation_gene_text.index("_")].capitalize()}'
    )

    # plt.xticks(data, data)
    plt.xlabel('Result | Результаты')
    plt.ylabel('Elapsed time | Затраченное время')

    if way_of_forming != '100% random species | 100% рандомных особей\n':
        elapsed_time = sorted(elapsed_time)
        data = sorted(data)
        plt.xlim(left=data[0] - (data[-1] - data[0]) / 20, right=data[-1] + (data[-1] - data[0]) / 20) # 0.05
        plt.ylim(bottom=elapsed_time[0] - 1, top=elapsed_time[-1] + 1)
    else:
        plt.xlim(left=data[0] - 0.45, right=data[0] + 0.45)
        plt.ylim(bottom=elapsed_time[0] - 1, top=elapsed_time[-1] + 1)

    plt.savefig(f"histograms/{file_formation_genes[bounds]}/Result_{file_formation_init[way]}")
    if is_create_way == 1:
        axes.append(ax), bar_container.append(bars), data_all.append(new_data), elapsed_all.append(new_elapsed)
        labels_all.append(new_str_methods)
    plt.close() if is_create_way == 1 else plt.show()

if is_create_way == 1:
    fig, axes = plt.subplots(2, 2)
    fig.set_size_inches(24, 13.5)
    # axes.set_size_inches
    #fig.subplots_adjust(left=0.07, bottom=0.04, top=0.97, hspace=0.13)
    # legends = [] * len(str_methods)
    for i, row in enumerate(axes):
        for j, col in enumerate(row):
            axes[i][j].set_title(
                f'{all_way_of_forming[i + j][:all_way_of_forming[i + j].index("|") - 1]}',
                bbox=dict(boxstyle="square", facecolor='darkviolet', edgecolor="black"),
                fontsize = 11
            )
            max_data, min_data = max(data_all[i + j]), min(data_all[i + j])
            max_elapsed, min_elapsed = max(elapsed_all[i + j]), min(elapsed_all[i + j])
            [axes[i][j].bar(x, y, label=z, color=colors_dict[z], width=(max_data - min_data) / 8) for x, y, z in zip(data_all[i + j], elapsed_all[i + j], labels_all[i + j])]
            axes[i][j].set_xlim(left=min_data - (max_data - min_data) / 10, right=max_data + (max_data - min_data) / 10)
            axes[i][j].set_ylim(bottom=min_elapsed - 1, top=max_elapsed + 1)
            [axes[i][j].text(x - 0.05, y - 0.15, f"{x} | {y}",
                     bbox=dict(boxstyle="square", facecolor=colors_dict[method], edgecolor="black")) for x, y, method in zip(data_all[i + j], elapsed_all[i + j], labels_all[i + j])]
            # axes[i][j].legend(loc='best')
            #axes[i][j].xlabel('Result | Результаты')
            #axes[i][j].ylabel('Elapsed time | Затраченное время')
            # axes[i][j].set_title()
    h, l = axes[0][0].get_legend_handles_labels()
    fig.legend(handles=h, labels=l, loc='upper left')
    fig.suptitle(f'{orientation_gene_text[:orientation_gene_text.index("_")].capitalize()}')
    plt.savefig(f"histograms/{file_formation_genes[bounds]}/Result_all")
    # t.sleep(1)
    plt.show()
    # os.startfile(f"C:/Users/Богдан/PycharmProjects/everistika/diploma/experiments/histograms/{file_formation_genes[bounds]}/Result_all.png")
