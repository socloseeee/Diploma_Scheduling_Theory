from copy import deepcopy

import numpy as np
from colorama import Fore, Style


def min_elem_method(matrix: np.ndarray, m: int, n: int) -> (np.ndarray, np.ndarray):
    new_matrix, result = [], [0] * n
    for j in range(m):
        new_matrix.append([])
        check = 0  # check - позволяет вычленять из двух одинаковых только первое левое значение
        for i in range(n):
            if matrix[j][i] != min(matrix[j]) or matrix[j][i] == check:
                new_matrix[j].append(matrix[j][i])
            else:
                result[i] += matrix[j][i]
                new_matrix[j].append(Fore.RED + str(matrix[j][i]) + Style.RESET_ALL)
                check = int(matrix[j][i])
    min_elem_method = deepcopy(new_matrix)
    return result, min_elem_method


def plotnikov_zverev_method(matrix: np.ndarray, m: int, n: int) -> (np.ndarray, np.ndarray):
    result_str = [0] * n
    plotnikov_zverev_method = deepcopy(matrix)
    for j in range(m):
        for i in range(n):
            result_str[i] += matrix[j][i]
        min_index = result_str.index(min(result_str))
        for i in range(n):
            if i != min_index:
                result_str[i] -= matrix[j][i]
        plotnikov_zverev_method[j][min_index] = Fore.RED + str(matrix[j][min_index]) + Style.RESET_ALL
    return result_str, plotnikov_zverev_method


def barrier_method(matrix: np.ndarray, m: int, n: int, min_method_result: np.ndarray) -> (np.ndarray, np.ndarray):
    barrier = sum(min_method_result) / n
    result_str2 = [0] * n
    barrier_method = []
    flag = False
    for j in range(m):
        if not flag:
            barrier_method.append([])
            check = 0  # check - позволяет вычленять из двух одинаковых только первое левое значение
            for i in range(n):
                if matrix[j][i] != min(matrix[j]) or matrix[j][i] == check:
                    barrier_method[j].append(str(matrix[j][i]))
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
            barrier_method.append([Fore.RED + str(matrix[j][i]).ljust(
                2) + Style.RESET_ALL if min_index == i else str(matrix[j][i]).ljust(2) for i in
                                   range(len(result_str2))])
    return result_str2, barrier_method
