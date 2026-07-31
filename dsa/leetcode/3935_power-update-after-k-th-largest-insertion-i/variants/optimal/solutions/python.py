from heapq import heapify, heappop, heappush


def solve(
    nums: list[int],
    p: int,
    queries: list[list[int]],
) -> list[int]:
    modulus = 1_000_000_007
    top: list[int] = []
    remaining = [-value for value in nums]
    heapify(remaining)
    answer = []

    for value, k in queries:
        if top and value >= top[0]:
            heappush(top, value)
        else:
            heappush(remaining, -value)

        while len(top) > k:
            heappush(remaining, -heappop(top))
        while len(top) < k:
            heappush(top, -heappop(remaining))

        p = pow(p, top[0], modulus)
        answer.append(p)

    return answer
