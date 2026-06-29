


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
                # Set the head to it's next
                self.head = self.head.next







        def printValues(self):
            current = self.head
            while current:
                print(current.value, end=' ')
                current = current.next
            print()

    if __name__ == "__main__":
        n, x = map(int, input().split())

        linked_list = LinkedList()

        vals = list(map(int, input().split()))
        for a in vals:
            linked_list.insertAtEnd(a)

        linked_list.deleteNode(x)
        linked_list.printValues()


if __name__ == "__main__":
    solve()
