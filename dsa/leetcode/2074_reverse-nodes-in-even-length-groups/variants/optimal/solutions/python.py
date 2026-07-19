def solve(head):
    group_tail = head
    target_length = 2

    while group_tail is not None and group_tail.next is not None:
        actual_length = 0
        after_group = group_tail.next
        while actual_length < target_length and after_group is not None:
            actual_length += 1
            after_group = after_group.next

        if actual_length % 2 == 0:
            old_head = group_tail.next
            current = old_head
            previous = after_group
            for _ in range(actual_length):
                following = current.next
                current.next = previous
                previous = current
                current = following
            group_tail.next = previous
            group_tail = old_head
        else:
            for _ in range(actual_length):
                group_tail = group_tail.next

        target_length += 1

    return head
