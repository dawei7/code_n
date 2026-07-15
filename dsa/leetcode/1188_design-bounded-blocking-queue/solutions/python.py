"""Synchronization reference for LeetCode 1188 (not app-runnable)."""

from collections import deque
from threading import Lock, Semaphore


class BoundedBlockingQueue:
    def __init__(self, capacity: int):
        self._queue = deque()
        self._slots = Semaphore(capacity)
        self._items = Semaphore(0)
        self._lock = Lock()

    def enqueue(self, element: int) -> None:
        self._slots.acquire()
        with self._lock:
            self._queue.appendleft(element)
        self._items.release()

    def dequeue(self) -> int:
        self._items.acquire()
        with self._lock:
            element = self._queue.pop()
        self._slots.release()
        return element

    def size(self) -> int:
        with self._lock:
            return len(self._queue)
