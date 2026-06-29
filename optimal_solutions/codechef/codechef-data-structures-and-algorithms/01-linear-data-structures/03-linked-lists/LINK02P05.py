


def solve():
    class LinkedList:
        def __init__(self):
            self.head = None

        def insert_at_index(self, index, value):
            new_node = Node(value)

            if index == 0:
                new_node.next = self.head
                if self.head is not None:
                    self.head.prev = new_node
                self.head = new_node
            else:
                iter_node = self.head
                for _ in range(index - 1):
                    iter_node = iter_node.next

                A = iter_node
                B = iter_node.next

                A.next = new_node
                if B is not None:
                    B.prev = new_node

                new_node.next = B
                new_node.prev = A

        def print_values(self):
            current = self.head
            while current is not None:
                print(current.value, end=' ')
                current = current.next
            print()


if __name__ == "__main__":
    solve()
