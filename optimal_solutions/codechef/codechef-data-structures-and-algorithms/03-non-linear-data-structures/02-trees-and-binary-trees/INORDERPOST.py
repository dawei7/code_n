


def solve():
    class Solution:
        def buildTree(self, inorder, postorder):
            index_map = {val: idx for idx, val in enumerate(inorder)}
            return self._helper(inorder, postorder, 0, len(inorder) - 1,
                                0, len(postorder) - 1, index_map)

        def _helper(self, inorder, postorder, in_start, in_end,
                    post_start, post_end, index_map):
            if in_start > in_end or post_start > post_end:
                return None

            root_val = postorder[post_end]
            root = TreeNode(root_val)
            in_root_index = index_map[root_val]
            left_size = in_root_index - in_start

            root.left = self._helper(inorder, postorder, 
                                     in_start, in_root_index - 1,
                                     post_start, post_start + left_size - 1,
                                     index_map)

            root.right = self._helper(inorder, postorder,
                                      in_root_index + 1, in_end,
                                      post_start + left_size, post_end - 1,
                                      index_map)
            return root


if __name__ == "__main__":
    solve()
