class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        values = sorted(set(nums))
        rank = {value: index + 1 for index, value in enumerate(values)}
        tree = [(0, 0)] * (len(values) + 1)

        def combine(left, right):
            if left[0] > right[0]:
                return left
            if right[0] > left[0]:
                return right
            return (left[0], left[1] + right[1])

        def query(index):
            result = (0, 0)
            while index > 0:
                result = combine(result, tree[index])
                index -= index & -index
            return result

        def update(index, state):
            while index < len(tree):
                tree[index] = combine(tree[index], state)
                index += index & -index

        for value in nums:
            current_rank = rank[value]
            length, count = query(current_rank - 1)
            update(current_rank, (length + 1, count if length else 1))

        return query(len(values))[1]

