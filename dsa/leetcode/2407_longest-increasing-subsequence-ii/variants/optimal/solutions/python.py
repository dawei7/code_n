def solve(nums: list[int], k: int) -> int:
    leaf_count = 1
    while leaf_count <= max(nums):
        leaf_count <<= 1
    tree = [0] * (2 * leaf_count)

    def range_maximum(left: int, right: int) -> int:
        left += leaf_count
        right += leaf_count
        maximum = 0
        while left < right:
            if left & 1:
                maximum = max(maximum, tree[left])
                left += 1
            if right & 1:
                right -= 1
                maximum = max(maximum, tree[right])
            left >>= 1
            right >>= 1
        return maximum

    answer = 0
    for value in nums:
        current = 1 + range_maximum(max(1, value - k), value)
        position = leaf_count + value
        tree[position] = max(tree[position], current)
        position >>= 1
        while position:
            tree[position] = max(tree[2 * position], tree[2 * position + 1])
            position >>= 1
        answer = max(answer, current)

    return answer
