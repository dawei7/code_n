from typing import List


def solve(n: int, maxDistance: int, roads: List[List[int]]) -> int:
    infinity = 10**15
    valid = 0

    for mask in range(1 << n):
        distance = [[infinity] * n for _ in range(n)]
        for branch in range(n):
            if mask >> branch & 1:
                distance[branch][branch] = 0

        for first, second, length in roads:
            if mask >> first & 1 and mask >> second & 1:
                if length < distance[first][second]:
                    distance[first][second] = length
                    distance[second][first] = length

        active = [branch for branch in range(n) if mask >> branch & 1]
        for middle in active:
            for first in active:
                through_middle = distance[first][middle]
                for second in active:
                    candidate = through_middle + distance[middle][second]
                    if candidate < distance[first][second]:
                        distance[first][second] = candidate

        if all(distance[first][second] <= maxDistance for first in active for second in active):
            valid += 1

    return valid
