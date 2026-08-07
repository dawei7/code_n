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
