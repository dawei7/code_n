class FenwickTree:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        total = 0
        index += 1
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def range_sum(self, left: int, right: int) -> int:
        if left > right:
            return 0
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    nums = list(nums)
    n = len(nums)
    peak = [0] * n
    peaks = FenwickTree(n)

    def is_peak(index: int) -> int:
        return int(
            0 < index < n - 1
            and nums[index] > nums[index - 1]
            and nums[index] > nums[index + 1]
        )

    for index in range(1, n - 1):
        peak[index] = is_peak(index)
        if peak[index]:
            peaks.add(index, 1)

    answer = []
    for query_type, first, second in queries:
        if query_type == 1:
            answer.append(peaks.range_sum(first + 1, second - 1))
            continue

        affected = range(max(1, first - 1), min(n - 2, first + 1) + 1)
        for index in affected:
            if peak[index]:
                peaks.add(index, -1)

        nums[first] = second

        for index in affected:
            peak[index] = is_peak(index)
            if peak[index]:
                peaks.add(index, 1)

    return answer
