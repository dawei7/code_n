class ListNode:
    """Local equivalent of LeetCode's ListNode for the standalone app template."""

    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def solve(head):
    read = head.next
    write = head

    while read:
        segment_sum = 0
        while read.val != 0:
            segment_sum += read.val
            read = read.next

        write.val = segment_sum
        read = read.next
        if read:
            write = write.next
        else:
            write.next = None

    return head
