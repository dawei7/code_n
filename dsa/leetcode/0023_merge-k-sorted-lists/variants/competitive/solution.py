import heapq
from typing import List, Optional


class Solution:
    def mergeKLists(self, lists: List[Optional["ListNode"]]) -> Optional["ListNode"]:
        heap = []
        for index, node in enumerate(lists):
            if node is not None:
                heapq.heappush(heap, (node.val, index, node))

        head = tail = None
        while heap:
            _, index, node = heapq.heappop(heap)
            successor = node.next
            if head is None:
                head = tail = node
            else:
                tail.next = node
                tail = node
            if successor is not None:
                heapq.heappush(heap, (successor.val, index, successor))
        return head
