def solve(head):
    value = 0
    current = head
    while current is not None:
        value = value * 2 + current.val
        current = current.next
    return value
