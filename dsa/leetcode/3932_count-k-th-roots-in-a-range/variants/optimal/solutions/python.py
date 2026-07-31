def solve(l: int, r: int, k: int) -> int:
    if k == 1:
        return r - l + 1

    def count_at_most(limit: int) -> int:
        if limit < 0:
            return 0

        low, high = 0, limit
        while low <= high:
            middle = (low + high) // 2
            if middle**k <= limit:
                low = middle + 1
            else:
                high = middle - 1
        return low

    return count_at_most(r) - count_at_most(l - 1)
