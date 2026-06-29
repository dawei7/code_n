


def solve():
    class Solution:
        def findLeaders(self, nums):
            n = len(nums)
            leaders = []
            max_from_right = nums[-1]

            # Last element is always a leader
            leaders.append(nums[-1])

            # Traverse from right to left
            for i in range(n - 2, -1, -1):
                if nums[i] > max_from_right:
                    leaders.append(nums[i])
                    max_from_right = nums[i]

            # Reverse to maintain order of appearance
            leaders.reverse()
            return leaders


if __name__ == "__main__":
    solve()
