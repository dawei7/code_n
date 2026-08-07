from collections import deque
from threading import Lock, Semaphore


class BoundedBlockingQueue(object):
    def __init__(self, capacity: int):
        self.queue = deque()
        self.slots = Semaphore(capacity)
        self.items = Semaphore(0)
        self.lock = Lock()

    def enqueue(self, element: int) -> None:
        self.slots.acquire()
        with self.lock:
            self.queue.appendleft(element)
        self.items.release()

    def dequeue(self) -> int:
        self.items.acquire()
        with self.lock:
            element = self.queue.pop()
        self.slots.release()
        return element

    def size(self) -> int:
        with self.lock:
            return len(self.queue)
