


def solve():
    class Solution:
        def rearrange(self, head):
            # Base case: if the list is empty or has one element
            if not head or not head.next:
                return head

            # Split the list into two halves
            mid = self.get_mid(head)
            right = mid.next
            mid.next = None

            # Recursively sort the sublists
            left_sorted = self.rearrange(head)
            right_sorted = self.rearrange(right)

            # Merge the two sorted lists
            return self.merge(left_sorted, right_sorted)

        def get_mid(self, head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def merge(self, l1, l2):
            dummy = Node(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if l1:
                curr.next = l1
            else:
                curr.next = l2
            return dummy.next


if __name__ == "__main__":
    solve()
