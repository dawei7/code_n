def solve(price: list[int], k: int) -> int:
    price.sort()

    def can_select(minimum_gap: int) -> bool:
        chosen = 1
        last_price = price[0]

        for index in range(1, len(price)):
            if price[index] - last_price >= minimum_gap:
                chosen += 1
                last_price = price[index]
                if chosen == k:
                    return True

        return False

    low = 0
    high = (price[-1] - price[0]) // (k - 1)

    while low <= high:
        middle = (low + high) // 2
        if can_select(middle):
            low = middle + 1
        else:
            high = middle - 1

    return high
