from typing import List, Optional


# Definition for a Node.
# class Node:
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next


class Solution:
    def toArray(self, node: "Optional[Node]") -> List[int]:
        while node is not None and node.prev is not None:
            node = node.prev

        values = []
        while node is not None:
            values.append(node.val)
            node = node.next
        return values
