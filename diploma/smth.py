import random
import copy
from copy import deepcopy
from random import choice as c, randint as r
from colorama import Fore, init, Style, Back

init(autoreset=True)

# Генерируем матрицу заданий
def generate_matrix(m, n, T1, T2):
    return [[r(T1, T2) for j in range(n)] for i in range(m)]

# Генерируем особь (рандомно/детерминированно):
def generate_individ(m, n, flag):
    individ = []
    if flag == 0:
        for row in m:
            for i, elem in enumerate(row):
                if '\x1b[31m' in str(elem):  # '\x1b[31m' - идентификатор цвета
                    # individ.append(i * (255 // n) + (255 // n) // 2)  # чётко по центру между двумя границами в процессоре
                    # individ.append(i * (255 // n))  # чётко по левой границе в процессоре
                    # individ.append(i * (255 // n) + (255 // n))  # чётко по правой границе в процессоре
                    individ.append(r(i * (255 // n) + 1, i * (255 // n) + (255 // n)))  # рандомно между двумя границами в процессоре
    else:
        return [r(1, 255) for _ in range(m)]
    return individ

# Считаем загрузки:
def count_load(individ, n, m, tasks, t=255):
    load_result = [0 for _ in range(n)]
    proc = [i for i in range(t//n, t + t//n, int(t//n))]
    for j, gen in enumerate(individ):
        for i in range(n):
            if gen <= proc[i]:
                load_result[i] += tasks[j][i]
                break
    return load_result

# Считаем лучшую загрузку для каждой особи:
def best_load(max_loads):
    result = [max(el) for el in max_loads]
    return (min(result), result.index(min(result)))

# Двухточечный кроссовер
def crossover(parent1, parent2):
    T1 = r(1, len(parent1) - 1)
    T2 = r(1, len(parent1) - 1)
    while T2 == T1:
        T2 = r(1, len(parent1) - 1)
    if T1 > T2:
        T1, T2 = T2, T1
    f.write(f'T: {T1}, {T2}\n')
    #print(f'parents({T1},{T2}):\n{parent1}\n{parent2}')
    child1, child2 = parent1[:T1] + parent2[T1:T2+1] + parent1[T2+1:], parent2[:T1] + parent1[T1:T2+1] + parent2[T2+1:],
    #print(f'children:\n{child1}\n{child2}')
    return child1, child2

# Двухточечная мутация
def mutation(child, Pm):
    child_copy = deepcopy(child)
    child_genes = [e for e in child_copy]
    f.write(f'Genes before: {" ".join([str(e) for e in child_genes])}')
    gen = c(child_genes)
    while r(1, 100) < Pm:
        gen = c(child_genes)
    f.write(f'\nGene: {gen}\n')
    that_gen = deepcopy(gen)
    binary_gen = '00000000'
    for j in range(len(binary_gen)):
        binary_gen = binary_gen[:j] + str(gen % 2) + binary_gen[j + 1:]
        gen //= 2
    binary_gen = binary_gen[::-1]
    f.write(f'Its binary form: {binary_gen}')
    binary_gen = list(binary_gen)
    index1 = r(0, len(binary_gen)-1)
    index2 = r(0, len(binary_gen)-1)
    if binary_gen.count(binary_gen[0]) != len(binary_gen):
        while index2 == index1 or binary_gen[index1] == binary_gen[index2]: # чтоб 0 менялся с 1 и индексы не одинаковые
            index2 = r(0, len(binary_gen)-1)
    binary_gen[index1], binary_gen[index2] = binary_gen[index2], binary_gen[index1]
    binary_gen = "".join(binary_gen)
    f.write(f'\nChanged bit: {binary_gen}\nNew number: {int(binary_gen, 2)}\n')
    child_copy = [genes if genes != that_gen else int(binary_gen, 2) for genes in child_copy]
    f.write(f'Genes after: {" ".join([str(e) for e in child_copy])}\n')
    return child_copy

# Список цветов
colors = [
    'RED',
    'GREEN',
    'YELLOW',
    'BLUE',
    'MAGENTA',
    'CYAN',
    'WHITE'
]

# Метод отображения
def show(matrix) -> None:
    for j in matrix:
        for i in j:
            f.write(f"{i}  ")
        f.write("\n")

# Отображаем данные
def show_generation(txt_file, amount_of_generations, word):
    with open(txt_file, 'r', encoding="utf-8") as file:
        chosen = 0
        while True:
            file.seek(0)
            while True:
                num = input(
                    '\nChoose what you want to display | Выберите что хотите отобразить:'
                    '\nDisplay generation from GA | Вывести поколение из ГА(0)'
                    '\nOrigin matrix | Искомый массив(1)'
                    '\nSorted matrix | Отсортированный массив(2)'
                    '\nMinimum element method | Метод минимальных элементов(3)'
                    '\nPlotnikov-Zverev method | Метод Плотникова-Зверева(4)'
                    '\nSquare method | Метод квадратов(5)'
                    '\nBarrier method | Метод барьера(6)'
                    '\nResult of all methods | Результат работы всех методов(7)'
                    f'\nCompare schedule of init and final generation | Сравнить расписания при начальном поколении сформированном при {word} и конечном(8)'
                    '\n>'
                )
                if num.isdigit() and 0 <= int(num) <= 8 or num == 'exit':
                    if int(num) == 0:
                        chosen = input('Choose generation to show (exit - to quit programm) > ')
                        if chosen.isdigit() and 0 <= int(chosen) <= amount_of_generations or chosen == 'exit':
                            chosen = f"{chosen} GENERATION | {chosen}-е ПОКОЛЕНИЕ >\n"
                            finish = "#\n"
                            break
                        else:
                            print('Incorrect input! | Неправильный ввод!')
                        chosen_generation = f"{num} GENERATION | {num}-е ПОКОЛЕНИЕ >\n"
                    elif int(num) == 1:
                        chosen = f"Origin matrix | Искомый массив:\n"
                        finish = "#\n"
                    elif int(num) == 2:
                        chosen = f"Sums of row elements | Суммы элементов строк:\n"
                        finish = "##\n"
                    elif int(num) == 3:
                        chosen = f"Minimum element method | Метод минимальных элементов:\n"
                        finish = "#\n"
                    elif int(num) == 4:
                        chosen = f"Plotnikov-Zverev method | Метод Плотникова-Зверева(обычный):\n"
                        finish = "#\n"
                    elif int(num) == 5:
                        chosen = f"Square method | Метод квадратов:\n"
                        finish = "#\n"
                    elif int(num) == 6:
                        chosen = f"Barrier method | Метод барьера:\n"
                        finish = "#\n"
                    elif int(num) == 7:
                        chosen = f"Result of all methods | Результат работы всех методов:\n"
                        finish = "#\n"
                    elif int(num) == 8:
                        chosen = f"Init generation | Начальное поколение при {word}:\n"
                        finish = "#\n"
                    break
                else:
                    print('Incorrect input! | Неправильный ввод!')
                print()
            if num == 'exit':
                break
            if chosen != 0:
                generation_tree_data = file.readlines()
                new_slice = generation_tree_data[generation_tree_data.index(chosen):]
                this = new_slice[:new_slice.index(finish)]
                print("".join(this))
            else:
                print(chosen)
        print('Good Bye!')


# Открываем файл для записи:
txt_file = 'data.txt'
f = open(txt_file, 'w', encoding="utf-8")

# Генерация массива и сортировка
n = 5    # кол-во процессоров
T1 = 10  # левая граница задания
T2 = 20  # правая граница задания
m = 10   # кол-во заданий
z = 100   # кол-во особей
k = 15   # кол-во поколений подряд при котором лучшая загрузка будет повторяться k-раз
Pk = 99  # вероятность кроссовера
Pm = 99  # вероятность мутации

f.write('Origin matrix | Искомый массив:\n')
matrix = generate_matrix(m, n, T1, T2)
[f.write(f"{[i for i in j]}\n") for j in matrix]
f.write('#\n\n')

matrix_sum = sorted([sum(elem) for elem in matrix], reverse=True)
f.write('Sums of row elements | Суммы элементов строк:\n')
f.write(f"{[i for i in matrix_sum]}\n")
matrix = sorted(matrix, key=lambda x: sum(x), reverse=True)

f.write('Sorted matrix | Отсортированный массив:\n')
[f.write(f"{[i for i in j]} = {matrix_sum[iter]}\n") for iter, j in enumerate(matrix)]
f.write('##\n\n')

# Метод минимальных элементов
new_matrix, result = [], [0] * n
f.write("Minimum element method | Метод минимальных элементов:\n")
for j in range(m):
    new_matrix.append([])
    check = 0   # check - позволяет вычленять из двух одинаковых только первое левое значение
    for i in range(n):
        if matrix[j][i] != min(matrix[j]) or matrix[j][i] == check:
            new_matrix[j].append(matrix[j][i])
        else:
            result[i] += matrix[j][i]
            new_matrix[j].append(Fore.RED + str(matrix[j][i]) + Style.RESET_ALL)
            check = int(matrix[j][i])
f.write('Schedule | Расписание:\n')
for j in new_matrix:
    for i in j:
        f.write(f"{i}  ")
    f.write("\n")
min_elem_method = deepcopy(new_matrix)
f.write('Result | Результат:\n')
f.write(f'max{tuple(result)} = {max(result)}\n')
f.write('#\n\n')

# Метод Плотникова-Зверева
f.write("Plotnikov-Zverev method | Метод Плотникова-Зверева(обычный):\n")
result_str = [0] * n
new_matrix2 = []
plotnikov_zverev_method = deepcopy(matrix)
f.write('Schedule(without addition) | Расписание(без сложения):\n')
for j in range(m):
    for i in range(n):
        result_str[i] += matrix[j][i]
    min_index = result_str.index(min(result_str))
    for i in range(n):
        if i != min_index:
            result_str[i] -= matrix[j][i]
    plotnikov_zverev_method[j][min_index] = Fore.RED + str(matrix[j][min_index]) + Style.RESET_ALL
for j in plotnikov_zverev_method:
    for i in j:
        f.write(f"{i}  ")
    f.write("\n")
result_str = [0] * n

f.write('Schedule | Расписание:\n')
for j in range(m):
    for i in range(n):
        result_str[i] += matrix[j][i]
    min_index = result_str.index(min(result_str))
    for i in range(n):
        if i != min_index:
            result_str[i] -= matrix[j][i]
    f.write('  '.join([Fore.RED + str(result_str[i]).ljust(2) + Style.RESET_ALL if i == min_index else str(result_str[i]).ljust(2) for i in range(len(result_str))]) + "\n")
f.write('Result | Результат:\n')
f.write(f'max{tuple(result_str)} = {max(result_str)}\n')
f.write('#\n\n')

# Метод квадратов
f.write('Square method | Метод квадратов:\n')
result_str1 = [0] * n
new_matrix = [[0 for i in range(n)] for j in range(m)]
square_method = deepcopy(matrix)
f.write('Schedule(without additions) | Расписание(без сложения):\n')
for j in range(m):
    min_sum = [0] * n
    for i in range(n):
        result_str1[i] += matrix[j][i]
        min_sum[i] = sum([elem * elem for elem in result_str1])
        result_str1[i] -= matrix[j][i]
    min_sum_index = min_sum.index(min(min_sum))
    for i in range(n):
        if i == min_sum_index:
            result_str1[i] += matrix[j][i]
    square_method[j][min_sum_index] = Fore.RED + str(matrix[j][min_sum_index]) + Style.RESET_ALL
for j in square_method:
    for i in j:
        f.write(f"{i}  ")
    f.write("\n")
result_str1 = [0] * n
new_matrix = [[0 for i in range(n)] for j in range(m)]
f.write('Schedule | Расписание:\n')
for j in range(m):
    min_sum = [0] * n
    for i in range(n):
        result_str1[i] += matrix[j][i]
        min_sum[i] = sum([elem * elem for elem in result_str1])
        result_str1[i] -= matrix[j][i]
    min_sum_index = min_sum.index(min(min_sum))
    for i in range(n):
        if i == min_sum_index:
            result_str1[i] += matrix[j][i]
    f.write('  '.join([Fore.RED + str(result_str1[i]).ljust(2) + Style.RESET_ALL if i == min_sum_index else str(result_str1[i]).ljust(2) for i in range(len(result_str1))]) + "\n")
f.write('Result | Результат:\n')
f.write(f'max{tuple(result_str1)} = {max(result_str1)}\n')
f.write('#\n\n')

# Метод барьера
f.write('Barrier method | Метод барьера:\n')
f.write('Barrier value | Значение барьера:\n')
barrier = sum(result) / n
f.write(f'{" + ".join([str(elem) for elem in tuple(result)])} / {n} = {barrier}\n')

result_str2 = [0] * n
barrier_method = []
flag = False
for j in range(m):
    if not flag:
        barrier_method.append([])
        check = 0  # check - позволяет вычленять из двух одинаковых только первое левое значение
        for i in range(n):
            if matrix[j][i] != min(matrix[j]) or matrix[j][i] == check:
                barrier_method[j].append(Style.RESET_ALL + str(matrix[j][i]))
            else:
                result_str2[i] += matrix[j][i]
                barrier_method[j].append(Fore.RED + str(matrix[j][i]) + Style.RESET_ALL)
                check = int(matrix[j][i])
                if result_str2[i] > barrier and not flag:
                    flag = True
                    barrier_method.append([])
                    for s in range(n):
                        barrier_method[-1].append('- ')
    else:
        for i in range(n):
            result_str2[i] += matrix[j][i]
        min_index = result_str2.index(min(result_str2))
        for i in range(n):
            if i != min_index:
                result_str2[i] -= matrix[j][i]
        barrier_method.append([Fore.RED + str(matrix[j][i]).ljust(2) + Style.RESET_ALL if min_index == i else str(matrix[j][i]).ljust(2) + Style.RESET_ALL for i in range(len(result_str2))])
f.write('Schedule(without addition) | Расписание(без сложения):\n')
show(barrier_method)
f.write('\n')

result_str2 = [0] * n
new_matrix = []
flag = False

for j in range(m):
    if not flag:
        new_matrix.append([])
        check = 0  # check - позволяет вычленять из двух одинаковых только первое левое значение
        for i in range(n):
            if matrix[j][i] != min(matrix[j]) or matrix[j][i] == check:
                new_matrix[j].append(matrix[j][i])
            else:
                result_str2[i] += matrix[j][i]
                new_matrix[j].append(Fore.RED + str(matrix[j][i]) + Style.RESET_ALL)
                check = int(matrix[j][i])
                if result_str2[i] > barrier and not flag:
                    flag = True
                    new_matrix.append([])
                    for s in range(n):
                        new_matrix[-1].append(Fore.BLUE + '- ' + Style.RESET_ALL)
    else:
        for i in range(n):
            result_str2[i] += matrix[j][i]
        min_index = result_str2.index(min(result_str2))
        for i in range(n):
            if i != min_index:
                result_str2[i] -= matrix[j][i]
        new_matrix.append([Fore.RED + str(result_str2[i]).ljust(2) + Style.RESET_ALL if i == min_index else str(result_str2[i]).ljust(2) for i in range(len(result_str2))])
f.write('Schedule | Расписание:\n')
show(new_matrix)
f.write('\n')
f.write('Result | Результат:\n')
f.write(f'max{tuple(result_str2)} = {max(result_str2)}\n')
f.write('#\n\n')

# Результат работы всех методов
f.write("\nResult of all methods | Результат работы всех методов:\n")
# chosen_method = min_elem_method
chosen_method = plotnikov_zverev_method
# chosen_method = square_method
# chosen_method = barrier_method
f.write(f"Minimum element method | Метод минимальных элементов:\n")
show(min_elem_method)
f.write(f"{result} = {max(result)}\n")
f.write(f"Plotnikov-Zverev method | Метод Плотникова-Зверева:\n")
show(plotnikov_zverev_method)
f.write(f"{result_str} = {max(result_str)}\n")
f.write(f"Quadrangle method | Метод Квадратов:\n")
show(square_method)
f.write(f"{result_str1} = {max(result_str1)}\n")
f.write(f"Barrier method | Метод Барьера:\n")
show(barrier_method)
f.write(f"{result_str2} = {max(result_str2)}\n")
# f.write('\n')
f.write(f"#\n\n")

# Генерация особей (50 детерминированно + 50 рандомно)
individuals = [generate_individ(chosen_method, n, 0) for _ in range(z//2)]
[individuals.append(generate_individ(m, n, 1)) for _ in range(z//2)]

# Особи нулевого поколения (родители для будущего поколения):
listMax = []
newline = "\n"
f.write('0 GENERATION | 0-е ПОКОЛЕНИЕ >\n')
for i, individual in enumerate(individuals):
    f.write(f'{i+1} individual | особь (O{i+1}):{" ".join([str(elem) for elem in individual])}\n')
    load = count_load(individual, n, m, matrix)
    listMax.append(load)
    f.write(f'Load | Загрузка: {load}\n')
best_result, bestLoad_index = best_load(listMax)  # лучшая загрузка и (индекс лучшей особи - 1)
best_individual = individuals[bestLoad_index]
f.write(f'All_Loads | Все загрузки:\n{newline.join(["(O" + str(i + 1) + ") " + " ".join([str(e) for e in el]) for i, el in enumerate(listMax)])}'
        f'\nBest individual is (O{bestLoad_index+1}) | Лучшая особь это (O{bestLoad_index+1}):\n{" ".join([str(elem) for elem in best_individual])}\n')
f.write(f'Its load| Его загрузка: {best_result}\n#\n')
previous_best_result, bestLoad_index = 0, 0
best_of_all_generations_result = best_result

# Переменные для ГА и сам ГА:
counter, gen_count = 0, 0

while k != counter - 1:
    previous_best_result = best_result
    gen_count += 1
    generation = []
    best_generation_loads = []
    f.write(f'\n{gen_count} GENERATION | {gen_count}-е ПОКОЛЕНИЕ >\n'
            f'Parents | Родители:\n'
            f'{newline.join([str(i+1) + " individual | особь" + "(O" + str(i+1) + ")" + newline + " ".join([str(elem) for elem in individual]) for i, individual in enumerate(individuals)])}\n\n')
    for _ in range(z):

        # Алгоритм образования пар родителей:
        parent1 = c(individuals)
        individuals_no_repeat = deepcopy(individuals)
        individuals_no_repeat.remove(parent1)  # дабы избежать попадание рандома на первого
        parent2 = c(individuals_no_repeat)
        while r(0, 100) <= Pk:
            parent2 = c(individuals_no_repeat)
        f.write(f'{_ + 1} child selection | Выборка {_ + 1}-го ребёнка >\n')
        f.write(f'Pair of parents | Пара родителей:\n'
                f'1 Parent | 1-й родитель: {" ".join(str(elem) for elem in parent1)}\n'
                f'2 Parent | 2-й родитель: {" ".join(str(elem) for elem in parent2)}\n')
        f.write(f'Parent1 load | Загрузка 1-го родителя: {count_load(parent1, n, m, matrix)}\nParent2 load | Загрузка 2-го родителя: {count_load(parent2, n, m, matrix)}\n')
        parents_list = (parent1, parent2)

        # Алгоритм отбора детей из потенциальных особей (2 + 2 мутанта)
        children = []
        load_list = []
        counter_child = 0
        crossover_result = crossover(parent1, parent2)
        f.write(f'Potential children | Потенциальные дети:\n{newline.join([" ".join([str(el) for el in elem]) for elem in crossover_result])}\n')
        for i, child in enumerate(crossover_result):
            children.append(child)
            load_list.append(count_load(child, n, m, matrix))
            f.write(f'{counter_child + i + 1} Potential child({i + 1} without mutation) | {counter_child + i + 1} Потенциальный ребёнок({i + 1} с мутацией) :\n'
                    f'{" ".join([str(el) for el in child])}\n')
            f.write(f'Its load | Его загрузка: {load_list[-1]}\n')
            f.write(f'Mutation process... | Процесс мутации...\n')
            counter_child += 1
            muted_child = mutation(child, Pm)
            children.append(muted_child)
            load_list.append(count_load(muted_child, n, m, matrix))
            f.write(f'{counter_child + i + 1} Potential child({i + 1} with mutation) | {counter_child + i + 1} Потенциальный ребёнок({i + 1} с мутацией) :\n'
                    f'{" ".join([str(el) for el in child])}\n')
            f.write(f'Its load | Его загрузка: {load_list[-1]}\n')
        best_child_load, best_child_index = best_load(load_list)
        num = 0
        if best_child_index == 0:
            f.write('The best child is 1 (without mutation) | Лучший ребёнок 1-й (без мутации):\n')
        elif best_child_index == 1:
            f.write('The best child is 1 (with mutation) | Лучший ребёнок 1-й (с мутацией):\n')
        elif best_child_index == 2:
            f.write('The best child is 2 (without mutation) | Лучший ребёнок 2-й (без мутации):\n')
        else:
            f.write('The best child is 2 (with mutation) | Лучший ребёнок 2-й (с мутацией): ')
        f.write(f'{" ".join([str(elem) for elem in children[best_child_index]])}\n')
        f.write(f'Its load | Его загрузка: {best_child_load}\n\n')
        generation.append(children[best_child_index])

    # Список всех детей:
    f.write('Children | Дети:\n')
    listMax = []
    for i, child in enumerate(generation):
        f.write(f'{str(i + 1)}) {" ".join([str(elem) for elem in child])}\n')
        listMax.append(count_load(child, n, m, matrix))
    f.write(f'\nTheir load | Их загрузка:\n{newline.join([str(i + 1) + ") " + " ".join([str(el) for el in count_load(elem, n, m, matrix)]) for i, elem in enumerate(generation)])}\n')

    # Индекс лучшего результата в поколении
    currentLoad = best_load(listMax)[1]

    # Собираем матрицу родителей и лучших детей для отбора:
    check_matrix, parent_child_loads = [], []
    for elem in generation:
        check_matrix.append(elem)
        parent_child_loads.append(max(count_load(elem, n, m, matrix)))
    for elem in individuals:
        check_matrix.append(elem)
        parent_child_loads.append(max(count_load(elem, n, m, matrix)))

    best_result = sorted(parent_child_loads)[0]

    # Создаём матрицу индексов лучших особей:
    best_index = []
    for elem in sorted(parent_child_loads)[:z]:
        for i, el in enumerate(parent_child_loads):
            if elem == el:
                best_index.append(i)
                break

    # Добавляем лучших особей поколения среди родителей и детей:
    individuals = []
    for elem in best_index:
        individuals.append(check_matrix[elem])

    f.write(f'\nBest individual | Лучшая особь: {" ".join([str(elem) for elem in individuals[0]])}\n')
    f.write(f'Its load | Его загрузка: {" ".join([str(el) for el in count_load(individuals[0], n, m, matrix)])}\n')

    f.write(f'Best children + parents loads | Лучшие детские + родительские загрузки: {parent_child_loads}\n')
    f.write(f'Best z individuals | Лучший z особей: {sorted(parent_child_loads)[:z]}\n')
    f.write(f'Best load | Лучшая загрузка: {best_result}\n')

    # Если сквозь поколения была лучшая загрузка ждем когда она не повторится или улучшится:
    if best_result < best_of_all_generations_result:
        best_of_all_generations_result = best_result
        counter = 0

    # Если загрузка предыдущего поколения равна загрузке текущего
    if best_of_all_generations_result == best_result:
        counter += 1
    else:
        counter = 0
    f.write(f'#\n')

print(f'Generations | Поколения: {gen_count}\nBest result | Лучший результат: {best_result}')
f.write(f'\nGenerations | Поколения: {gen_count}\nBest result | Лучший результат: {best_result}\n')

# Сравнение расписания при начальном поколении и конечном:
if chosen_method == min_elem_method:
    word = "методе минимальных элементов"
    chosen_load = result
elif chosen_method == plotnikov_zverev_method:
    word = "методе Плотникова-Зверева"
    chosen_load = result_str
elif chosen_method == square_method:
    word = "методе квадратов"
    chosen_load = result_str1
else:
    word = "методе барьеров"
    chosen_load = result_str2
f.write(f"Init generation | Начальное поколение при {word}:\n")
show(chosen_method)
f.write(f'Init generation load | Загрузка при {word}:\n{" ".join([str(el) for el in chosen_load])}\nMax = {max(chosen_load)}\n')
f.write("Final generation | Финальное поколение:\n")
proc = [i for i in range(255//n, 255 + 255//n, int(255//n))]
last_gen_show = []
for j, gen in enumerate(individuals[0]):
    load_result = deepcopy(matrix[j])
    for i in range(n):
        if gen <= proc[i]:
            load_result[i] = Fore.RED + str(matrix[j][i]) + Style.RESET_ALL
            last_gen_show.append(load_result)
            break
show(last_gen_show)
bestie = count_load(individuals[0], n, m, matrix)
f.write(f'Final generation load | Загрузка при финальном поколении:\n')
f.write(f'{" ".join([str(el) for el in bestie])}\n')
f.write(f'Max = {max(bestie)}\n')
f.write(f"#\n\n")

f.close()

# Вывод данных из txt-файлов:
show_generation(txt_file, gen_count, word)
