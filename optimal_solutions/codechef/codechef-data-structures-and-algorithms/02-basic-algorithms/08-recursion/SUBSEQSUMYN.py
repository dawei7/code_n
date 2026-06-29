


def solve():
    def existsSubsequence(nums, n, k):
        n = len(nums)

        def helper(index, current_sum):
            # If target sum is reached
            if current_sum == k:
                return True

            # If end of array is reached or sum exceeds k
            if index == n or current_sum > k:
                return False

            # Include current element
            if helper(index + 1, current_sum + nums[index]):
                return True

            # Exclude current element
            if helper(index + 1, current_sum):
                return True

            return False

        return helper(0, 0)


if __name__ == "__main__":
    solve()
