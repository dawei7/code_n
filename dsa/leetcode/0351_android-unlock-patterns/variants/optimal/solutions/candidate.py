from collections import defaultdict


def solve(m: int, n: int) -> int:
    skip = [[0] * 10 for _ in range(10)]
    for first, second, middle in (
        (1, 3, 2),
        (1, 7, 4),
        (3, 9, 6),
        (7, 9, 8),
        (1, 9, 5),
        (3, 7, 5),
        (2, 8, 5),
        (4, 6, 5),
    ):
        skip[first][second] = middle
        skip[second][first] = middle

    states = {(1 << 1, 1): 4, (1 << 2, 2): 4, (1 << 5, 5): 1}
    answer = 9 if m == 1 else 0

    for length in range(2, n + 1):
        next_states = defaultdict(int)
        for (visited, current), ways in states.items():
            for destination in range(1, 10):
                bit = 1 << destination
                middle = skip[current][destination]
                if not visited & bit and (middle == 0 or visited & (1 << middle)):
                    next_states[visited | bit, destination] += ways
        states = next_states
        if length >= m:
            answer += sum(states.values())

    return answer
