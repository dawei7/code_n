def solve(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    if 1 in nums:
        return False

    parent = list(range(len(nums)))
    size = [1] * len(nums)

    def find(node: int) -> int:
        while parent[node] != node:
            parent[node] = parent[parent[node]]
            node = parent[node]
        return node

    def union(first: int, second: int) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return
        if size[first_root] < size[second_root]:
            first_root, second_root = second_root, first_root
        parent[second_root] = first_root
        size[first_root] += size[second_root]

    maximum = max(nums)
    smallest_factor = list(range(maximum + 1))
    factor = 2
    while factor * factor <= maximum:
        if smallest_factor[factor] == factor:
            for multiple in range(factor * factor, maximum + 1, factor):
                if smallest_factor[multiple] == multiple:
                    smallest_factor[multiple] = factor
        factor += 1

    factor_owner: dict[int, int] = {}
    for index, value in enumerate(nums):
        remaining = value
        while remaining > 1:
            factor = smallest_factor[remaining]
            if factor in factor_owner:
                union(index, factor_owner[factor])
            else:
                factor_owner[factor] = index
            while remaining % factor == 0:
                remaining //= factor

    root = find(0)
    return all(find(index) == root for index in range(1, len(nums)))
