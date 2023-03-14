from random import choice as c, randint as r
from copy import deepcopy
from prettytable import PrettyTable
from datetime import datetime
from tqdm import tqdm

def beautiful_table(head, values):
    columns = len(head)  # Подсчитаем кол-во столбцов на будущее.
    table = PrettyTable(head)  # Определяем таблицу.
    # Cкопируем список td, на случай если он будет использоваться в коде дальше.
    td_data = values[:]  # Входим в цикл который заполняет нашу таблицу. Цикл будет выполняться до тех пор пока
    # у нас не кончатся данные для заполнения строк таблицы (список td_data).
    while td_data:
        table.add_row(td_data[:columns])  # Используя срез добавляем первые три элементов в строку (columns = 3).
        td_data = td_data[columns:]  # Используя срез переопределяем td_data так, чтобы он
        # больше не содержал первых 3 элементов.
    #print(table)  # Печатаем таблицу
    table = table.get_string()
    f.write(table)
    f.write('\n')


# Рисуем матрицы(если позиционный аргумент не задан выведется всё поколение, иначе конкретная особь):
def fill_matrix_to_txt(matrix, num_of_individual=-2, name_of_individual='individual'):
    th = ['m', 'Genes']
    [th.append(f'n{i + 1}') for i in range(n)]
    td = []
    if num_of_individual == -2:
        for i, individual in enumerate(matrix):
            f.write(f'{i + 1} {name_of_individual} (O{i + 1})\n')
            m_count = 0
            for gene, m in individual:
                m_count += 1
                td.append(f'm{m_count}')
                td.append(gene)
                for elem in m:
                    td.append(elem)
            beautiful_table(th, td)
            td = []
    else:
        if name_of_individual == 'parent':
            f.write(f'{num_of_individual + 1} {name_of_individual}\n')
        elif name_of_individual == 'child':
            f.write('')
        else:
            f.write(f'{num_of_individual + 1} {name_of_individual} (O{num_of_individual + 1})\n')
        m_count = 0
        for gene, m in matrix[num_of_individual]:
            m_count += 1
            td.append(f'm{m_count}')
            td.append(gene)
            for elem in m:
                td.append(elem)
        beautiful_table(th, td)
        td = []



# Генерируем матрицу(m - строки, n - столбцы) со значениями от T1 до T2:
def generate_matrix(m, n, T1, T2):
    return [[r(T1, T2) for j in range(n)] for i in range(m)]


# Генерируем особь:
def generate_individ(MATRIX):
    return [(r(1, 255), elem) for elem in MATRIX]


