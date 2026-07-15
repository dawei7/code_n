"""Synchronization reference for LeetCode 1116 (not app-runnable)."""

from threading import Semaphore


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self._zero_turn = Semaphore(1)
        self._odd_turn = Semaphore(0)
        self._even_turn = Semaphore(0)

    def zero(self, printNumber):
        for value in range(1, self.n + 1):
            self._zero_turn.acquire()
            printNumber(0)
            (self._odd_turn if value % 2 else self._even_turn).release()

    def even(self, printNumber):
        for value in range(2, self.n + 1, 2):
            self._even_turn.acquire()
            printNumber(value)
            self._zero_turn.release()

    def odd(self, printNumber):
        for value in range(1, self.n + 1, 2):
            self._odd_turn.acquire()
            printNumber(value)
            self._zero_turn.release()
