from random import choice as c, randint as r
from copy import deepcopy
from typing import List, Any
from datetime import datetime

newline = '\n'


class Matrix:
    matrix = []

    def __init__(self, m, n, T1, T2):
        self.m = m
        self.n = n
        self.T1 = T1
        self.T2 = T2
        self.matrix = Matrix.matrix

    def __getitem__(self, key):
        return self.matrix[key]

    def __str__(self):
        return f"{newline.join([str(elem) for elem in self.matrix])}"

    def generate_new_matrix(self):
        Matrix.matrix = [[r(self.T1, self.T2) for _ in range(self.n)] for __ in range(self.m)]


class Individ(Matrix):

    def __init__(self, Pk=93, Pm=92, m=12, n=3, T1=10, T2=17):
        super().__init__(m, n, T1, T2)
        self.Pm = Pm
        self.individ = []

    def __getitem__(self, key):
        return self.individ[key]

    def __str__(self):
        return f"{self.individ}"

    def generate_new_individ(self):
        self.individ = [(r(1, 255), elem) for elem in self.matrix]
        return self.individ

    def count_load(self):
        n = len(self.individ[0][1])
        load_result = [0 for _ in range(n)]
        proc = [i for i in range(255 // n, 255 + 255 // n, int(255 / n))]
        for gen, tasks in self.individ:
            for i in range(n):
                if gen <= proc[i]:
                    load_result[i] += tasks[i]
                    break
        return load_result

    def crossover(self, parent2):
        parent1 = self.individ
        T1 = r(1, len(parent1) - 1)
        T2 = r(1, len(parent1) - 1)
        while T2 == T1:
            T2 = r(1, len(parent1) - 1)
        if T1 > T2:
            T1, T2 = T2, T1
        # f.write(f'T: {T1}, {T2}\n')
        # print(f'parents({T1},{T2}):\n{parent1}\n{parent2}')
        child1, child2 = parent1[:T1] + parent2[T1:T2 + 1] + parent1[T2 + 1:], parent2[:T1] + parent1[
                                                                                              T1:T2 + 1] + parent2[
                                                                                                           T2 + 1:],
        child1_, child2_ = Individ(), Individ()
        child1_.individ, child2_.individ = child1, child2
        # print(f'children:\n{child1}\n{child2}')
        return child1_, child2_

    def mutation(self):
        child_copy = deepcopy(self.individ)
        child_genes = [e[0] for e in child_copy]
        # f.write(f'Genes before: {" ".join([str(e) for e in child_genes])}')
        gen = c(child_genes)
        while r(1, 100) < self.Pm:
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
        index1 = r(0, len(binary_gen) - 1)
        index2 = r(0, len(binary_gen) - 1)
        while index2 == index1:
            index2 = r(0, len(binary_gen) - 1)
        if index1 > index2:
            index1, index2 = index2, index1
        binary_gen[index1], binary_gen[index2] = binary_gen[index2], binary_gen[index1]
        binary_gen = "".join(binary_gen)
        # f.write(f'\nChanged bit: {binary_gen}\nNew number: {int(binary_gen, 2)}\n')
        child_copy = [(genes, tasks) if genes != that_gen else (int(binary_gen, 2), tasks) for genes, tasks in
                      child_copy]
        # f.write(f'Genes after: {" ".join([str(e[0]) for e in child_copy])}\n')
        child_ = Individ()
        child_.individ = child_copy
        return child_


def best_load(max_loads):
    result = [max(el) for el in max_loads]
    return min(result), result.index(min(result))


class Generation(Individ):
    def __init__(self, Pk=93, Pm=92, m=12, n=3, T1=10, T2=17, z=10):
        super().__init__(Pk, Pm, m, n, T1, T2)
        self.z = z
        self.generation = []

    def __getitem__(self, key):
        return self.generation[key]

    def __str__(self):
        return f"{newline.join([str(elem) for elem in self.generation])}"

    def __len__(self):
        return len(self.generation)

    def remove(self, obj):
        print(obj)
        print(self.generation)
        self.generation.remove(obj)

    def generate_new_generation(self):
        for _ in range(self.z):
            x = Individ(self.Pm, self.Pm, self.m, self.n, self.T1, self.T2)
            x.generate_new_individ()
            self.generation.append(x)



# Переменные
m = 12
n = 3
z = 10
k = 10
Pk = 93

# Матрица и генерация нулевого поколения
Matrix(m=12, n=3, T1=10, T2=17).generate_new_matrix()
start, results, generations = datetime.now(), [], []
for _ in range(100):
    individuals = Generation(Pk=93, Pm=92, m=12, n=3, T1=10, T2=17, z=10)
    individuals.generate_new_generation()
    # print(individuals)

    # Особи нулевого поколения (родители для будущего поколения):
    listMax = []
    for i, individual in enumerate(individuals):
        # print(individual)
        load = individual.count_load()
        listMax.append(load)
    best_result, bestLoad_index = best_load(listMax)  # лучшая загрузка и (индекс лучшей особи - 1)
    best_individual = individuals[bestLoad_index]
    previous_best_result, bestLoad_index = 0, 0
    best_of_all_generations_result = best_result
    # Переменные для ГА и сам ГА:
    counter, gen_count = 0, 0

    while k != counter - 1:
        previous_best_result = best_result
        gen_count += 1
        generation = []
        best_generation_loads = []
        for _ in range(z):

            # Алгоритм образования пар родителей:
            parent1 = individuals[_]
            parent2 = c(individuals)
            while r(0, 100) <= Pk:
                parent2 = c(individuals)
            parents_list = (parent1, parent2)

            # Алгоритм отбора детей из потенциальных особей (2 + 2 мутанта)
            children: list[Any] = []
            load_list = []
            crossover_result = parent1.crossover(parent2)
            for i, child in enumerate(crossover_result):
                children.append(child)
                load_list.append(child.count_load())
                muted_child = child.mutation()
                children.append(muted_child)
                load_list.append(muted_child.count_load())
            best_child_load, best_child_index = best_load(load_list)
            generation.append(children[best_child_index])

        # Список всех детей:
        listMax = []
        for i, child in enumerate(generation):
            listMax.append(child.count_load())

        # Индекс лучшего результата в поколении
        currentLoad = best_load(listMax)[1]

        # Собираем матрицу родителей и лучших детей для отбора:
        check_matrix, parent_child_loads = [], []
        for elem in generation:
            check_matrix.append(elem)
            parent_child_loads.append(max(elem.count_load()))
        for elem in individuals:
            check_matrix.append(elem)
            parent_child_loads.append(max(elem.count_load()))

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

        head, values = [], []
        [head.append(f'm{m - i}') for i in range(m)]
        head.append('m')
        reversed_best = deepcopy(individuals[0])[::-1]
        to_add = ['genes']
        [to_add.append(f'n{i + 1}') for i in range(n)]
        count = 0
        for gene, procs in reversed_best:
            values.append(gene)
        values.append('Genes')
        for i in range(n):
            for gene, procs in reversed_best:
                values.append(procs[i])
            values.append(f'n{i+1}')

        # Если сквозь поколения была лучшая загрузка ждем когда она не повторится или улучшится:
        if best_result < best_of_all_generations_result:
            best_of_all_generations_result = best_result
            counter = 0

        # Если загрузка предыдущего поколения равна загрузке текущего
        if best_of_all_generations_result == best_result:
            counter += 1
        else:
            counter = 0
        # print(gen_count, best_result, best_of_all_generations_result)

    generations.append(gen_count), results.append(best_result)
    # print(f'Generations: {gen_count}\nBest result: {best_result}')
print(
    f"{datetime.now() - start}\n"
    f"{sum(generations) / len(generations)}\n"
    f"{sum(results) / len(results)}"
)
# Вывод данных из нужного поколения:
# show_generation(txt_file, gen_count)