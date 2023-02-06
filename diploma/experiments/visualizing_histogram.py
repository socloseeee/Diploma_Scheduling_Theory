import matplotlib
import matplotlib.pyplot as plt
from decimal import *
import numpy as np
from copy import deepcopy

data, elapsed_time = [], []
str_methods = (
    "The method of minimal elements | Метод минмальных элементов:",
    "The Plotnikov-Zverev method | Метод Плотникова-Зверева:",
    "The method of squares | Метод квадратов:",
    "The barrier method | Метод барьера:"
)
with open("result.txt", 'r', encoding="UTF-8") as file:
    file_data = file.readlines()
    for elem in file_data:
        if 'Result | Результат: ' in elem:
            number = float(elem[-6:-1])
            data.append(number)
        elif 'Elapsed time | Время работы: ' in elem:
            time = elem[-5:-1]
            elapsed_time.append(time)
for i, elem in enumerate(elapsed_time):
    min, secs = [int(i) for i in elem.split(':')]
    elapsed_time[i] = min * 60 + secs
# print(elapsed_time)
# [plt.hist(result, bins=20, label=str_method) for result, str_method in zip(data, str_methods)]
# for result, times, str_method in zip(data, elapsed_time, str_methods):
#     plt.hist(result, label=str_method)
# elapsed_time = sorted(elapsed_time)
# plt.yticks([int(elem[-2:]) for elem in elapsed_time])
fig, ax = plt.subplots()
fig.set_size_inches(8, 5.5)
fig.canvas.set_window_title('Result')
f1, f2, f3, f4 = [ax.bar(x, y, label=z, width=0.025) for x, y, z in zip(data, elapsed_time, str_methods)]
# print(ax)
# print(f1)
# wid = 0.025
# f1.set(width=wid, x=data[0], color='g')
# f2.set(width=wid, x=data[1], color='b')
# f3.set(width=wid, x=data[2], color='m')
# f4.set(width=wid, x=data[3], color='r')
ax.legend()
# print(data)
plt.title('Результаты при начальном формировании \n(50 рандомно + 50 детерминированно)')
# plt.xticks(data, data)
plt.xlabel('Result | Результаты')
data = sorted(data)
plt.xlim(left=data[0] - 0.05, right=data[-1] + 0.05)
# plt.legend(f1, str_methods[0])
print(data)
# plt.ylim(elapsed_time[0], elapsed_time[-1])
plt.ylabel('Elapsed time | Затраченное время')
# f = plt.figure()
# ax = f.add_subplot(1, 1, 1)
# f1, f2, f3, f4 = ax.bar(data, elapsed_time)
# wid = 0.01
# print(data)
# f1.set(width=wid)
# f1.set(x=data[0])
# f2.set(width=wid)
# f2.set(x=data[1])
# f3.set(width=wid)
# f3.set(x=data[2])
# f4.set(width=wid)
# f4.set(x=data[3])
# print(f1, f2, f3, f4)
plt.savefig("Result")
plt.show()