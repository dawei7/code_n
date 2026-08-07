class Solution:
    def getKthCharacter(self, root: Optional[object], k: int) -> str:
        """
        :type root: Optional[RopeTreeNode]
        """
        node = root

        while node.val == "":
            if node.left is None:
                left_length = 0
            elif node.left.len > 0:
                left_length = node.left.len
            else:
                left_length = len(node.left.val)

            if k <= left_length:
                node = node.left
            else:
                k -= left_length
                node = node.right

        return node.val[k - 1]
