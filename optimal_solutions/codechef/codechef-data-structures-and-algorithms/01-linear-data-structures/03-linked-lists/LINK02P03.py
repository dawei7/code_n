


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
            else:
                self.tail.next = new_node

            self.tail = new_node
            self.tail.next = self.head

        def deleteNode(self, value):
            # If there is only one element and it is the value to be deleted, remove it
            if self.head == self.tail and self.head.value == value:
                self.head = None
                self.tail = None
                return

            # if the target is at head set head to second element and set tail's next to the new head
            iter = self.head
            if self.head.value == value:
                self.head = self.head.next
                self.tail.next = self.head
                return

            # Now iterate over the linked list till you reach the tail and check if the next node is target
            # If it is, set current nodes next to the next of the next node and break.
            while iter.next is not None and iter != self.tail:
                if iter.next.value == value:
                    iter.next = iter.next.next
                    return
                iter = iter.next

        def printValues(self):
            if self.head is None:
                return
            else:
                current = self.head
                while True:
                    print(current.value, end=' ')
                    current = current.next
                    if current == self.head:
                        break
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
