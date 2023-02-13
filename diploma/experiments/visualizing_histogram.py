import matplotlib
import matplotlib.pyplot as plt
from decimal import *
import numpy as np
from copy import deepcopy


data, elapsed_time, way_of_forming = [], [], ''
str_methods = (
    "The method of minimal elements | Метод минмальных элементов",
    "The Plotnikov-Zverev method | Метод Плотникова-Зверева",
    "The method of squares | Метод квадратов",
    "The barrier method | Метод барьера"
)
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
bounds = int(
    input(
        "Ways to form genes | Способы формирования генов:\n"
        "Clearly centered between two borders in the processor | Чётко по центру между двумя границами в процессоре(0)\n"
        "Clearly on the left border in the processor | Чётко по левой границе в процессоре(1)\n"
        "Clearly on the right border in the processor | Чётко по правой границе в процессоре(2)\n"
        "Randomly between two boundaries in the processor | Рандомно между двумя границами в процессоре(3)\n"
        "> "
    )
) if create_way != 0 else 4
file_formation_init = {
    0: '100r',
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
colors = ('blue', 'orange', 'green', 'red')
with open(f"experiment_results/{file_formation_genes[bounds]}/result_{file_formation_init[create_way]}.txt", 'r', encoding="UTF-8") as file:
    file_data = file.readlines()
    # print(file_data)
    for i, elem in enumerate(file_data):
        if 'Way of forming | Способ формирования:' in elem:
            way_of_forming = file_data[i + 1]
        elif 'Result | Результат: ' in elem:
            number = float(elem[elem.index(":") + 1:elem.index("\n")])
            data.append(number)
        elif 'Elapsed time | Время работы: ' in elem:
            time = elem[elem.index(":") + 1:elem.index("\n")]
            elapsed_time.append(time)
for i, elem in enumerate(elapsed_time):
    min, secs = [int(i) for i in elem.split(':')]
    elapsed_time[i] = min * 60 + secs

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
    f1, f2, f3, f4 = [ax.bar(x, y, label=z, width=0.75) for x, y, z in zip(new_data, new_elapsed, new_str_methods)] # 0.075 + (data[-1] - data[0]) / 20
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

    print(dict_, dict__)
    # [plt.text(x - 0.05, (y + 0.35) + 0.2 * (dict_[x] > 1), f"{x} | {y}", bbox=dict(boxstyle="square")) for x, y in zip(new_data, new_elapsed)]
    for x, y, color_ in zip(new_data, new_elapsed, colors):
        dict_[x] -= 1
        plt.text(x - 0.05 + dict__[x], (y + 0.35) + 0.45 * dict_[x], f"{x} | {y}", bbox=dict(boxstyle="square", facecolor=color_, edgecolor="black"))
else:
    f = ax.bar(data[0], elapsed_time[0], label="Random formation method | Метод рандомного формирования", width=0.075)
    [plt.text(x - 0.05, y + 0.35, f"{x} | {y}", bbox=dict(boxstyle="square")) for x, y in zip(data, elapsed_time)]

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

plt.savefig(f"histograms/{file_formation_genes[bounds]}/Result_{file_formation_init[create_way]}")
plt.show()
