


def solve():
    class Solution:
        @staticmethod
        def create_bst(nums):
            def helper(left, right):
                if left > right:
                    return None

                mid = (left + right) // 2
                root = Node(nums[mid])
                root.left = helper(left, mid - 1)
                root.right = helper(mid + 1, right)
                return root

            return helper(0, len(nums) - 1)


if __name__ == "__main__":
    solve()
