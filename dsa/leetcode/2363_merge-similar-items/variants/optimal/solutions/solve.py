from typing import List


def solve(items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
    weights = [0] * 1001
    for value, weight in items1:
        weights[value] += weight
    for value, weight in items2:
        weights[value] += weight
    return [[value, weights[value]] for value in range(1, 1001) if weights[value]]
