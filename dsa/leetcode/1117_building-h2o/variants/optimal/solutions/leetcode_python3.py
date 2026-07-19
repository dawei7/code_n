from threading import Barrier, Semaphore


class H2O:
    def __init__(self):
        self.hydrogen_slots = Semaphore(2)
        self.oxygen_slots = Semaphore(1)
        self.molecule = Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.hydrogen_slots.acquire()
        self.molecule.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.hydrogen_slots.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.oxygen_slots.acquire()
        self.molecule.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.oxygen_slots.release()
