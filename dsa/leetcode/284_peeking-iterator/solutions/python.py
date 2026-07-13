class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.has_next = iterator.hasNext()
        self.cached = iterator.next() if self.has_next else None

    def peek(self):
        return self.cached

    def next(self):
        value = self.cached
        self.has_next = self.iterator.hasNext()
        self.cached = self.iterator.next() if self.has_next else None
        return value

    def hasNext(self):
        return self.has_next


def solve(iterator_data: list[int], operations: list[str]) -> list[object]:
    class Iterator:
        def __init__(self, values):
            self.values = values
            self.index = 0

        def next(self):
            value = self.values[self.index]
            self.index += 1
            return value

        def hasNext(self):
            return self.index < len(self.values)

    iterator = PeekingIterator(Iterator(iterator_data))
    output = []
    for operation in operations:
        if operation == "peek":
            output.append(iterator.peek())
        elif operation == "next":
            output.append(iterator.next())
        else:
            output.append(iterator.hasNext())
    return output
