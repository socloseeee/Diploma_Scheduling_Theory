from copy import deepcopy
from random import randint as r, choice as c

import numpy as np

from diploma.utils.GA_utils import count_load, best_load, mutation, crossover, parents_pairing, children_selection


def genetic_algorithm(
        n: int = None, k: int = None, z: int = None, Pk: int = None, Pm: int = None,
        best_result: int = None,
        best_of_all_generations_result: int = None,
        matrix: list = None,
        individuals: list = None,
) -> int:
    counter, gen_count = 0, 0

    while k != counter - 1:
        gen_count += 1
        generation = []
        for _ in range(z):

            # Алгоритм образования пар родителей:
            parent1, parent2 = parents_pairing(individuals, Pk)

            # Алгоритм отбора детей из потенциальных особей (2 + 2 мутанта)
            children, load_list = children_selection(parent1, parent2, matrix, Pm, n)
            best_child_load, best_child_index = best_load(load_list)
            generation.append(children[best_child_index])

        # Список всех детей:
        listMax = []
        for i, child in enumerate(generation):
            listMax.append(count_load(child, n, matrix))

        # Собираем матрицу родителей и лучших детей для отбора:
        check_matrix, parent_child_loads = [], []
        for elem in generation:
            check_matrix.append(elem)
            parent_child_loads.append(max(count_load(elem, n, matrix)))
        for elem in individuals:
            check_matrix.append(elem)
            parent_child_loads.append(max(count_load(elem, n, matrix)))

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

        # Если сквозь поколения была лучшая загрузка ждем когда она не повторится или улучшится:
        if best_result < best_of_all_generations_result:
            best_of_all_generations_result = best_result
            counter = 0

        # Если загрузка предыдущего поколения равна загрузке текущего
        if best_of_all_generations_result == best_result:
            counter += 1
        else:
            counter = 0
        # print(best_result, list(count_load(elem, n, matrix) for elem in check_matrix))
    return best_result
