def solve(nested_list: list) -> int:
    def weighted_sum(values: list, depth: int) -> int:
        total = 0
        for value in values:
            if isinstance(value, int):
                total += value * depth
            else:
                total += weighted_sum(value, depth + 1)
        return total

    return weighted_sum(nested_list, 1)
