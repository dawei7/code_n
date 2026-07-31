class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        ordered_values = sorted(set(nums))
        ranks = {value: index + 1 for index, value in enumerate(ordered_values)}
        size = len(ordered_values)

        def add(tree: List[int], index: int) -> None:
            while index <= size:
                tree[index] += 1
                index += index & -index

        def prefix_count(tree: List[int], index: int) -> int:
            count = 0
            while index:
                count += tree[index]
                index -= index & -index
            return count

        first = [nums[0]]
        second = [nums[1]]
        first_tree = [0] * (size + 1)
        second_tree = [0] * (size + 1)
        add(first_tree, ranks[nums[0]])
        add(second_tree, ranks[nums[1]])

        for value in nums[2:]:
            rank = ranks[value]
            first_greater = len(first) - prefix_count(first_tree, rank)
            second_greater = len(second) - prefix_count(second_tree, rank)

            if first_greater > second_greater or (
                first_greater == second_greater and len(first) <= len(second)
            ):
                first.append(value)
                add(first_tree, rank)
            else:
                second.append(value)
                add(second_tree, rank)

        return first + second
