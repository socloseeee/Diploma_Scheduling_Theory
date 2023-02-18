from random import choice as c, randint as r
from copy import deepcopy

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
    matrix = []

    def __init__(self, Pk, Pm, m, n, T1, T2):
        super().__init__(m, n, T1, T2)
        self.individ = []
        self.Pk = Pk
        self.Pm = Pm

    def __getitem__(self, key):
        return self.individ[key]

    def __str__(self):
        return f"{newline.join([str(elem[1]) for elem in self.individ])}"

    def generate_individ(self):
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
        # print(f'children:\n{child1}\n{child2}')
        return child1, child2

    def mutation(self, Pm):
        child_copy = deepcopy(self.individ)
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
        return child_copy


class Generation(Individ):
    def __init__(self, Pk, Pm, m, n, T1, T2, z):
        self.z = z
        super().__init__(Pk, Pm, m, n, T1, T2)
        self.generation = []

    def __getitem__(self, key):
        return self.generation[key]

    def __str__(self):
        return f"{newline.join([str(elem) for elem in self.generation])}"

    def generate_new_generation(self):
        for _ in range(self.z):
            self.generation.append(super().generate_individ())

    def best_load(self, max_loads):
        result = [max(el) for el in max_loads]
        return min(result), result.index(min(result))


matrix = Matrix(m=12, n=3, T1=10, T2=17)
matrix.generate_new_matrix()
matrix = Matrix.matrix
print(matrix)
individuals = Generation(Pk=93, Pm=92, m=12, n=3, T1=10, T2=17, z=10)
individuals.generate_new_generation()
print(individuals)

# Особи нулевого поколения (родители для будущего поколения):
listMax = []
for i, individual in enumerate(individuals):
    print(individual)
    load = individual.count_load()
    listMax.append(load)
best_result, bestLoad_index = individuals.best_load(listMax)  # лучшая загрузка и (индекс лучшей особи - 1)
best_individual = individuals[bestLoad_index]
previous_best_result, bestLoad_index = 0, 0
best_of_all_generations_result = best_result
# print(listMax, individuals)

# Переменные для ГА и сам ГА:
counter, gen_count = 0, 0
