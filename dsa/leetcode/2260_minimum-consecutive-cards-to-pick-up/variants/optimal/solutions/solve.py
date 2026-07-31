def solve(cards: list[int]) -> int:
    last_index: dict[int, int] = {}
    best = len(cards) + 1
    for index, value in enumerate(cards):
        if value in last_index:
            best = min(best, index - last_index[value] + 1)
        last_index[value] = index
    return best if best <= len(cards) else -1
