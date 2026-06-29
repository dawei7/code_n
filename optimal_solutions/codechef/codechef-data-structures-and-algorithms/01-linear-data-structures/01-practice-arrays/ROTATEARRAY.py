


def solve():
    def reverse(nums, start, end):
        """Helper function to reverse part of the list"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    def rotate(nums, k):
        """Rotate nums by k steps"""
        n = len(nums)
        if n == 0:
            return nums

        k %= n  # handle k > n

        reverse(nums, 0, n - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, n - 1)
        return nums


if __name__ == "__main__":
    solve()
