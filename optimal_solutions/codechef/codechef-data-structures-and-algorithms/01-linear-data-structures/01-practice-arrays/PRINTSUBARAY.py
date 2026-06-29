


def solve():
    class Solution:
        def maxSubArray(self, nums):
            max_sum = curr_sum = nums[0]
            start = end = temp_start = 0

            for i in range(1, len(nums)):
                if curr_sum + nums[i] < nums[i]:
                    curr_sum = nums[i]
                    temp_start = i
                else:
                    curr_sum += nums[i]

                if curr_sum > max_sum:
                    max_sum = curr_sum
                    start = temp_start
                    end = i

            return nums[start:end+1]


if __name__ == "__main__":
    solve()
