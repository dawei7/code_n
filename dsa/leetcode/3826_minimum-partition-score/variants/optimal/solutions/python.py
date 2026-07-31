from collections import deque


def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    prefix = [0]
    for value in nums:
        prefix.append(prefix[-1] + value)

    infinity = 10**100
    previous = [infinity] * (n + 1)
    previous[0] = 0

    def evaluate(line: tuple[int, int], x: int) -> int:
        slope, intercept = line
        return slope * x + intercept

    def is_redundant(
        first: tuple[int, int],
        middle: tuple[int, int],
        last: tuple[int, int],
    ) -> bool:
        first_slope, first_intercept = first
        middle_slope, middle_intercept = middle
        last_slope, last_intercept = last
        return (
            (middle_intercept - first_intercept)
            * (middle_slope - last_slope)
            >= (last_intercept - middle_intercept)
            * (first_slope - middle_slope)
        )

    for groups in range(1, k + 1):
        current = [infinity] * (n + 1)

        start = groups - 1
        start_sum = prefix[start]
        hull = deque(
            [
                (
                    -start_sum,
                    previous[start]
                    + (start_sum * start_sum - start_sum) // 2,
                )
            ]
        )

        for end in range(groups, n + 1):
            total = prefix[end]
            while len(hull) >= 2 and evaluate(hull[0], total) >= evaluate(
                hull[1], total
            ):
                hull.popleft()

            current[end] = (
                (total * total + total) // 2 + evaluate(hull[0], total)
            )

            if previous[end] < infinity:
                split_sum = prefix[end]
                new_line = (
                    -split_sum,
                    previous[end]
                    + (split_sum * split_sum - split_sum) // 2,
                )
                while len(hull) >= 2 and is_redundant(
                    hull[-2], hull[-1], new_line
                ):
                    hull.pop()
                hull.append(new_line)

        previous = current

    return previous[n]
