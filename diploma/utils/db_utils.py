import datetime
import sqlite3
from io import BytesIO
from sqlite3 import Connection

from PyQt5.QtGui import QPixmap


def db_init(db_path) -> Connection:
    # Создание подключения к базе данных
    conn = sqlite3.connect(db_path)
    # Создание курсора
    cursor = conn.cursor()
    # выполнение запроса на выборку метаданных таблиц (проверка на существование таблицы)
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='all_method'")
    result = cursor.fetchone()
    # проверка наличия таблицы
    if not result:
        print("Таблицы не созданы. Создаём таблицы...")
        cursor.execute('''CREATE TABLE all_method
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data BLOB NOT NULL,
        result TEXT NOT NULL,
        elapsed_time TEXT NOT NULL,
        amount_of_methods TEXT NOT NULL,
        splitting_values TEXT NOT NULL,
        sorted_on TEXT NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        )''')
        conn.commit()
    return conn


def image2bytes_save(fig, ga_data, elapsed_time, data_dict, conn):
    cursor = conn.cursor()
    pic = fig.canvas.draw()
    # Сохраняем изображение в формате PNG
    buf = BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)
    image_converted = buf.read()
    if data_dict["sort_regenerate_matrix"] != "Без сортировки":
        sort_ = ('Отсортированно по убыванию', 'Отсортированно по возрастанию')[
            data_dict['sort_regenerate_matrix'] == 'Отсортированно по возрастанию']
    else:
        sort_ = "Без сортировки"
    cursor.execute(
        "INSERT INTO all_method ("
        "data, result, elapsed_time, amount_of_methods, splitting_values, sorted_on, created_at"
        ") VALUES (?, ?, ?, ?, ?, ?, ?)",
        (
            image_converted,
            " ".join(map(str, ga_data)),
            " ".join(map(str, elapsed_time)),
            data_dict["amount_of_methods"],
            " + ".join(
                [
                    f"{method} {value}%" for method, value in zip([
                    data_dict[f"{i}method"] for i in range(1, len(data_dict["splitting_values"]) + 1)],
                    data_dict["splitting_values"])
                ]
            ),
            sort_,
            datetime.datetime.now()
        )
    )
    conn.commit()
    image = BytesIO(image_converted)
    pixmap = QPixmap()
    pixmap.loadFromData(image.read())  # .scaled(width=107, height=109)
    pixmap_scaled = pixmap.scaled(159, 99)
    return pixmap_scaled


