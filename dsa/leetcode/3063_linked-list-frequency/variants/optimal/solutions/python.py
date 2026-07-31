def solve(head):
    frequencies = {}
    current = head

    while current is not None:
        frequencies[current.val] = frequencies.get(current.val, 0) + 1
        current = current.next

    node_type = type(head)
    dummy = node_type(0)
    tail = dummy
    for frequency in frequencies.values():
        tail.next = node_type(frequency)
        tail = tail.next

    return dummy.next
