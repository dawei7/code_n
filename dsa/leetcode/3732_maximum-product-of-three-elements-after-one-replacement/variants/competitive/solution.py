class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        largest = 0
        second_largest = 0
        for value in nums:
            magnitude = abs(value)
            if magnitude >= largest:
                second_largest = largest
                largest = magnitude
            elif magnitude > second_largest:
                second_largest = magnitude

        return 100000 * largest * second_largest
