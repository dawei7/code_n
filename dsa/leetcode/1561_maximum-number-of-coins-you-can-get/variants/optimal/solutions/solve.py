def solve(piles):
    ordered = sorted(piles)
    return sum(ordered[len(ordered) // 3 :: 2])
