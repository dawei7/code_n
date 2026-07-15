"""Optimal app-local solution for LeetCode 887."""


def solve(k, n):
    def covers(moves):
        combinations = 1
        covered = 0
        for used_eggs in range(1, min(k, moves) + 1):
            combinations = combinations * (moves - used_eggs + 1) // used_eggs
            covered += combinations
            if covered >= n:
                return True
        return False

    low, high = 1, n
    while low < high:
        moves = (low + high) // 2
        if covers(moves):
            high = moves
        else:
            low = moves + 1
    return low
