def solve(nums: list[int], k: int, m: int) -> int:
    n = len(nums)
    prefix = [0] * (n + 1)
    for index, value in enumerate(nums):
        prefix[index + 1] = prefix[index] + value

    negative_infinity = -(10**30)
    previous = [0] * (n + 1)

    for chosen in range(1, k + 1):
        current = [negative_infinity] * (n + 1)
        best_start = negative_infinity

        for end in range(chosen * m, n + 1):
            start = end - m
            best_start = max(
                best_start,
                previous[start] - prefix[start],
            )
            current[end] = max(
                current[end - 1],
                prefix[end] + best_start,
            )

        previous = current

    return previous[n]
