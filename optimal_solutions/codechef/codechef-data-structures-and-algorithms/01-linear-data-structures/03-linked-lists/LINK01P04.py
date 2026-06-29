


def solve():
    class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None

        def insert_at_end(self, value):
            new_node = Node(value)
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                return
            self.tail.next = new_node
            self.tail = new_node


if __name__ == "__main__":
    solve()
