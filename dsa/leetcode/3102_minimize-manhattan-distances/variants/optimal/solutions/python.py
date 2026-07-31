def solve(points: list[list[int]]) -> int:
    def bounds(sign: int):
        low1 = (float("inf"), -1)
        low2 = (float("inf"), -1)
        high1 = (float("-inf"), -1)
        high2 = (float("-inf"), -1)

        for index, (x, y) in enumerate(points):
            value = x + sign * y

            if value < low1[0]:
                low2 = low1
                low1 = (value, index)
            elif value < low2[0]:
                low2 = (value, index)

            if value > high1[0]:
                high2 = high1
                high1 = (value, index)
            elif value > high2[0]:
                high2 = (value, index)

        return low1, low2, high1, high2

    transformed_bounds = (bounds(1), bounds(-1))
    answer = float("inf")

    for removed in range(len(points)):
        remaining_maximum = 0
        for low1, low2, high1, high2 in transformed_bounds:
            low = low2[0] if low1[1] == removed else low1[0]
            high = high2[0] if high1[1] == removed else high1[0]
            remaining_maximum = max(remaining_maximum, high - low)
        answer = min(answer, remaining_maximum)

    return answer
