import matplotlib
import matplotlib.pyplot as plt
from decimal import *
import numpy as np
from copy import deepcopy
from colorama import Fore, init, Style, Back
import os

str_methods = (
    "The method of minimal elements | Метод минмальных элементов",
    "The Plotnikov-Zverev method | Метод Плотникова-Зверева",
    "The method of squares | Метод квадратов",
    "The barrier method | Метод барьера"
)
colors_dict = {
     'central': 'royalblue',
     'left': 'darkorange',
     'right': 'forestgreen',
     'random': 'firebrick'
}
bounds = ['central', 'left', 'right', 'random']
fig, axes = plt.subplots(2, 2)
axes_dict = {
    'central': axes[0][0],
    'left': axes[0][1],
    'right': axes[1][0],
    'random': axes[1][1]
}
fig.set_size_inches(19, 9.5)
for bound in bounds:
    with open(f"experiment_results/{bound}_bound/all_result.txt", 'r', encoding="utf-8") as f:
        data = f.readlines()
        methods_data = [[float(el) for el in elem[1:-2].split(', ')] for elem in data[data.index('Methods summary\n') + 1:data.index('Methods summary\n') + 1 + len(bounds)]]
        genes_data = [[float(el) for el in elem[1:-2].split(', ')] for elem in data[data.index('Genes_summary\n') + 1:data.index('Genes_summary\n') + 1 + len(bounds)]]
    axes_dict[bound].set_title(
        f'{bound}',
        bbox=dict(boxstyle="square", facecolor='darkviolet', edgecolor="black"),
        fontsize=11
    )
    [
        axes_dict[bound].bar(
            [elem[0] for elem in methods_data][i],
            [elem[1] for elem in methods_data][i],
            label=str_methods[i],
            color=colors_dict[[elem for elem in colors_dict.keys()][i]],
            width=(max([elem[0] for elem in methods_data]) - min([elem[0] for elem in methods_data]))/10
        )
        for i in range(len(methods_data))
    ]
    axes_dict[bound].set_xlabel('Result | Результаты')
    axes_dict[bound].set_ylabel('Elapsed time | Затраченное время')
    axes_dict[bound].set_xlim(right=max([elem[0] for elem in methods_data]) + 10, left=min([elem[0] for elem in methods_data]) - 10)  # 0.05
    axes_dict[bound].set_ylim(bottom=min([elem[1] for elem in methods_data]) - 10, top=max([elem[1] for elem in methods_data]) + 10)
    print(methods_data, genes_data)
h, l = axes[0][0].get_legend_handles_labels()
fig.legend(handles=h, labels=l, loc='upper left')
plt.savefig("all_bounds_results")
plt.show()