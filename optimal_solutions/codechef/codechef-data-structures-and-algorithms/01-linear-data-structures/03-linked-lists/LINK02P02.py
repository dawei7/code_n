


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
            else:
                self.tail.next = new_node

            self.tail = new_node
            self.tail.next = self.head

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
        n = int(input())

        ll = LinkedList()
        vals = list(map(int, input().split()))

        for a in vals:
            ll.insertAtEnd(a)

        ll.printValues()


if __name__ == "__main__":
    solve()
