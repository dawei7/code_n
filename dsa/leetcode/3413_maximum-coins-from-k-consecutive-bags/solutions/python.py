from bisect import bisect_right


def solve(coins: list[list[int]], k: int) -> int:
    def best_starting_at_left(intervals: list[list[int]]) -> int:
        intervals.sort()
        n = len(intervals)
        starts = [left for left, _, _ in intervals]
        prefix = [0] * (n + 1)
        for index, (left, right, value) in enumerate(intervals):
            prefix[index + 1] = prefix[index] + (right - left + 1) * value

        answer = 0
        for index in range(n):
            window_right = intervals[index][0] + k - 1
            last = bisect_right(starts, window_right) - 1
            if last < index:
                continue

            current = prefix[last] - prefix[index]
            left, right, value = intervals[last]
            overlap = min(right, window_right) - left + 1
            if overlap > 0:
                current += overlap * value
            answer = max(answer, current)

        return answer

    reflected = [[-right, -left, value] for left, right, value in coins]
    return max(best_starting_at_left([coin[:] for coin in coins]), best_starting_at_left(reflected))
