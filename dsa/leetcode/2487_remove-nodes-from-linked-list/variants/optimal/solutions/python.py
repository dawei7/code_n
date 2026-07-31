class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(head: ListNode) -> list[int]:
    reversed_head = None
    current = head
    while current:
        following = current.next
        current.next = reversed_head
        reversed_head = current
        current = following

    maximum = 0
    kept_head = None
    current = reversed_head
    while current:
        following = current.next
        if current.val >= maximum:
            maximum = current.val
            current.next = kept_head
            kept_head = current
        current = following

    values = []
    current = kept_head
    while current:
        values.append(current.val)
        current = current.next
    return values
