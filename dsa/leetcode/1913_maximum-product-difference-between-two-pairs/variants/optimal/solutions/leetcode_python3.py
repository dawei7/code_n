from typing import List


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        smallest = second_smallest = float("inf")
        largest = second_largest = float("-inf")

        for value in nums:
            if value <= smallest:
                second_smallest = smallest
                smallest = value
            elif value < second_smallest:
                second_smallest = value

            if value >= largest:
                second_largest = largest
                largest = value
            elif value > second_largest:
                second_largest = value

        return largest * second_largest - smallest * second_smallest
