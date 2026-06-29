


def solve():
    class Solution:
        def addTwoNumbers(self, l1, l2):
            # Create a dummy node to form the new linked list
            dummyHead = Node(0)
            current = dummyHead
            carry = 0

            # Loop until both lists are finished and no carry remains
            while l1 is not None or l2 is not None or carry:
                val1 = l1.data if l1 else 0
                val2 = l2.data if l2 else 0
                total = val1 + val2 + carry
                carry = total // 10
                current.next = Node(total % 10)
                current = current.next
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next

            return dummyHead.next


if __name__ == "__main__":
    solve()
