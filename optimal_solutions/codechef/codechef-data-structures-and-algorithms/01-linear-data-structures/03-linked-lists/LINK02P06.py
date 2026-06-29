


def solve():
    class Node:
        def __init__(self, val):
            self.value = val
            self.next = None
            self.prev = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def insertAtIndex(self, index, value):
            new_node = Node(value)

            if index == 0:
                new_node.next = self.head
                if self.head:
                    self.head.prev = new_node
                self.head = new_node
            else:
                iter = self.head
                for _ in range(index - 1):
                    iter = iter.next

                A = iter
                B = iter.next

                A.next = new_node
                if B:
                    B.prev = new_node

                new_node.next = B
                new_node.prev = A

        def deleteNode(self, value):
            target_node = self.head
            while target_node and target_node.value != value:
                target_node = target_node.next

            if not target_node:
                return

            A = target_node.prev
            B = target_node.next

            if A:
                A.next = B

            if B:
                B.prev = A

            if target_node == self.head:
                self.head = B

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
        for i in range(len(vals)):
            a = vals[i]
            ll.insertAtIndex(i, a)

        ll.deleteNode(x)
        ll.printValues()


if __name__ == "__main__":
    solve()
