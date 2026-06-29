


def solve():
    def sortArrayByParity(nums):
        result = [0] * len(nums)
        left, right = 0, len(nums) - 1

        for num in nums:
            if num % 2 != 0:
                result[left] = num
                left += 1
            else:
                result[right] = num
                right -= 1

        # Reverse the even part to maintain relative order
        result[left:] = result[left:][::-1]

        for i in range(len(nums)):
            nums[i] = result[i]

    if __name__ == "__main__":
        N = int(input())
        nums = list(map(int, input().split()))

        sortArrayByParity(nums)

        print(" ".join(map(str, nums)))


if __name__ == "__main__":
    solve()
