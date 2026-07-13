def solve(node) -> None:
    node.val = node.next.val
    node.next = node.next.next
