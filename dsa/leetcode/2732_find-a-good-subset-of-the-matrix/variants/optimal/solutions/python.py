def solve(grid):
    seen = {}

    for index, row in enumerate(grid):
        mask = sum(bit << column for column, bit in enumerate(row))
        if mask == 0:
            return [index]

        for other_mask, other_index in seen.items():
            if mask & other_mask == 0:
                return [other_index, index]

        if mask not in seen:
            seen[mask] = index

    return []
