def solve(head, x: int):
    lower_head = lower_tail = None
    upper_head = upper_tail = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = None
        if current.val < x:
            if lower_head is None:
                lower_head = current
            else:
                lower_tail.next = current
            lower_tail = current
        else:
            if upper_head is None:
                upper_head = current
            else:
                upper_tail.next = current
            upper_tail = current
        current = next_node

    if lower_head is None:
        return upper_head
    lower_tail.next = upper_head
    return lower_head
