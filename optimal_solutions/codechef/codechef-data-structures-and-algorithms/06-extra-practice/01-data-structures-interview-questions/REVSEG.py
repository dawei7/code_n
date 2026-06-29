


def solve():
    def reverseSegment(head, L, R):
        if not head or L == R:
            return head

        dummy = Node(0)
        dummy.next = head
        prev = dummy

        # move prev to node before L-th position
        for _ in range(L - 1):
            prev = prev.next

        # reversal process starts
        reversal_tail = prev.next
        curr = reversal_tail
        prev_reverse = None
        for _ in range(R - L + 1):
            next_temp = curr.next
            curr.next = prev_reverse
            prev_reverse = curr
            curr = next_temp

        # reconnect the reversed segment with the list
        prev.next = prev_reverse
        reversal_tail.next = curr

        return dummy.next


if __name__ == "__main__":
    solve()
