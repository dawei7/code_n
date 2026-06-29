


def solve():
    def backtrack(index, current_sum, taken, nums, k):
        # Base case
        if index == len(nums):
            return 1 if current_sum == k and taken else 0

        # Include current element
        include = backtrack(
            index + 1,
            current_sum + nums[index],
            True,
            nums,
            k
        )

        # Exclude current element
        exclude = backtrack(
            index + 1,
            current_sum,
            taken,
            nums,
            k
        )

        return include + exclude


    def countSubsequences(nums, k):
        return backtrack(0, 0, False, nums, k)


if __name__ == "__main__":
    solve()
