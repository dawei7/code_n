def solve(nums: list[int], k: int) -> int:
    groups: dict[int, list[int]] = {}
    for value in nums:
        groups.setdefault(value % k, []).append(value)

    answer = 1
    for values in groups.values():
        values.sort()
        skip, take = 1, 0
        previous = None

        for value in values:
            if previous is not None and value - previous == k:
                skip, take = skip + take, skip
            else:
                total = skip + take
                skip, take = total, total
            previous = value

        answer *= skip + take

    return answer
