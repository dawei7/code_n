def solve(head):
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values
