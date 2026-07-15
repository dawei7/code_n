from threading import Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_turn = Semaphore(1)
        self.bar_turn = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.foo_turn.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_turn.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for _ in range(self.n):
            self.bar_turn.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_turn.release()
