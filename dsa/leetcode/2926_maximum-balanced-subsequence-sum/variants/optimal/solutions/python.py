from bisect import bisect_left


def solve(nums: list[int]) -> int:
    keys = [value - index for index, value in enumerate(nums)]
    ordered = sorted(set(keys))
    tree = [0] * (len(ordered) + 1)

    def query(index: int) -> int:
        best = 0
        while index > 0:
            best = max(best, tree[index])
            index -= index & -index
        return best

    def update(index: int, value: int) -> None:
        while index < len(tree):
            tree[index] = max(tree[index], value)
            index += index & -index

    answer = nums[0]
    for key, value in zip(keys, nums):
        rank = bisect_left(ordered, key) + 1
        current = value + query(rank)
        update(rank, current)
        answer = max(answer, current)

    return answer
