"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def moveSubTree(self, root: "Node", p: "Node", q: "Node") -> "Node":
        parent = {root: None}
        stack = [root]

        while stack:
            node = stack.pop()
            for child in node.children:
                parent[child] = node
                stack.append(child)

        p_parent = parent[p]
        if p_parent is q:
            return root

        current = q
        q_is_below_p = False
        while current is not None:
            if current is p:
                q_is_below_p = True
                break
            current = parent[current]

        if q_is_below_p:
            q_parent = parent[q]
            q_parent.children.remove(q)
            if p_parent is None:
                root = q
            else:
                p_index = p_parent.children.index(p)
                p_parent.children[p_index] = q
        else:
            p_parent.children.remove(p)

        q.children.append(p)
        return root