# Считаем загрузки:
def count_load(individ, n=5, t=255):
    load_result = [0 for _ in range(n)]
    proc = [i for i in range(t//n, t + t//n, int(t/n))]
    for gen, tasks in individ:
        for i in range(n):
            if gen <= proc[i]:
                load_result[i] += tasks[i]
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
    #f.write(f'T: {T1}, {T2}\n')
    #print(f'parents({T1},{T2}):\n{parent1}\n{parent2}')
    child1, child2 = parent1[:T1] + parent2[T1:T2+1] + parent1[T2+1:], parent2[:T1] + parent1[T1:T2+1] + parent2[T2+1:],
    #print(f'children:\n{child1}\n{child2}')
    return child1, child2


# Двухточечная мутация
def mutation(child, Pm):
    child_copy = deepcopy(child)
    child_genes = [e[0] for e in child_copy]
   # f.write(f'Genes before: {" ".join([str(e) for e in child_genes])}')
    gen = c(child_genes)
    while r(1, 100) < Pm:
        gen = c(child_genes)
   # f.write(f'\nGene: {gen}\n')
    that_gen = deepcopy(gen)
    binary_gen = '00000000'
    for j in range(len(binary_gen)):
        binary_gen = binary_gen[:j] + str(gen % 2) + binary_gen[j + 1:]
        gen //= 2
    binary_gen = binary_gen[::-1]
   # f.write(f'Its binary form: {binary_gen}')
    index = r(0, len(binary_gen) - 1)
    binary_gen = list(binary_gen)
    index1 = r(0, len(binary_gen)-1)
    index2 = r(0, len(binary_gen)-1)
    while index2 == index1:
        index2 = r(0, len(binary_gen)-1)
    if index1 > index2:
        index1, index2 = index2, index1
    binary_gen[index1], binary_gen[index2] = binary_gen[index2], binary_gen[index1]
    binary_gen = "".join(binary_gen)
   # f.write(f'\nChanged bit: {binary_gen}\nNew number: {int(binary_gen, 2)}\n')
    child_copy = [(genes, tasks) if genes != that_gen else (int(binary_gen, 2), tasks) for genes, tasks in child_copy]
   # f.write(f'Genes after: {" ".join([str(e[0]) for e in child_copy])}\n')
    return child_copy


# Выводим нужное поколение
def show_generation(txt_file, amount_of_generations):
    with open(txt_file, 'r') as file:
        while True:
            file.seek(0)
            while True:
                num = input('Choose generation to show (exit - to quit programm) > ')
                if num.isdigit() and 0 <= int(num) <= amount_of_generations or num == 'exit':
                    chosen_generation = f"{num} GENERATION >\n"
                    break
                else:
                    print('Incorrect input!')
                chosen_generation = f"{num} GENERATION >\n"
            print()
            if num == 'exit':
                break
            generation_tree_data = file.readlines()
            new_slice = generation_tree_data[generation_tree_data.index(chosen_generation):]
            this_generation = new_slice[:new_slice.index('#\n')]
            print("".join(this_generation))
        print('Good Bye!')


# Переменные для задания ГА:
m = 12
n = 3
z = 100
k = 30
Pk = 93
Pm = 92
T1 = 10
T2 = 30

# Открываем файл для записи:
#txt_file = 'lab6_results.txt'
#f = open(txt_file, 'w')

# Генерируем нулевое поколение:
matrix = generate_matrix(m, n, T1, T2)
start, generations, results = datetime.now(), [], []
with tqdm(range(100), ncols=100, desc=f"Не ООП ГА") as t:
    for _ in t:
        individuals = [generate_individ(matrix) for _ in range(z)]  # генерируем родителей 0-го поколения

        newline = '\n'

        # Особи нулевого поколения (родители для будущего поколения):
        listMax = []
        #f.write('0 GENERATION >\n')
        for i, individual in enumerate(individuals):
          #  fill_matrix_to_txt(individuals, i)
            load = count_load(individual, n)
            listMax.append(load)
        #    f.write(f'load: {load}\n')
        best_result, bestLoad_index = best_load(listMax)  # лучшая загрузка и (индекс лучшей особи - 1)
        best_individual = individuals[bestLoad_index]
        #f.write(f'All_Loads:\n{newline.join(["(O" + str(i + 1) + ") " + " ".join([str(e) for e in el]) for i, el in enumerate(listMax)])}\nBest individual is ')
        #fill_matrix_to_txt(individuals, bestLoad_index)
        #f.write(f'Its load: {best_result}\n#\n')
        previous_best_result, bestLoad_index = 0, 0
        best_of_all_generations_result = best_result
        #print(listMax)

        # Переменные для ГА:
        counter, gen_count = 0, 0

        while k != counter - 1:
            previous_best_result = best_result
            gen_count += 1
            generation = []
            best_generation_loads = []
        #    f.write(f'\n{gen_count} GENERATION >\n')
           ## f.write(f'Parents:\n')
         #   [fill_matrix_to_txt(individuals, i) for i, el in enumerate(individuals)]
            for _ in range(z):

                # Алгоритм образования пар родителей:
                parent1 = individuals[_]
                parent2 = c(individuals)
                while r(0, 100) <= Pk:
                    parent2 = c(individuals)
             #   f.write(f'Pair of parents:\n')
              #  [fill_matrix_to_txt([parent1, parent2], i, 'parent') for i in range(2)]
             #   f.write(f'Parent1 load: {count_load(parent1, n)}\nParent2 load: {count_load(parent2, n)}\n')
                parents_list = (parent1, parent2)

                # Алгоритм отбора детей из потенциальных особей (2 + 2 мутанта)
                children = []
                load_list = []
                counter_child = 0
              #  f.write(f'\n{_+1} child >\n')
                crossover_result = crossover(parent1, parent2)
                for i, child in enumerate(crossover_result):
                    children.append(child)
                    load_list.append(count_load(child, n))
                 #   f.write(f'{counter_child+i+1} Potential child({i+1} without mutation):\n')
                 #   fill_matrix_to_txt(crossover_result, counter_child, 'child')
                 #   f.write(f'Its load: {load_list[-1]}\n')
                 #   f.write(f'Mutation process...\n')
                    counter_child += 1
                    muted_child = mutation(child, Pm)
                    children.append(muted_child)
                    load_list.append(count_load(muted_child, n))
                #    f.write(f'{counter_child+i+1} Potential child({i+1} with mutation):\n')
                #    fill_matrix_to_txt(children, -1, 'child')
               #     f.write(f'Its load: {load_list[-1]}\n')
                best_child_load, best_child_index = best_load(load_list)
               # f.write(f'Best child:\n')
               # fill_matrix_to_txt(children, best_child_index, 'child')
               # f.write(f'Its load: {best_child_load}\n\n')
                generation.append(children[best_child_index])

            # Список всех детей:
           # f.write('\nChildren:\n')
            listMax = []
            for i, child in enumerate(generation):
               # f.write(f'{str(i + 1)})\n')
                #fill_matrix_to_txt(generation, i, 'child')
                listMax.append(count_load(child, n))
            #f.write(f'\nTheir load:\n{newline.join([str(i + 1) + ") " + " ".join([str(el) for el in count_load(elem, n)]) for i, elem in enumerate(generation)])}\n')

            # Индекс лучшего результата в поколении
            currentLoad = best_load(listMax)[1]

            # Собираем матрицу родителей и лучших детей для отбора:
            check_matrix, parent_child_loads = [], []
            for elem in generation:
                check_matrix.append(elem)
                parent_child_loads.append(max(count_load(elem, n)))
            for elem in individuals:
                check_matrix.append(elem)
                parent_child_loads.append(max(count_load(elem, n)))

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

           # f.write(f'\nBest individual:\n')
           # fill_matrix_to_txt(individuals, 0, 'child')
            #print(individuals[0])
            # head, values = [], []
            # [head.append(f'm{m - i}') for i in range(m)]
            # head.append('m')
            # reversed_best = deepcopy(individuals[0])[::-1]
            # to_add = ['genes']
            # [to_add.append(f'n{i + 1}') for i in range(n)]
            # count = 0
            # for gene, procs in reversed_best:
            #     values.append(gene)
            # values.append('Genes')
            # for i in range(n):
            #     for gene, procs in reversed_best:
            #         values.append(procs[i])
            #     values.append(f'n{i+1}')


            #[values.append(f'n{i+1}') for i in range(n)]
            #print(head, values)

            # columns = len(head)  # Подсчитаем кол-во столбцов на будущее.
            # table = PrettyTable(head)  # Определяем таблицу.
            # # Cкопируем список td, на случай если он будет использоваться в коде дальше.
            # td_data = values[:]  # Входим в цикл который заполняет нашу таблицу. Цикл будет выполняться до тех пор пока
            # # у нас не кончатся данные для заполнения строк таблицы (список td_data).
            # while td_data:
            #     table.add_row(td_data[:columns])  # Используя срез добавляем первые три элементов в строку (columns = 3).
            #     td_data = td_data[columns:]  # Используя срез переопределяем td_data так, чтобы он
            #     # больше не содержал первых 3 элементов.
            #     table.hrules = 1
            # print(table)  # Печатаем таблицу
            #table = table.get_string()
            # f.write(table)
            # f.write('\n')
            #
            # f.write(f'Its load: {" ".join([str(el) for el in count_load(individuals[0], n)])}\n')
            #
            # f.write(f'Best children + parents loads: {parent_child_loads}\n')
            # f.write(f'Best z individuals: {sorted(parent_child_loads)[:z]}\n')
            # f.write(f'Best load: {best_result}\n')

            # Если сквозь поколения была лучшая загрузка ждем когда она не повторится или улучшится:
            if best_result < best_of_all_generations_result:
                best_of_all_generations_result = best_result
                counter = 0

            # Если загрузка предыдущего поколения равна загрузке текущего
            if best_of_all_generations_result == best_result:
                counter += 1
            else:
                counter = 0
            #f.write(f'#\n')
            # print(gen_count, best_result, best_of_all_generations_result)

        generations.append(gen_count), results.append(best_result)
        #print(f'Generations: {gen_count}\nBest result: {best_result}')
print(
    f"{datetime.now() - start}\n"
    f"{sum(generations) / len(generations)}\n"
    f"{sum(results) / len(results)}"
)
    #f.write(f'\nGenerations: {gen_count}\nBest result: {best_result}\n')

    #f.close()

    # Вывод данных из нужного поколения:
    #show_generation(txt_file, gen_count)

    #f.close()
#print(datetime.now() - start)