def solve(mat: list[list[int]], target: int) -> int:
    reachable = {0}

    for row in mat:
        next_sums = {
            current + value
            for current in reachable
            for value in set(row)
        }
        above = [total for total in next_sums if total > target]
        reachable = {total for total in next_sums if total <= target}
        if above:
            reachable.add(min(above))

    return min(abs(total - target) for total in reachable)
