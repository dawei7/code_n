from bisect import bisect_left, bisect_right


class RangeMax:
    def __init__(self, values: list[int]):
        self.size = 1
        while self.size < len(values):
            self.size *= 2
        self.tree = [0] * (2 * self.size)
        for index, value in enumerate(values):
            self.tree[self.size + index] = value
        for index in range(self.size - 1, 0, -1):
            self.tree[index] = max(self.tree[index * 2], self.tree[index * 2 + 1])

    def query(self, left: int, right: int) -> int:
        if left > right:
            return 0
        left += self.size
        right += self.size
        best = 0
        while left <= right:
            if left % 2 == 1:
                best = max(best, self.tree[left])
                left += 1
            if right % 2 == 0:
                best = max(best, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return best


def solve(s: str, queries: list[list[int]]) -> list[int]:
    n = len(s)
    ones_prefix = [0] * (n + 1)
    for index, char in enumerate(s):
        ones_prefix[index + 1] = ones_prefix[index] + (char == "1")

    runs: list[tuple[str, int, int]] = []
    start = 0
    for index in range(1, n + 1):
        if index == n or s[index] != s[start]:
            runs.append((s[start], start, index - 1))
            start = index

    candidates: list[tuple[int, int, int, int, int]] = []
    for run_index in range(1, len(runs) - 1):
        char, left, right = runs[run_index]
        if char == "1" and runs[run_index - 1][0] == "0" and runs[run_index + 1][0] == "0":
            left_zero_start = runs[run_index - 1][1]
            right_zero_end = runs[run_index + 1][2]
            full_gain = (left - left_zero_start) + (right_zero_end - right)
            candidates.append((left, right, left_zero_start, right_zero_end, full_gain))

    starts = [candidate[0] for candidate in candidates]
    ends = [candidate[1] for candidate in candidates]
    tree = RangeMax([candidate[4] for candidate in candidates])

    def actual_gain(index: int, left_bound: int, right_bound: int) -> int:
        left, right, left_zero_start, right_zero_end, _full = candidates[index]
        if left <= left_bound or right >= right_bound:
            return 0
        return (left - max(left_bound, left_zero_start)) + (min(right_bound, right_zero_end) - right)

    answer: list[int] = []
    total_ones = ones_prefix[n]
    for left, right in queries:
        first = bisect_right(starts, left)
        last = bisect_left(ends, right) - 1
        gain = 0
        if first <= last:
            gain = max(gain, actual_gain(first, left, right))
            if first != last:
                gain = max(gain, actual_gain(last, left, right))
                gain = max(gain, tree.query(first + 1, last - 1))
        answer.append(total_ones + gain)
    return answer
