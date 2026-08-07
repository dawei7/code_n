class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:
        answer = 0

        for left in range(len(nums)):
            total = 0
            for right in range(left, len(nums)):
                total += nums[right]
                if total % 10 != x:
                    continue

                leading = total
                while leading >= 10:
                    leading //= 10
                if leading == x:
                    answer += 1

        return answer
