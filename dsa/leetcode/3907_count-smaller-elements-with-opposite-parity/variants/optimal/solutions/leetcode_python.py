class Solution:
    def countSmallerOppositeParity(self, nums: list[int]) -> list[int]:
        values = sorted(set(nums))
        rank = {value: index + 1 for index, value in enumerate(values)}
        trees = [[0] * (len(values) + 1) for _ in range(2)]
        answer = [0] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            value = nums[i]
            parity = value & 1

            index = rank[value] - 1
            tree = trees[parity ^ 1]
            while index > 0:
                answer[i] += tree[index]
                index -= index & -index

            index = rank[value]
            tree = trees[parity]
            while index < len(tree):
                tree[index] += 1
                index += index & -index

        return answer
