


def solve():
    class Solution:
        def detectCycle(self, head):
            if not head:
                return None
            slow = head
            fast = head
            cycle_found = False

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    cycle_found = True
                    break

            if not cycle_found:
                return None

            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow


if __name__ == "__main__":
    solve()
