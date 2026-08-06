import heapq


class ListNode:
    """Local equivalent of the linked-list node supplied by LeetCode's judge."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solve(lists):
    heap = []
    for i, node in enumerate(lists):
        if node is not None:
            heapq.heappush(heap, (node.val, i, node))

    head = tail = None
    while heap:
        _, i, node = heapq.heappop(heap)
        successor = node.next
        if head is None:
            head = tail = node
        else:
            tail.next = node
            tail = node
        if successor is not None:
            heapq.heappush(heap, (successor.val, i, successor))
    return head
