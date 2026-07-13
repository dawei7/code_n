from typing import List


def _count_range_sums(nums: List[int], lower: int, upper: int) -> int:
    prefixes = [0]
    for value in nums:
        prefixes.append(prefixes[-1] + value)
    buffer = [0] * len(prefixes)

    def sort_and_count(left: int, right: int) -> int:
        if right - left <= 1:
            return 0
        middle = (left + right) // 2
        count = sort_and_count(left, middle) + sort_and_count(middle, right)

        lower_index = upper_index = middle
        for first in range(left, middle):
            while lower_index < right and prefixes[lower_index] - prefixes[first] < lower:
                lower_index += 1
            while upper_index < right and prefixes[upper_index] - prefixes[first] <= upper:
                upper_index += 1
            count += upper_index - lower_index

        first = left
        second = middle
        output = left
        while first < middle and second < right:
            if prefixes[first] <= prefixes[second]:
                buffer[output] = prefixes[first]
                first += 1
            else:
                buffer[output] = prefixes[second]
                second += 1
            output += 1
        while first < middle:
            buffer[output] = prefixes[first]
            first += 1
            output += 1
        while second < right:
            buffer[output] = prefixes[second]
            second += 1
            output += 1
        prefixes[left:right] = buffer[left:right]
        return count

    return sort_and_count(0, len(prefixes))


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        return _count_range_sums(nums, lower, upper)
