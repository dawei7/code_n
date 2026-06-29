


def solve():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def removeDuplicates(head):
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        current = head
        while current is not None:
            # If current node has a duplicate
            if current.next is not None and current.data == current.next.data:
                dup_val = current.data
                # Skip all nodes with duplicate value
                while current is not None and current.data == dup_val:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next
        return dummy.next


if __name__ == "__main__":
    solve()
