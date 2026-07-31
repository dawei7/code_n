def solve(nums: list[int], head):
    removed = set(nums)

    while head is not None and head.val in removed:
        head = head.next

    current = head
    while current is not None and current.next is not None:
        if current.next.val in removed:
            current.next = current.next.next
        else:
            current = current.next

    return head
