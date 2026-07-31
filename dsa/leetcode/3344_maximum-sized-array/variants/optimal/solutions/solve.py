def solve(s: int) -> int:
    def array_sum(size: int) -> int:
        index_sum = size * (size - 1) // 2
        pair_or_sum = 0
        bit = 1

        while bit < size:
            cycle = bit * 2
            zero_count = (size // cycle) * bit + min(size % cycle, bit)
            pair_or_sum += bit * (size * size - zero_count * zero_count)
            bit *= 2

        return index_sum * pair_or_sum

    low = 1
    high = 2
    while array_sum(high) <= s:
        low = high
        high *= 2

    while low + 1 < high:
        middle = (low + high) // 2
        if array_sum(middle) <= s:
            low = middle
        else:
            high = middle

    return low
