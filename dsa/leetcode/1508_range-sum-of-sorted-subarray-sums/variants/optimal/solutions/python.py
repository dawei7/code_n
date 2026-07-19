"""Optimal app-local solution for LeetCode 1508."""


def solve(nums: list[int], n: int, left: int, right: int) -> int:
    prefix = [0] * (n + 1)
    prefix_of_prefix = [0] * (n + 1)
    for index, value in enumerate(nums):
        prefix[index + 1] = prefix[index] + value
        prefix_of_prefix[index + 1] = prefix_of_prefix[index] + prefix[index]

    def count_and_sum(limit: int) -> tuple[int, int]:
        count = total = start = 0
        for end in range(n):
            while prefix[end + 1] - prefix[start] > limit:
                start += 1
            ending_count = end - start + 1
            count += ending_count
            total += ending_count * prefix[end + 1] - (
                prefix_of_prefix[end + 1] - prefix_of_prefix[start]
            )
        return count, total

    def first_k_sum(k: int) -> int:
        low, high = 0, prefix[-1]
        while low < high:
            middle = (low + high) // 2
            count, _ = count_and_sum(middle)
            if count >= k:
                high = middle
            else:
                low = middle + 1
        count, total = count_and_sum(low)
        return total - (count - k) * low

    return (first_k_sum(right) - first_k_sum(left - 1)) % 1_000_000_007
