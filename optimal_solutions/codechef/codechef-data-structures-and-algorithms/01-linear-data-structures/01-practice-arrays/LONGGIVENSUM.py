


def solve():
    class Solution:
        def longestSubarraySum(self, nums, k):
            prefix_index = {}  # prefix_sum -> first index
            prefix_sum = 0
            max_len = 0

            for i, num in enumerate(nums):
                prefix_sum += num

                # Case: subarray from 0 to i
                if prefix_sum == k:
                    max_len = i + 1

                # Case: subarray ending at i
                if (prefix_sum - k) in prefix_index:
                    max_len = max(max_len, i - prefix_index[prefix_sum - k])

                # Store only first occurrence of this prefix sum
                if prefix_sum not in prefix_index:
                    prefix_index[prefix_sum] = i

            return max_len


if __name__ == "__main__":
    solve()
