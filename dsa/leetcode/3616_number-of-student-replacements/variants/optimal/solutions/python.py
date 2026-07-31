def solve(ranks: list[int]) -> int:
    if ranks.count(ranks[0]) == len(ranks):
        return 0

    best_rank = ranks[0]
    replacements = 0

    for rank in ranks:
        if rank < best_rank:
            best_rank = rank
            replacements += 1

    return replacements
