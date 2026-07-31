from collections import defaultdict


def solve(nums: list[int]) -> int:
    n = len(nums)
    size = 1
    while size < n:
        size <<= 1

    negative_infinity = -(10**30)
    tree = [(0, negative_infinity, negative_infinity, negative_infinity) for _ in range(2 * size)]

    def make_node(value: int) -> tuple[int, int, int, int]:
        return (value, value, value, value)

    def make_removed_node() -> tuple[int, int, int, int]:
        return (0, negative_infinity, negative_infinity, negative_infinity)

    def merge(left, right):
        total = left[0] + right[0]
        prefix = max(left[1], left[0] + right[1])
        suffix = max(right[2], right[0] + left[2])
        best = max(left[3], right[3], left[2] + right[1])
        return (total, prefix, suffix, best)

    for index, value in enumerate(nums):
        tree[size + index] = make_node(value)
    for index in range(size - 1, 0, -1):
        tree[index] = merge(tree[index * 2], tree[index * 2 + 1])

    def update(position: int, value: int | None) -> None:
        index = size + position
        tree[index] = make_removed_node() if value is None else make_node(value)
        index //= 2
        while index:
            tree[index] = merge(tree[index * 2], tree[index * 2 + 1])
            index //= 2

    positions = defaultdict(list)
    for index, value in enumerate(nums):
        if value < 0:
            positions[value].append(index)

    answer = tree[1][3]
    for value, indices in positions.items():
        for index in indices:
            update(index, None)
        answer = max(answer, tree[1][3])
        for index in indices:
            update(index, value)

    return answer
