class Node:
    """Local equivalent of LeetCode's circular singly linked-list node."""

    def __init__(self, val: int = 0, next: "Node | None" = None):
        self.val = val
        self.next = next


def solve(head: Node | None, insertVal: int) -> Node:
    if head is None:
        node = Node(insertVal)
        node.next = node
        return node

    current = head
    while True:
        following = current.next
        normal_gap = current.val <= insertVal <= following.val
        wrap_gap = current.val > following.val and (insertVal >= current.val or insertVal <= following.val)
        if normal_gap or wrap_gap:
            break
        current = following
        if current is head:
            break

    node = Node(insertVal)
    node.next = current.next
    current.next = node
    return head
