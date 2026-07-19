"""Optimal solution for LeetCode 1057: Campus Bikes."""


def solve(workers: list[list[int]], bikes: list[list[int]]) -> list[int]:
    max_distance = 1998
    pairs_by_distance: list[list[tuple[int, int]]] = [
        [] for _ in range(max_distance + 1)
    ]

    for worker_index, (worker_x, worker_y) in enumerate(workers):
        for bike_index, (bike_x, bike_y) in enumerate(bikes):
            distance = abs(worker_x - bike_x) + abs(worker_y - bike_y)
            pairs_by_distance[distance].append((worker_index, bike_index))

    answer = [-1] * len(workers)
    used_bikes = [False] * len(bikes)
    assigned = 0

    for pairs in pairs_by_distance:
        for worker_index, bike_index in pairs:
            if answer[worker_index] != -1 or used_bikes[bike_index]:
                continue
            answer[worker_index] = bike_index
            used_bikes[bike_index] = True
            assigned += 1
            if assigned == len(workers):
                return answer

    return answer
