from typing import Optional


class Node:
    """Local equivalent of the random-list node supplied by LeetCode's judge."""

    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional["Node"]) -> Optional["Node"]:
        current = head
        while current is not None:
            copy = Node(current.val, current.next)
            current.next = copy
            current = copy.next

        current = head
        while current is not None:
            copy = current.next
            copy.random = current.random.next if current.random is not None else None
            current = copy.next

        dummy = Node(0)
        copy_tail = dummy
        current = head
        while current is not None:
            copy = current.next
            current.next = copy.next
            copy_tail.next = copy
            copy_tail = copy
            current = current.next
        return dummy.next


def solve(nodes: list[list[int | None]]) -> list[list[int | None]]:
    original_nodes = [Node(entry[0]) for entry in nodes]
    for index, (_, random_index) in enumerate(nodes):
        if index + 1 < len(original_nodes):
            original_nodes[index].next = original_nodes[index + 1]
        if random_index is not None:
            original_nodes[index].random = original_nodes[random_index]

    copied_head = Solution().copyRandomList(original_nodes[0] if original_nodes else None)
    copied_nodes = []
    current = copied_head
    while current is not None:
        copied_nodes.append(current)
        current = current.next
    index_by_node = {node: index for index, node in enumerate(copied_nodes)}
    return [[node.val, index_by_node[node.random] if node.random is not None else None] for node in copied_nodes]
