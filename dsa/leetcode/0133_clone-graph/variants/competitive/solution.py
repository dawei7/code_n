from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None
        clones = {}

        def clone(original):
            if original in clones:
                return clones[original]
            copy = Node(original.val)
            clones[original] = copy
            copy.neighbors = [clone(neighbor) for neighbor in original.neighbors]
            return copy

        return clone(node)
