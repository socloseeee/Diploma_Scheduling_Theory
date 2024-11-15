import os
import json
import matplotlib.pyplot as plt

from diploma.utils.db_utils import db_init, image2bytes_save


def run():
    # инициализация бд
    conn = db_init("experiments_results/resultsdb.sqlite3")

    # отрисовка результатов
    with open(os.path.abspath('experiments_results/data.json'), 'r', encoding='UTF-8') as f:
        data = json.load(f)

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

    sorted_ = None
    if data["sort_regenerate_matrix"] == "Отсортированно по возрастанию":
        sorted_ = "sorted_up"
    if data["sort_regenerate_matrix"] == "Отсортированно по убыванию":
        sorted_ = "sorted_down"

    axes_data = []
    for bound in way_of_forming_genes.values():
        if data['sort_regenerate_matrix'] != "Без сортировки":
            file_path = os.path.abspath(
                        f"experiments_results/bounds_data/{sorted_}/summary_results/result_{bound}.txt"
                    )
        else:
            file_path = os.path.abspath(
                        f"experiments_results/bounds_data/no_sort/summary_results/result_{bound}.txt"
                    )
        with open(file_path, 'r', encoding="UTF-8") as file:
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

    value = " + ".join(
        [
            f"{method} {value}%" for method, value in zip([
            data[f"{i}method"] for i in range(1, len(data["splitting_values"]) + 1)],
            data["splitting_values"])
        ]
    )
    labels_pie = value.split(' + ')
    x = list(map(lambda x: int(x[x.rindex(' '):]), value.split('%')[:-1]))

    fig, (ax, ax1) = plt.subplots(1, 2)
    fig.set_size_inches(14, 8)
    fig.canvas.setWindowTitle('Result')
    ax.bar(
        x=ga_data,
        height=elapsed_time,
        label=all_way_of_forming,
        color=colors_dict.values(),
        width=(max(ga_data) - min(ga_data)) / 10
    )
    [ax.text(
        x,
        y,
        f"{x} | {y}",
        bbox=dict(boxstyle="square",
                  facecolor=color,
                  edgecolor="black")
    ) for x, y, color in zip(ga_data, elapsed_time, colors_dict.values())]
    h, l = ax.get_legend_handles_labels()
    l = list(map(lambda x, y, z: (x[:-1], y, z), l, ga_data, elapsed_time))
    ax.legend(handles=h, labels=l, loc='best')
    ax.set_title('Результат работы по границам')
    ax.set_xlabel('Результат')
    ax.set_ylabel('Затраченное время')

    plt.xlabel('Result | Результаты')
    plt.ylabel('Elapsed time | Затраченное время')
    explode = [0.1 for _ in range(len(data["splitting_values"]))]
    wedges, texts, autotexts = ax1.pie(
        x=x,
        colors=colors_dict.values(),
        autopct='%1.1f%%',
        shadow=True,
        radius=3,
        explode=explode,
        wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"},
        frame=True,
        textprops={'fontsize': 12}
    )
    ax1.set_position([0.345, 0.1, 0.775, 0.775])
    ax1.legend(wedges, labels_pie)
    ax1.set_title('Разбиение начального поколения')

    # Добавление диаграммы pie на новые оси
    ax1.add_artist(wedges[0])
    ax1.axis('off')
    if data['sort_regenerate_matrix'] != 'Без сортировки':
        fig.suptitle(
            f'Результаты при начальном формировании \n'
            f'Матрица {data["sort_regenerate_matrix"].lower()}'
        )
        img_path = os.path.abspath(
            f"experiments_results/histograms/{sorted_}/result_{('sorted_down', 'sorted_up')[data['sort_regenerate_matrix'] == 'Отсортированно по убыванию']}"
        )
    else:
        fig.suptitle(
            f'Результаты при начальном формировании \n'
            f'c неотсортированной матрицей'
        )
        img_path = os.path.abspath(
            f"experiments_results/histograms/no_sort/result_no_sort"
        )

    plt.savefig(img_path)

    # Сохранение картинки в БД
    img = image2bytes_save(
        fig=fig,
        ga_data=ga_data,
        elapsed_time=elapsed_time,
        data_dict=data,
        conn=conn
    )
    conn.close()
    # plt.show()
    return img

# run()
