def solve(nums: list[int], queries: list[list[int]]) -> list[int]:
    size = len(nums)
    trees = [[0] * (size + 1) for _ in range(6)]
    depths = []

    def depth(value: int) -> int:
        steps = 0
        while value != 1:
            value = value.bit_count()
            steps += 1
        return steps

    for index, value in enumerate(nums, 1):
        current_depth = depth(value)
        depths.append(current_depth)
        trees[current_depth][index] = 1

    for tree in trees:
        for index in range(1, size + 1):
            parent = index + (index & -index)
            if parent <= size:
                tree[parent] += tree[index]

    def add(tree: list[int], index: int, delta: int) -> None:
        index += 1
        while index <= size:
            tree[index] += delta
            index += index & -index

    def prefix_sum(tree: list[int], end: int) -> int:
        total = 0
        while end:
            total += tree[end]
            end -= end & -end
        return total

    answer = []
    for query in queries:
        if query[0] == 1:
            _, left, right, wanted_depth = query
            tree = trees[wanted_depth]
            answer.append(
                prefix_sum(tree, right + 1) - prefix_sum(tree, left)
            )
        else:
            _, index, value = query
            new_depth = depth(value)
            old_depth = depths[index]
            if new_depth != old_depth:
                add(trees[old_depth], index, -1)
                add(trees[new_depth], index, 1)
                depths[index] = new_depth

    return answer
