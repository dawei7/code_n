def solve(head):
    current = head

    while current.next is not None:
        if current.next.val < 0:
            moved = current.next
            current.next = moved.next
            moved.next = head
            head = moved
        else:
            current = current.next

    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next

    return values
