"""Synchronization reference for LeetCode 1114 (not app-runnable)."""

from threading import Event


class Foo:
    def __init__(self):
        self._first_done = Event()
        self._second_done = Event()

    def first(self, printFirst):
        printFirst()
        self._first_done.set()

    def second(self, printSecond):
        self._first_done.wait()
        printSecond()
        self._second_done.set()

    def third(self, printThird):
        self._second_done.wait()
        printThird()
