


def solve():
    class Solution:
        def largestBST(self, root):
            self.max_size = 0
            self._solve(root)
            return self.max_size

        def _solve(self, node):
            """
            Returns a tuple: (isBST, size, minVal, maxVal)
            """
            if not node:
                return True, 0, float('inf'), float('-inf')

            left_is_bst, left_size, left_min, left_max = self._solve(node.left)
            right_is_bst, right_size, right_min, right_max = self._solve(node.right)

            # If left and right subtrees are BSTs and the current node follows BST rules
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                curr_size = 1 + left_size + right_size
                self.max_size = max(self.max_size, curr_size)
                curr_min = min(left_min, node.data)
                curr_max = max(right_max, node.data)
                return True, curr_size, curr_min, curr_max

            # Otherwise, not a BST
            return False, 0, 0, 0


if __name__ == "__main__":
    solve()
