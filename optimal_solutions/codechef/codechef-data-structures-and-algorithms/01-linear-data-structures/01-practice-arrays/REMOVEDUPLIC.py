


def solve():
    def remove_duplicates(nums):
        if not nums:
            return 0

        k = 1  # pointer for the position of next unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    solve()
