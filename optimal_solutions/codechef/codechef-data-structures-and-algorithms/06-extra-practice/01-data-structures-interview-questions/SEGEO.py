


def solve():
    class Solution:
        def rearrange(self, head):
            evenDummy = Node(0)
            oddDummy = Node(0)
            evenTail = evenDummy
            oddTail = oddDummy
            current = head
            while current:
                if current.val % 2 == 0:
                    evenTail.next = current
                    evenTail = evenTail.next
                else:
                    oddTail.next = current
                    oddTail = oddTail.next
                current = current.next
            evenTail.next = oddDummy.next
            oddTail.next = None
            return evenDummy.next if evenDummy.next else oddDummy.next


if __name__ == "__main__":
    solve()
