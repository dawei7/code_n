


def solve():
    class Solution:
        def longestConsecutive(self, nums):
            if not nums:
                return 0

            num_set = set(nums)
            longest = 0

            for num in num_set:
                # check if num is the start of a sequence
                if num - 1 not in num_set:
                    current = num
                    length = 1

                    while current + 1 in num_set:
                        current += 1
                        length += 1

                    longest = max(longest, length)

            return longest


if __name__ == "__main__":
    solve()
