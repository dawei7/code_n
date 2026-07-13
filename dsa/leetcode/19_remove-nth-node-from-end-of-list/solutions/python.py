def solve(head, n: int):
    fast = head
    for _ in range(n):
        fast = fast.next
    if fast is None:
        return head.next

    slow = head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
