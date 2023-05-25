import json


class DataApp:
    json_data: dict = []
    try:
        with open("experiments_results/data.json", 'r') as f:
            json_data = json.load(f)
    except Exception as e:
        print(e)
    if json_data:
        data = json_data
    else:
        data = {
            "repetitions": 100,
            "m": 10,
            "n": 5,
            "T1": 20,
            "T2": 50,
            "z": 100,
            "k": 30,
            "Pk": 99,
            "Pm": 99,
            "matrix": "23 20 29 26 30\n25 34 29 27 23\n35 21 22 27 39\n34 21 28 46 40\n26 42 42 32 28\n34 47 27 43 "
                      "20\n41 28 22 48 35\n48 24 37 33 44\n42 37 39 41 33\n38 27 47 42 50",
            "newline": "\n",
            "ui_matrix_size": 13,
            "methods_amount": 3,
            "ways_of_formation": 3,
            "1method": "Метод Плотникова-Зверева",
            "amount_of_methods": 1,
            "2method": "Метод минимальных элементов",
            "splitting_values": [
                0,
                100
            ],
            "3method": "Метод минимальных элементов",
            "bound": 2
        }
