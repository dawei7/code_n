def solve(head):
    if head is None or head.next is None:
        return head

    new_head = head.next
    previous = None
    current = head
    while current is not None and current.next is not None:
        first = current
        second = current.next
        following = second.next
        second.next = first
        first.next = following
        if previous is not None:
            previous.next = second
        previous = first
        current = following
    return new_head
