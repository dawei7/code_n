"""Stack-based traversal for LeetCode 1265's immutable-node interface."""


def solve(head) -> None:
    nodes = []
    current = head
    while current is not None:
        nodes.append(current)
        current = current.getNext()

    while nodes:
        nodes.pop().printValue()
