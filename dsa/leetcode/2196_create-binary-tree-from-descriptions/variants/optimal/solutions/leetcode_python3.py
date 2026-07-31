from typing import List, Optional


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        children = set()

        for parent_value, child_value, is_left in descriptions:
            if parent_value not in nodes:
                nodes[parent_value] = TreeNode(parent_value)
            if child_value not in nodes:
                nodes[child_value] = TreeNode(child_value)

            if is_left:
                nodes[parent_value].left = nodes[child_value]
            else:
                nodes[parent_value].right = nodes[child_value]
            children.add(child_value)

        for value, node in nodes.items():
            if value not in children:
                return node

        return None
