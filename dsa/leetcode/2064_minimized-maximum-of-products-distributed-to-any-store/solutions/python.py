def solve(n: int, quantities: list[int]) -> int:
    low = 1
    high = max(quantities)

    while low < high:
        limit = (low + high) // 2
        stores_needed = sum(
            (quantity + limit - 1) // limit for quantity in quantities
        )
        if stores_needed <= n:
            high = limit
        else:
            low = limit + 1

    return low
