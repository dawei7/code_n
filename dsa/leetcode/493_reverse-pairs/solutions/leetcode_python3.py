from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        buffer = [0] * len(nums)

        def sort_and_count(left, right):
            if right - left <= 1:
                return 0
            middle = (left + right) // 2
            count = sort_and_count(left, middle) + sort_and_count(middle, right)

            partner = middle
            for index in range(left, middle):
                while partner < right and nums[index] > 2 * nums[partner]:
                    partner += 1
                count += partner - middle

            first, second, write = left, middle, left
            while first < middle and second < right:
                if nums[first] <= nums[second]:
                    buffer[write] = nums[first]
                    first += 1
                else:
                    buffer[write] = nums[second]
                    second += 1
                write += 1
            while first < middle:
                buffer[write] = nums[first]
                first += 1
                write += 1
            while second < right:
                buffer[write] = nums[second]
                second += 1
                write += 1
            nums[left:right] = buffer[left:right]
            return count

        return sort_and_count(0, len(nums))
