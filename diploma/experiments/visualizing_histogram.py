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
        bars = [ax.bar(x, y, label=z, color=colors_dict[z], width=(max(data) - min(data))/10) for x, y, z in zip(new_data, new_elapsed, new_str_methods)] #
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
    fig.set_size_inches(19, 9.5)
    # axes.set_size_i
    k = 0
    for i, row in enumerate(axes):
        for j, col in enumerate(row):
            axes[i][j].set_title(
                f'{all_way_of_forming[i + j + k][:all_way_of_forming[i + j + k].index("|") - 1]}',
                bbox=dict(boxstyle="square", facecolor='darkviolet', edgecolor="black"),
                fontsize = 11
            )
            max_data, min_data = max(data_all[i + j + k]), min(data_all[i + j + k])
            max_elapsed, min_elapsed = max(elapsed_all[i + j + k]), min(elapsed_all[i + j + k])
            [axes[i][j].bar(x, y, label=z, color=colors_dict[z], width=(max_data - min_data) / 8) for x, y, z in zip(data_all[i + j + k], elapsed_all[i + j + k], labels_all[i + j + k])]
            axes[i][j].set_xlim(left=min_data - (max_data - min_data) / 10, right=max_data + (max_data - min_data) / 10)
            axes[i][j].set_ylim(bottom=min_elapsed - 1, top=max_elapsed + 1)
            [axes[i][j].text(x - 0.05, y - 0.15, f"{x} | {y}",
                     bbox=dict(boxstyle="square", facecolor=colors_dict[method], edgecolor="black")) for x, y, method in zip(data_all[i + j + k], elapsed_all[i + j + k], labels_all[i + j + k])]
            # axes[i][j].legend(loc='best')
            #axes[i][j].xlabel('Result | Результаты')
            #axes[i][j].ylabel('Elapsed time | Затраченное время')
            # axes[i][j].set_title()
        k += 1
    boundaries = {
        0: '|__________x__________|',
        1: 'x_____________________|',
        2: '|_____________________x',
        3: 'xxxxxxxxxxxxxxxxxxxxxxx'
    }
    h, l = axes[0][0].get_legend_handles_labels()
    # l = [f"{elem} ({data_all[0]} | {elapsed_all[0]})" for i, elem in enumerate(l)]
    fig.legend(handles=h, labels=l, loc='upper left')
    fig.suptitle(
        f'Location between two processor boundaries: \n'
        f'{orientation_gene_text[:orientation_gene_text.index("_")].capitalize()}\n'
        f'{boundaries[bounds]}\n'
       # f'{data_all[0]} | {elapsed_all[0]}'
    )
    plt.savefig(f"histograms/{file_formation_genes[bounds]}/Result_all")
    # t.sleep(1)
    # fig = plt.figure(figsize=(3.5, 2))
    # location = (
    #     0.5, 0.4, 0.3, 0.2
    # )
    # [fig.text(0, y, f"{row_data} {row_time}") for y, row_data, row_time in zip(location, data_all, elapsed_all)]
    fig, ax = plt.subplots()
    # fig.set_figheight(8)
    # fig.set_figwidth(8)
    ax.axis('tight')
    ax.axis('off')
    row = ["50r+50d", "25r+75d", "75r+25d", "100d", "result"]
    col = ["Minimum", "Plt-Zverev", "Square", "Barrier", "result"]
    cellData = [[0 for _ in range(len(data_all[0]))] for __ in range(len(data_all))]

    for row_label, row_data, row_elapsed, row_cell in zip(labels_all, data_all, elapsed_all, cellData):
        for i, check_method in enumerate(str_methods):
            index = row_label.index(check_method)
            row_cell[i] = (row_data[index], row_elapsed[index])
    summary_results_method = [(0, 0) for _ in range(len(str_methods))]
    summary_results_genes = [(0, 0) for _ in range(len(str_methods))]
    for i in range(len(cellData)):
        for j in range(len(cellData)):
            summary_results_method[i] = (round(summary_results_method[i][0] + cellData[j][i][0], 2),
                                         round(summary_results_method[i][1] + cellData[j][i][1], 2))
            summary_results_genes[i] = (round(summary_results_genes[i][0] + cellData[i][j][0], 2),
                                         round(summary_results_genes[i][1] + cellData[i][j][1], 2))
    print(summary_results_genes)
    print(cellData)
    for i, elem in enumerate(cellData):
        elem.append(summary_results_genes[i])
    cellData.append(summary_results_method)
    cellData[-1].append('')
    ax.table(
        cellText=cellData, cellLoc='center', loc='center',
        rowColours=["palegreen"] * 5, colColours=["palegreen"] * 5, colLabels=col, rowLabels=row# colWidths=[0.1, 0.1, 0.1, 0.1],
    )
    # for i, row in enumerate(axes):
    #     for j, col in enumerate(row):
    #         ax[i][j].axis('tight')
    #         ax[i][j].axis('off')
    #         ax[i][j].table(
    #             cellText=data_all, cellLoc='center', rowLabels=labels_all[i + j],
    #             #rowColours=["palegreen"] * 4, colLabels=col, colColours=["palegreen"] * 4, loc='center'
    #         )
    #         ax[i][j].set_title('Матрица заданий', family='fantasy', size=15)
    plt.savefig(f"histograms/{file_formation_genes[bounds]}/results.png")
    plt.show()
    # os.startfile(f"C:/Users/Богдан/PycharmProjects/everistika/diploma/experiments/histograms/{file_formation_genes[bounds]}/Result_all.png")
