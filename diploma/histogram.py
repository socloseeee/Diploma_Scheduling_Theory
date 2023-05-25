import os
import json
import matplotlib.pyplot as plt

import numpy as np

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
methods_chosen = [data["1method"], data["2method"], data["3method"], data["4method"]]

way_of_forming_genes = {
    0: "left_bound",
    1: "right_bound",
    2: "central_bound",
    3: "random_bound",
}
colors_dict = {
    "left_bound": 'royalblue',
    "right_bound": 'darkorange',
    "central_bound": 'firebrick',
    "random_bound": 'purple'
}

sorted_ = "sorted_up" if data["sorted_up"] else "sorted_down"

axes_data = []
for bound in way_of_forming_genes.values():
    with open(
            os.path.abspath(
                f"experiments_results/bounds_data/{sorted_}/summary_results/result_{bound}.txt"
            ), 'r', encoding="UTF-8") as file:
        file_data = file.readlines()
        all_way_of_forming = []
        ga_data, elapsed_time, way_of_forming = [], [], ''
        for i, elem in enumerate(file_data):
            if 'Way of forming | Способ формирования:' in elem:
                way_of_forming = file_data[i + 1]
                if way_of_forming not in all_way_of_forming:
                    all_way_of_forming = way_of_forming
            elif 'Result | Результат: ' in elem:
                number = float(elem[elem.index(":") + 1:elem.index("\n")])
                ga_data = number
            elif 'Elapsed time | Время работы: ' in elem:
                time = elem[elem.index(":") + 1:elem.index("\n")]
                elapsed_time.append(time)
    for i, elem in enumerate(elapsed_time):
        min_, secs = [int(i) for i in elem.split(':')]
        elapsed_time[i] = min_ * 60 + secs
    axes_data.append((all_way_of_forming, ga_data, elapsed_time[0]))

# Cортировка для того, чтоб графики не наслаивались
axes_data = list(sorted(axes_data, key=lambda x: x[2], reverse=True))
all_way_of_forming = list(map(lambda x: x[0], axes_data))
ga_data = list(map(lambda x: x[1], axes_data))
elapsed_time = list(map(lambda x: x[2], axes_data))
fig, ax = plt.subplots()
fig.set_size_inches(14, 8)
fig.canvas.setWindowTitle('Result')
print(axes_data)
bar = ax.bar(
    x=ga_data,
    height=elapsed_time,
    label=all_way_of_forming,
    color=colors_dict.values(),
    width=(max(ga_data) - min(ga_data)) / 10
)
[plt.text(
    x,
    y,
    f"{x} | {y}",
    bbox=dict(boxstyle="square",
              facecolor=color,
              edgecolor="black")
) for x, y, color in zip(ga_data, elapsed_time, colors_dict.values())]
h, l = ax.get_legend_handles_labels()
l = list(map(lambda x, y, z: (x[:-1], y, z), l, ga_data, elapsed_time))
ax.legend(handles=h, labels=l, loc='lower center')
plt.title(
    f'Результаты при начальном формировании \n'
    f'c отсортированной по {("убыванию", "возрастанию")[data["sorted_up"]]} матрицей'
)
plt.xlabel('Result | Результаты')
plt.ylabel('Elapsed time | Затраченное время')
plt.savefig(
    os.path.abspath(
        f"experiments_results/histograms/{sorted_}/result_{('sorted_down', 'sorted_up')[data['sorted_up']]}"
    )
)
# plt.show()
