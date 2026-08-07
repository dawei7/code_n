class CustomStack:
    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.values = []
        self.increments = []

    def push(self, x: int) -> None:
        if len(self.values) < self.max_size:
            self.values.append(x)
            self.increments.append(0)

    def pop(self) -> int:
        if not self.values:
            return -1

        index = len(self.values) - 1
        increment = self.increments.pop()
        if index > 0:
            self.increments[index - 1] += increment
        return self.values.pop() + increment

    def increment(self, k: int, val: int) -> None:
        if self.values:
            index = min(k, len(self.values)) - 1
            self.increments[index] += val
