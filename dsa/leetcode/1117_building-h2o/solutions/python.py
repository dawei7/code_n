"""Source-native synchronization reference for LeetCode 1117."""

from threading import Barrier, Semaphore


class H2O:
    def __init__(self):
        self._hydrogen_slots = Semaphore(2)
        self._oxygen_slots = Semaphore(1)
        self._molecule = Barrier(3)

    def hydrogen(self, releaseHydrogen):
        self._hydrogen_slots.acquire()
        self._molecule.wait()
        releaseHydrogen()
        self._hydrogen_slots.release()

    def oxygen(self, releaseOxygen):
        self._oxygen_slots.acquire()
        self._molecule.wait()
        releaseOxygen()
        self._oxygen_slots.release()
