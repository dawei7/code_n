class Solution:
    def deleteNode(self, node: Optional[ListNode]) -> None:
        node.val = node.next.val
        node.next = node.next.next
