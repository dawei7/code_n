"""Right-to-left Fenwick counting for LeetCode 315."""


def _count_smaller(nums: list[int]) -> list[int]:
    ranks = {value: rank for rank, value in enumerate(sorted(set(nums)), 1)}
    tree = [0] * (len(ranks) + 1)

    def prefix_sum(i: int) -> int:
        total = 0
        while i > 0:
            total += tree[i]
            i -= i & -i
        return total

    def add(i: int) -> None:
        while i < len(tree):
            tree[i] += 1
            i += i & -i

    answer = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        rank = ranks[nums[i]]
        answer[i] = prefix_sum(rank - 1)
        add(rank)
    return answer


def solve(nums: list[int]) -> list[int]:
    return _count_smaller(nums)
