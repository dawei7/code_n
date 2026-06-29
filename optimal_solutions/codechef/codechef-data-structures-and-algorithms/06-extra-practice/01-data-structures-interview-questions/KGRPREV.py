


def solve():
    def reverse_m_size_groups(head, M):
        if not head or M <= 1:
            return head

        # Helper function to reverse k nodes in the list.
        # It returns the new head after reversal and the original head becomes the tail.
        def reverse_list(group_head, k):
            prev = None
            curr = group_head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev, group_head

        dummy = Node(0)
        dummy.next = head
        group_prev = dummy

        while head:
            # Check if we have M nodes remaining
            tail = head
            count = 1
            while count < M and tail:
                tail = tail.next
                count += 1
            if not tail:
                break

            next_group = tail.next  # Mark next group's start
            tail.next = None        # Disconnect current group

            # Reverse current group
            new_head, new_tail = reverse_list(head, M)
            # Connect reversed group with previous part
            group_prev.next = new_head
            new_tail.next = next_group

            # Prepare for next iteration
            group_prev = new_tail
            head = next_group

        return dummy.next


if __name__ == "__main__":
    solve()
