


def solve():
    class Solution:    
        def pairWiseSwap(self, head):
            if head is None or head.next is None:
                return head
            dummy = Node(0)
            dummy.next = head
            prev = dummy
            while prev.next and prev.next.next:
                first = prev.next
                second = first.next
                prev.next = second
                first.next = second.next
                second.next = first
                prev = first
            return dummy.next


if __name__ == "__main__":
    solve()