def select8_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM table_name ORDER BY id DESC LIMIT 8;
    ''')


def fill_labels_with_pics_and_data(sorted_up_pics, sorted_center_pics, sorted_down_pics, data_labels):
    # pics_container: list = []
    conn = sqlite3.connect('experiments_results/resultsdb.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='all_method'")
    result = cursor.fetchone()
    # проверка наличия таблицы
    if not result:
        print("Таблицы не созданы. Создаём таблицы...")
        cursor.execute('''CREATE TABLE all_method
        (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data BLOB NOT NULL,
        result TEXT NOT NULL,
        elapsed_time TEXT NOT NULL,
        amount_of_methods TEXT NOT NULL,
        splitting_values TEXT NOT NULL,
        sorted_on TEXT NOT NULL, 
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
        )''')
    conn.commit()
    cursor.execute('''
    SELECT data FROM all_method WHERE sorted_on = 'Отсортированно по возрастанию' ORDER BY id DESC LIMIT 8;
    ''')
    images_sorted_up = cursor.fetchall()
    cursor.execute('''
    SELECT data FROM all_method WHERE sorted_on = 'Отсортированно по убыванию' ORDER BY id DESC LIMIT 8;
    ''')
    images_sorted_center = cursor.fetchall()
    cursor.execute('''
        SELECT data FROM all_method WHERE sorted_on = 'Без сортировки' ORDER BY id DESC LIMIT 8;
        ''')
    images_sorted_down = cursor.fetchall()
    for image_data, label in zip(
            images_sorted_up, sorted_up_pics
    ):
        image = BytesIO(image_data[0])
        pixmap = QPixmap()
        pixmap.loadFromData(image.read())  # .scaled(width=107, height=109)
        pixmap_scaled = pixmap.scaled(159, 99)
        label.setPixmap(pixmap_scaled)
        # pics_container.append(pixmap_scaled)
    for image_data, label in zip(
            images_sorted_center, sorted_center_pics
    ):
        image = BytesIO(image_data[0])
        pixmap = QPixmap()
        pixmap.loadFromData(image.read())
        pixmap_scaled = pixmap.scaled(159, 99)
        label.setPixmap(pixmap_scaled)
        # pics_container.append(pixmap_scaled)
    for image_data, label in zip(
            images_sorted_down, sorted_down_pics
    ):
        image = BytesIO(image_data[0])
        pixmap = QPixmap()
        pixmap.loadFromData(image.read())
        pixmap_scaled = pixmap.scaled(159, 99)
        label.setPixmap(pixmap_scaled)
        # pics_container.append(pixmap_scaled)
    # Лучшие данные
    # Лучшие данные
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
        data_labels[0].setText(
            str("{:.2f}".format(sum(map(sum, result_sorted_up)) / len(result_sorted_up) / 4)))
        data_labels[1].setText(
            str("{:.2f}".format(sum(map(sum, time_sorted_up)) / len(time_sorted_up) / 4)))
    if data_sorted_down:
        result_sorted_down = list(map(lambda x: list(map(float, x[0].split())), data_sorted_down))
        time_sorted_down = list(map(lambda x: list(map(float, x[1].split())), data_sorted_down))
        data_labels[2].setText(
            str("{:.2f}".format(sum(map(sum, result_sorted_down)) / len(result_sorted_down) / 4)))
        data_labels[3].setText(
            str("{:.2f}".format(sum(map(sum, time_sorted_down)) / len(time_sorted_down) / 4)))
    if data_no_sort:
        result_no_sort = list(map(lambda x: list(map(float, x[0].split())), data_no_sort))
        time_no_sort = list(map(lambda x: list(map(float, x[1].split())), data_no_sort))
        data_labels[4].setText(
            str("{:.2f}".format(sum(map(sum, result_no_sort)) / len(result_no_sort) / 4)))
        data_labels[5].setText(
            str("{:.2f}".format(sum(map(sum, time_no_sort)) / len(time_no_sort) / 4)))
    # return pics_container


def collect_methods_bound_res(sort: str):
    conn = db_init("experiments_results/resultsdb.sqlite3")
    cursor = conn.cursor()

    # left_rise
    cursor.execute('''SELECT CAST(word AS REAL) AS word_float, splitting_values, result FROM (
                                  WITH split(word, str, splitting_values, result) AS (
                                      SELECT '', result||' ', splitting_values, result FROM all_method
                                      WHERE sorted_on = ?
                                      UNION ALL SELECT
                                      substr(str, 0, instr(str, ' ')),
                                      substr(str, instr(str, ' ') + 1),
                                      splitting_values,
                                      result
                                      FROM split WHERE str!=''
                                  ) SELECT word, splitting_values, result FROM split WHERE word!=''
                                  LIMIT 0, 
                                  (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?)
                              )
                              ORDER BY word_float; ''',
                   (sort, sort))
    left_rise = list(map(lambda x: (x[0], ''.join(
        [word[0].upper() if word.isalpha() else word for word in x[1].replace('-', ' ').split(' ')]), x[2]),
                         cursor.fetchall()))

    # right_rise
    cursor.execute('''SELECT CAST(word AS REAL) AS word_float, splitting_values, result FROM (
                                  WITH split(word, str, splitting_values, result) AS (
                                      SELECT '', result||' ', splitting_values, result FROM all_method
                                      WHERE sorted_on = ?
                                      UNION ALL SELECT
                                      substr(str, 0, instr(str, ' ')),
                                      substr(str, instr(str, ' ') + 1),
                                      splitting_values,
                                      result
                                      FROM split WHERE str!=''
                                  ) SELECT word, splitting_values, result FROM split WHERE word!=''
                                  LIMIT (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?), 
                                  (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?)
                              )
                              ORDER BY word_float; ''',
                   (sort, sort, sort))
    right_rise = list(map(lambda x: (x[0], ''.join(
        [word[0].upper() if word.isalpha() else word for word in x[1].replace('-', ' ').split(' ')]), x[2]),
                         cursor.fetchall()))

    # center_rise
    cursor.execute('''SELECT CAST(word AS REAL) AS word_float, splitting_values, result FROM (
                                  WITH split(word, str, splitting_values, result) AS (
                                      SELECT '', result||' ', splitting_values, result FROM all_method
                                      WHERE sorted_on = ?
                                      UNION ALL SELECT
                                      substr(str, 0, instr(str, ' ')),
                                      substr(str, instr(str, ' ') + 1),
                                      splitting_values,
                                      result
                                      FROM split WHERE str!=''
                                  ) SELECT word, splitting_values, result FROM split WHERE word!=''
                                  LIMIT (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?) * 2, 
                                  (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?)
                              )
                              ORDER BY word_float; ''',
                   (sort, sort, sort))
    center_rise = list(map(lambda x: (x[0], ''.join(
        [word[0].upper() if word.isalpha() else word for word in x[1].replace('-', ' ').split(' ')]), x[2]),
                         cursor.fetchall()))

    # random_rise
    cursor.execute('''SELECT CAST(word AS REAL) AS word_float, splitting_values, result FROM (
                                  WITH split(word, str, splitting_values, result) AS (
                                      SELECT '', result||' ', splitting_values, result FROM all_method
                                      WHERE sorted_on = ?
                                      UNION ALL SELECT
                                      substr(str, 0, instr(str, ' ')),
                                      substr(str, instr(str, ' ') + 1),
                                      splitting_values,
                                      result
                                      FROM split WHERE str!=''
                                  ) SELECT word, splitting_values, result FROM split WHERE word!=''
                                  LIMIT (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?) * 3, 
                                  (SELECT COUNT(*) FROM all_method WHERE sorted_on = ?)
                              )
                              ORDER BY word_float; ''',
                   (sort, sort, sort))
    random_rise = list(map(lambda x: (x[0], ''.join(
        [word[0].upper() if word.isalpha() else word for word in x[1].replace('-', ' ').split(' ')]), x[2]),
                         cursor.fetchall()))

    top_methods = []
    for result, method in zip(
            list(map(lambda x: x[0], left_rise)),
            list(map(lambda x: x[1], left_rise))
    ):
        value = [result, method]
        value[0] += right_rise[list(map(lambda x: x[1], right_rise)).index(method)][0]
        value[0] += center_rise[list(map(lambda x: x[1], center_rise)).index(method)][0]
        value[0] += random_rise[list(map(lambda x: x[1], random_rise)).index(method)][0]
        top_methods.append(
            (value[1],
             result,
             right_rise[list(map(lambda x: x[1], right_rise)).index(method)][0],
             center_rise[list(map(lambda x: x[1], center_rise)).index(method)][0],
             random_rise[list(map(lambda x: x[1], random_rise)).index(method)][0],
             value[0] / 4)
        )

    top_methods = sorted(list(map(lambda x: (x[0], x[1], x[2], x[3], x[4], round(x[-1], 2)), top_methods)),
                         key=lambda x: x[-1])

    return top_methods
