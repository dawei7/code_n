def solve(numArrows: int, aliceArrows: list[int]) -> list[int]:
    best_score = -1
    best_allocation = [0] * 12

    for mask in range(1 << 12):
        allocation = [0] * 12
        used = 0
        score = 0
        for section in range(12):
            if mask & (1 << section):
                allocation[section] = aliceArrows[section] + 1
                used += allocation[section]
                score += section
        if used <= numArrows and score > best_score:
            allocation[0] += numArrows - used
            best_score = score
            best_allocation = allocation

    return best_allocation
