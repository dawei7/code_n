"""Source-native synchronization reference for LeetCode 1115."""

from threading import Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self._foo_turn = Semaphore(1)
        self._bar_turn = Semaphore(0)

    def foo(self, printFoo):
        for _ in range(self.n):
            self._foo_turn.acquire()
            printFoo()
            self._bar_turn.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self._bar_turn.acquire()
            printBar()
            self._foo_turn.release()
