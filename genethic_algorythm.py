from random import choice as c, randint as r
from copy import deepcopy

newline = '\n'


class Matrix:
    def __init__(self, m, n, T1, T2):
        self.matrix = [[r(T1, T2) for _ in range(n)] for __ in range(m)]

    def __getitem__(self, key):
        return self.matrix[key]

    def __str__(self):
        return f"{newline.join([str(elem) for elem in self.matrix])}"


class Individ:
    def __init__(self, Pk, Pm, mtrx_cls):
        self.Pk = Pk
        self.Pm = Pm
        self.individ = [(r(1, 255), elem) for elem in mtrx_cls.matrix]

    def __getitem__(self, key):
        return self.individ[key]

    def __str__(self):
        return f"{newline.join([str(elem) for elem in self.individ])}"

    def count_load(self):
        n = len(self.individ[0])
        load_result = [0 for _ in range(n)]
        proc = [i for i in range(255//n, 255 + 255//n, int(255/n))]
        for gen, tasks in self.individ:
            for i in range(n):
                if gen <= proc[i]:
                    load_result += tasks[i]
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
        f.write(f'\nChanged bit: {binary_gen}\nNew number: {int(binary_gen, 2)}\n')
        child_copy = [(genes, tasks) if genes != that_gen else (int(binary_gen, 2), tasks) for genes, tasks in
                      child_copy]
        f.write(f'Genes after: {" ".join([str(e[0]) for e in child_copy])}\n')
        return child_copy

class Generation:
    def __init__(self, z, individ):
        self.generation = [individ for _ in range(z)]

    def __getitem__(self, key):
        return self.generation[key]

    def __str__(self):
        return f"{newline.join([str(elem) for elem in self.generation])}"

    def best_load(self, max_loads):
        result = [max(el) for el in max_loads]
        return (min(result), result.index(min(result)))


matrix = Matrix(m=12, n=3, T1=10, T2=17)
individ = Individ(92, 93, matrix)
individuals = Generation(z=11, individ=Individ(92, 93, matrix))

