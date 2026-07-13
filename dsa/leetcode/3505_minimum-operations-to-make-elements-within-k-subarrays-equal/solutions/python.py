from bisect import bisect_left


class Fenwick:
    def __init__(self, size: int):
        self.tree = [0] * (size + 1)

    def add(self, index: int, delta: int) -> None:
        index += 1
        while index < len(self.tree):
            self.tree[index] += delta
            index += index & -index

    def sum(self, index: int) -> int:
        total = 0
        index += 1
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total

    def kth(self, target: int) -> int:
        index = 0
        bit = 1 << (len(self.tree).bit_length() - 1)
        while bit:
            nxt = index + bit
            if nxt < len(self.tree) and self.tree[nxt] < target:
                target -= self.tree[nxt]
                index = nxt
            bit //= 2
        return index


def solve(nums: list[int], x: int, k: int) -> int:
    n = len(nums)
    values = sorted(set(nums))
    compressed = [bisect_left(values, value) for value in nums]
    count_tree = Fenwick(len(values))
    sum_tree = Fenwick(len(values))
    window_cost = [0] * (n - x + 1)

    for right, (value, index) in enumerate(zip(nums, compressed)):
        count_tree.add(index, 1)
        sum_tree.add(index, value)
        if right >= x:
            old_index = compressed[right - x]
            old_value = nums[right - x]
            count_tree.add(old_index, -1)
            sum_tree.add(old_index, -old_value)
        if right >= x - 1:
            median_index = count_tree.kth((x + 1) // 2)
            median = values[median_index]
            left_count = count_tree.sum(median_index)
            left_sum = sum_tree.sum(median_index)
            total_sum = sum_tree.sum(len(values) - 1)
            right_count = x - left_count
            right_sum = total_sum - left_sum
            window_cost[right - x + 1] = (
                median * left_count - left_sum + right_sum - median * right_count
            )

    inf = 10**30
    previous = [0] * (n + 1)
    for chosen in range(1, k + 1):
        current = [inf] * (n + 1)
        for length in range(1, n + 1):
            current[length] = current[length - 1]
            if length >= x and previous[length - x] < inf:
                current[length] = min(
                    current[length],
                    previous[length - x] + window_cost[length - x],
                )
        previous = current
    return previous[n]
