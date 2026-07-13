def solve(fruits: list[int], baskets: list[int]) -> int:
    placed = 0
    n = len(baskets)
    used = [False] * n

    for fruit in fruits:
        for i in range(n):
            if not used[i] and baskets[i] >= fruit:
                used[i] = True
                placed += 1
                break

    return n - placed
