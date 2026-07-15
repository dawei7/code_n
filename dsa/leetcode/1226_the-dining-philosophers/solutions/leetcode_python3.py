from threading import Lock
from typing import Callable


class DiningPhilosophers:
    def __init__(self):
        self.transaction = Lock()

    def wantsToEat(
        self,
        philosopher: int,
        pickLeftFork: 'Callable[[], None]',
        pickRightFork: 'Callable[[], None]',
        eat: 'Callable[[], None]',
        putLeftFork: 'Callable[[], None]',
        putRightFork: 'Callable[[], None]',
    ) -> None:
        with self.transaction:
            pickLeftFork()
            pickRightFork()
            eat()
            putRightFork()
            putLeftFork()
