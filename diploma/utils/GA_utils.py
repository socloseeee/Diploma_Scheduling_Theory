import random
import time
from copy import deepcopy
from random import randint as r, choice as c
from typing import Any

random.seed(time.time() * 1000)

def generate_matrix(
        m: int,
        n: int,
        T1: int,
        T2: int
) -> list[list[int]]:
    return [[r(T1, T2) for j in range(n)] for i in range(m)]


# Генерируем особь (рандомно/детерминированно):
def generate_individ(
        m: Any,
        n: int,
        random: Any,
        bnds=None
) -> list[int]:
    if random:
        return [r(1, 255) for _ in range(m)]
    else:
        individ: list = []
        for row in m:
            for i, elem in enumerate(row):
                if '\x1b[31m' in str(elem):  # '\x1b[31m' - идентификатор цвета
                    if bnds == 0:
                        individ.append(
                            i * (255 // n) + (255 // n) // 2)  # чётко по центру между двумя границами в процессоре
                    elif bnds == 1:
                        individ.append(i * (255 // n))  # чётко по левой границе в процессоре
                    elif bnds == 2:
                        individ.append(i * (255 // n) + (255 // n))  # чётко по правой границе в процессоре
                    elif bnds == 3:
                        individ.append(r(i * (255 // n) + 1,
                                         i * (255 // n) + (255 // n)))  # рандомно между двумя границами в процессоре
    return individ


# Считаем загрузки:
def count_load(individ: list[int], n: int, tasks: list[list[int]]) -> list[int]:
    t: int = 255
    load_result: list = [0 for _ in range(n)]
    proc: list = [i for i in range(t // n, t + t // n, int(t // n))]
    for j, gen in enumerate(individ):
        for i in range(n):
            if gen <= proc[i]:
                load_result[i] += tasks[j][i]
                break
    return load_result


# Считаем лучшую загрузку для каждой особи:
def best_load(max_loads) -> (int, int):
    result: list[int] = list(map(max, max_loads))
    min_result: int = min(result)
    return min_result, result.index(min_result)


# Двухточечный кроссовер
def crossover(
        parent1: list[int],
        parent2: list[int]
) -> (list[int], list[int]):
    T1: int = r(1, len(parent1) - 1)
    T2: int = r(1, len(parent1) - 1)
    while T2 == T1:
        T2 = r(1, len(parent1) - 1)
    if T1 > T2:
        T1, T2 = T2, T1
    child1: list[int] = parent1[:T1] + parent2[T1:T2 + 1] + parent1[T2 + 1:]
    child2: list[int] = parent2[:T1] + parent1[T1:T2 + 1] + parent2[T2 + 1:]
    return child1, child2


# Двухточечная мутация
def mutation(
        child: list[int],
        Pm: int
) -> list[int]:
    child_copy: list = deepcopy(child)
    child_genes: list = [e for e in child_copy]
    gen: int = c(child_genes)
    while r(1, 100) < Pm:
        gen = c(child_genes)
    that_gen: int = deepcopy(gen)
    binary_gen = '00000000'
    for j in range(len(binary_gen)):
        binary_gen = binary_gen[:j] + str(gen % 2) + binary_gen[j + 1:]
        gen //= 2
    binary_gen = binary_gen[::-1]
    binary_gen = list(binary_gen)
    index1: int = r(0, len(binary_gen) - 1)
    index2: int = r(0, len(binary_gen) - 1)
    if binary_gen.count(binary_gen[0]) != len(binary_gen):
        while index2 == index1 or binary_gen[index1] == binary_gen[index2]:  # 0 меняется с 1 и индексы не одинаковые
            index2 = r(0, len(binary_gen) - 1)
    binary_gen[index1], binary_gen[index2] = binary_gen[index2], binary_gen[index1]
    binary_gen = "".join(binary_gen)
    child_copy = [genes if genes != that_gen else int(binary_gen, 2) for genes in child_copy]
    return child_copy


def parents_pairing(
        individuals: list[list[int]],
        Pk: int
) -> (list[int], list[int]):
    parent1 = c(individuals)
    individuals_no_repeat = deepcopy(individuals)
    individuals_no_repeat.remove(parent1)  # дабы избежать попадание рандома на первого
    parent2 = c(individuals_no_repeat)
    while r(0, 100) <= Pk:
        parent2 = c(individuals_no_repeat)
    return parent1, parent2


def children_selection(
        parent1: list[int],
        parent2: list[int],
        matrix: list[list[int]],
        Pm: int,
        n: int
) -> (list[list[int]], list[int]):
    children = []
    load_list = []
    counter_child = 0
    crossover_result = crossover(parent1, parent2)
    for i, child in enumerate(crossover_result):
        children.append(child)
        load_list.append(count_load(child, n, matrix))
        counter_child += 1
        muted_child = mutation(child, Pm)
        children.append(muted_child)
        load_list.append(count_load(muted_child, n, matrix))
    return children, load_list
