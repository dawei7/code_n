class NestedIterator:
    def __init__(self, nested_list: list) -> None:
        self.stack = [iter(nested_list)]
        self.cached: int | None = None
        self.ready = False

    def next(self) -> int:
        if not self.has_next():
            raise StopIteration
        value = self.cached
        self.cached = None
        self.ready = False
        return value

    def has_next(self) -> bool:
        if self.ready:
            return True

        while self.stack:
            try:
                value = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if isinstance(value, int):
                self.cached = value
                self.ready = True
                return True
            self.stack.append(iter(value))

        return False


def solve(nested_list: list) -> list[int]:
    iterator = NestedIterator(nested_list)
    flattened: list[int] = []
    while iterator.has_next():
        flattened.append(iterator.next())
    return flattened
