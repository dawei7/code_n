def solve(fruits: list[int], baskets: list[int]) -> int:
    unplaced = 0

    for fruit in fruits:
        for index, capacity in enumerate(baskets):
            if capacity >= fruit:
                baskets[index] = 0
                break
        else:
            unplaced += 1

    return unplaced
