from typing import List


class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        total = sum(nums[:k])
        if total % 2 == 0:
            return total

        smallest_selected = [None, None]
        for value in nums[:k]:
            smallest_selected[value % 2] = value

        largest_unselected = [None, None]
        for value in nums[k:]:
            parity = value % 2
            if largest_unselected[parity] is None:
                largest_unselected[parity] = value

        best = -1
        for selected_parity in (0, 1):
            selected = smallest_selected[selected_parity]
            replacement = largest_unselected[1 - selected_parity]
            if selected is not None and replacement is not None:
                best = max(best, total - selected + replacement)
        return best
