from typing import List


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.stack = [iter(nestedList)]
        self.cached = None
        self.ready = False

    def next(self) -> int:
        if not self.hasNext():
            raise StopIteration
        value = self.cached
        self.cached = None
        self.ready = False
        return value

    def hasNext(self) -> bool:
        if self.ready:
            return True

        while self.stack:
            try:
                value = next(self.stack[-1])
            except StopIteration:
                self.stack.pop()
                continue

            if value.isInteger():
                self.cached = value.getInteger()
                self.ready = True
                return True
            self.stack.append(iter(value.getList()))

        return False
