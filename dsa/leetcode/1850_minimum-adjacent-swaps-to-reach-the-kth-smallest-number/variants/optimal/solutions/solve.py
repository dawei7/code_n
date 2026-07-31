from collections import deque


def solve(num: str, k: int) -> int:
    target = list(num)
    for _ in range(k):
        pivot = len(target) - 2
        while target[pivot] >= target[pivot + 1]:
            pivot -= 1

        successor = len(target) - 1
        while target[successor] <= target[pivot]:
            successor -= 1

        target[pivot], target[successor] = target[successor], target[pivot]
        target[pivot + 1 :] = reversed(target[pivot + 1 :])

    positions = [deque() for _ in range(10)]
    for index, digit in enumerate(num):
        positions[int(digit)].append(index)

    source_indices = [positions[int(digit)].popleft() for digit in target]
    tree = [0] * (len(num) + 1)

    def prefix_sum(index: int) -> int:
        total = 0
        while index:
            total += tree[index]
            index -= index & -index
        return total

    swaps = 0
    for seen, source_index in enumerate(source_indices):
        tree_index = source_index + 1
        swaps += seen - prefix_sum(tree_index)
        while tree_index < len(tree):
            tree[tree_index] += 1
            tree_index += tree_index & -tree_index

    return swaps
