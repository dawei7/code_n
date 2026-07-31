def solve(banned: list[int], n: int, maxSum: int) -> int:
    blocked = sorted(set(value for value in banned if value <= n))
    answer = 0
    start = 1
    remaining = maxSum

    for stop in blocked + [n + 1]:
        length = stop - start
        if length > 0:
            low, high = 0, length
            while low < high:
                middle = (low + high + 1) // 2
                cost = middle * (2 * start + middle - 1) // 2
                if cost <= remaining:
                    low = middle
                else:
                    high = middle - 1

            take = low
            answer += take
            remaining -= take * (2 * start + take - 1) // 2
            if take < length:
                return answer

        start = max(start, stop + 1)

    return answer
