from collections import Counter


def solve(basket1: list[int], basket2: list[int]) -> int:
    difference = Counter(basket1)
    difference.subtract(basket2)
    minimum = min(min(basket1), min(basket2))
    misplaced = []

    for fruit, delta in difference.items():
        if delta % 2:
            return -1
        misplaced.extend([fruit] * (abs(delta) // 2))

    misplaced.sort()
    swaps = len(misplaced) // 2
    return sum(min(fruit, 2 * minimum) for fruit in misplaced[:swaps])
