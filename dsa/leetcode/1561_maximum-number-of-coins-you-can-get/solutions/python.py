def solve(piles):
    piles = sorted(piles)
    groups = len(piles) // 3
    total = 0
    index = len(piles) - 2
    for _ in range(groups):
        total += piles[index]
        index -= 2
    return total
