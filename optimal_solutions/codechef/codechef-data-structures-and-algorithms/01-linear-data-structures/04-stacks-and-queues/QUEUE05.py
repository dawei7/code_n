


def solve():
    class CircularQueue:
        def __init__(self, max_size):
            self.max_size = max_size
            self.a = [0] * max_size
            self.front = 0
            self.rear = -1
            self.current_size = 0

        def is_empty(self):
            return self.current_size == 0

        def is_full(self):
            return self.current_size == self.max_size

        def size(self):
            return self.current_size

        def enqueue(self, item):
            if self.is_full():
                print("Queue is full. Cannot enqueue.")
                return
            self.rear = (self.rear + 1) % self.max_size  # Circular increment
            self.a[self.rear] = item
            self.current_size += 1

        def dequeue(self):
            if self.is_empty():
                print("Queue is empty. Cannot dequeue.")
                return -1  # Return a sentinel value or throw an exception
            removed_item = self.a[self.front]
            self.front = (self.front + 1) % self.max_size  # Circular increment
            self.current_size -= 1
            return removed_item


    if __name__ == "__main__":
        n = 10
        queue = CircularQueue(101)

        for i in range(1, n + 1):
            if i % 2 == 1:
                print(i, end=" ")
            else:
                queue.enqueue(i)

        while not queue.is_empty():
            print(queue.dequeue(), end=" ")


if __name__ == "__main__":
    solve()
