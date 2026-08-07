class MinStack:
    def __init__(self):
        self.values = []

    def push(self, val: int) -> None:
        minimum = val if not self.values else min(val, self.values[-1][1])
        self.values.append((val, minimum))

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
        return self.values[-1][0]

    def getMin(self) -> int:
        return self.values[-1][1]
