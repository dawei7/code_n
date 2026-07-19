from typing import List, Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(
        self,
        head: Optional[ListNode],
    ) -> List[int]:
        previous = head
        current = head.next
        index = 1
        first_critical = -1
        previous_critical = -1
        minimum_distance = float("inf")

        while current.next is not None:
            next_node = current.next
            if (
                previous.val < current.val > next_node.val
                or previous.val > current.val < next_node.val
            ):
                if first_critical == -1:
                    first_critical = index
                else:
                    minimum_distance = min(
                        minimum_distance,
                        index - previous_critical,
                    )
                previous_critical = index

            previous = current
            current = next_node
            index += 1

        if minimum_distance == float("inf"):
            return [-1, -1]
        return [
            int(minimum_distance),
            previous_critical - first_critical,
        ]
