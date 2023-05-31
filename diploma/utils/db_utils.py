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
    img = fig.savefig(buf, format='png')
    buf.seek(0)
    image_converted = buf.read()

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
            ('Отсортированно по убыванию', 'Отсортированно по возрастанию')[data_dict["sorted_up"]],
            datetime.datetime.now()
        )
    )
    conn.commit()
    image = BytesIO(image_converted)
    pixmap = QPixmap()
    pixmap.loadFromData(image.read())  # .scaled(width=107, height=109)
    pixmap_scaled = pixmap.scaled(145, 109)
    return pixmap_scaled


def select8_from_db(conn):
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM table_name ORDER BY id DESC LIMIT 8;
    ''')


def fill_labels_with_pics_and_data(sorted_up_pics, sorted_down_pics, data_labels):
    pics_container: list = []
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
    images_sorted_down = cursor.fetchall()
    for image_data, label in zip(
            images_sorted_up, sorted_up_pics
    ):
        image = BytesIO(image_data[0])
        pixmap = QPixmap()
        pixmap.loadFromData(image.read())  # .scaled(width=107, height=109)
        pixmap_scaled = pixmap.scaled(145, 109)
        label.setPixmap(pixmap_scaled)
        pics_container.append(pixmap_scaled)
    for image_data, label in zip(
            images_sorted_down, sorted_down_pics
    ):
        image = BytesIO(image_data[0])
        pixmap = QPixmap()
        pixmap.loadFromData(image.read())
        pixmap_scaled = pixmap.scaled(145, 109)
        label.setPixmap(pixmap_scaled)
        pics_container.append(pixmap_scaled)
    # Лучшие данные
    cursor.execute('''
                                    SELECT result, elapsed_time FROM all_method WHERE sorted_on = 'Отсортированно по возрастанию';
                                    ''')
    data_sorted_up = cursor.fetchall()
    cursor.execute('''
                                    SELECT result, elapsed_time FROM all_method WHERE sorted_on = 'Отсортированно по убыванию';
                                    ''')
    data_sorted_down = cursor.fetchall()
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
    return pics_container
