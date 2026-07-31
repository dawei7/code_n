from typing import Optional


class Node:
    """Local equivalent of the graph node supplied by LeetCode's judge."""

    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = [] if neighbors is None else neighbors


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


def solve(adj_list: list[list[int]]) -> list[list[int]]:
    if not adj_list:
        return []

    nodes = [Node(value) for value in range(1, len(adj_list) + 1)]
    for node, neighbors in zip(nodes, adj_list, strict=True):
        node.neighbors = [nodes[value - 1] for value in neighbors]

    cloned_root = Solution().cloneGraph(nodes[0])
    clones_by_value = {}
    pending = [cloned_root]
    while pending:
        node = pending.pop()
        if node.val in clones_by_value:
            continue
        clones_by_value[node.val] = node
        pending.extend(node.neighbors)

    return [[neighbor.val for neighbor in clones_by_value[value].neighbors] for value in range(1, len(adj_list) + 1)]
