class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ordered_values = sorted(set(nums))
        ranks = {value: index + 1 for index, value in enumerate(ordered_values)}
        size = len(ordered_values)

        suffix_maximum = [0] * len(nums)
        suffix_maximum[-1] = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            suffix_maximum[index] = max(nums[index], suffix_maximum[index + 1])

        tree = [0] * (size + 1)

        def update(index: int, value: int) -> None:
            while index <= size:
                tree[index] = max(tree[index], value)
                index += index & -index

        def prefix_maximum(index: int) -> int:
            best = 0
            while index:
                best = max(best, tree[index])
                index -= index & -index
            return best

        answer = 0
        for middle in range(1, len(nums) - 1):
            update(ranks[nums[middle - 1]], nums[middle - 1])
            right = suffix_maximum[middle + 1]
            if right > nums[middle]:
                left = prefix_maximum(ranks[nums[middle]] - 1)
                if left:
                    answer = max(answer, left - nums[middle] + right)

        return answer
