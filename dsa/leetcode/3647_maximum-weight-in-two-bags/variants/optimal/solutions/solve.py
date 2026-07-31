def solve(weights: list[int], w1: int, w2: int) -> int:
    reachable = [[False] * (w2 + 1) for _ in range(w1 + 1)]
    reachable[0][0] = True

    for weight in weights:
        for first in range(w1, -1, -1):
            for second in range(w2, -1, -1):
                if not reachable[first][second]:
                    continue
                if first + weight <= w1:
                    reachable[first + weight][second] = True
                if second + weight <= w2:
                    reachable[first][second + weight] = True

    return max(first + second for first in range(w1 + 1) for second in range(w2 + 1) if reachable[first][second])
