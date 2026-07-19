def solve(nums: list[int]) -> int:
    n = len(nums)
    states = {0: 0}
    index = 1

    while index + 1 < n:
        updated: dict[int, int] = {}
        first = nums[index]
        second = nums[index + 1]
        for leftover, cost in states.items():
            previous = nums[leftover]
            candidates = (
                (index + 1, cost + max(previous, first)),
                (index, cost + max(previous, second)),
                (leftover, cost + max(first, second)),
            )
            for next_leftover, next_cost in candidates:
                if next_cost < updated.get(next_leftover, 10**30):
                    updated[next_leftover] = next_cost
        states = updated
        index += 2

    if index == n:
        return min(cost + nums[leftover] for leftover, cost in states.items())
    return min(cost + max(nums[leftover], nums[index]) for leftover, cost in states.items())
