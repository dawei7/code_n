


def solve():
    class Node:
        def __init__(self, val):
            self.value = val
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def insertAtEnd(self, value):
            new_node = Node(value)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return

            self.tail.next = new_node
            self.tail = new_node

        def deleteNode(self, value):
            if self.head.value == value:
                self.head = self.head.next
                return

            iter = self.head

            # Traverse the list
            # When next element is our target element, eliminate it

            while iter.next:
                if iter.next.value == value:
                    # Set next of iter
                    # To next to next of iter
                    iter.next = iter.next.next
                    return
                iter = iter.next


        def printValues(self):
            current = self.head
            while current:
                print(current.value, end=' ')
                current = current.next
            print()

    if __name__ == "__main__":
        n, x = map(int, input().split())

        ll = LinkedList()
        vals = list(map(int, input().split()))
        for a in vals:
            ll.insertAtEnd(a)

        ll.deleteNode(x)
        ll.printValues()


if __name__ == "__main__":
    solve()
