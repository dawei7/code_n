def _linear_pairs(values: list[int], limit: int) -> int:
    negative = -10**30
    closed = [negative] * (limit + 1)
    closed[0] = 0
    opened = [[negative, negative] for _ in range(limit)]

    for value in values:
        old_closed = closed
        old_opened = opened
        closed = old_closed[:]
        opened = [state[:] for state in old_opened]

        for pairs in range(limit):
            closed[pairs + 1] = max(
                closed[pairs + 1],
                old_opened[pairs][0] - value,
                old_opened[pairs][1] + value,
            )
            opened[pairs][0] = max(
                opened[pairs][0], old_closed[pairs] + value
            )
            opened[pairs][1] = max(
                opened[pairs][1], old_closed[pairs] - value
            )

    return max(closed)


def _wrapped_pairs(values: list[int], limit: int, outer_sign: int) -> int:
    negative = -10**30
    outer = [negative] * limit
    inner = [[negative, negative] for _ in range(limit)]
    finished = [negative] * (limit + 1)

    for value in values:
        old_outer = outer
        old_inner = inner
        outer = old_outer[:]
        inner = [state[:] for state in old_inner]

        for pairs in range(limit):
            finished[pairs + 1] = max(
                finished[pairs + 1], old_outer[pairs] - outer_sign * value
            )
            if pairs + 1 < limit:
                outer[pairs + 1] = max(
                    outer[pairs + 1],
                    old_inner[pairs][0] - value,
                    old_inner[pairs][1] + value,
                )
                inner[pairs][0] = max(
                    inner[pairs][0], old_outer[pairs] + value
                )
                inner[pairs][1] = max(
                    inner[pairs][1], old_outer[pairs] - value
                )

        outer[0] = max(outer[0], outer_sign * value)

    return max(finished)


def solve(nums: list[int], k: int) -> int:
    limit = min(k, len(nums) // 2)
    if limit == 0:
        return 0
    return max(
        _linear_pairs(nums, limit),
        _wrapped_pairs(nums, limit, -1),
        _wrapped_pairs(nums, limit, 1),
    )
