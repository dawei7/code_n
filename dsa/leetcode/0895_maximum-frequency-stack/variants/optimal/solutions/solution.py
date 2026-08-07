from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.groups = defaultdict(list)
        self.max_frequency = 0

    def push(self, val: int) -> None:
        frequency = self.frequency[val] + 1
        self.frequency[val] = frequency
        self.groups[frequency].append(val)
        self.max_frequency = max(self.max_frequency, frequency)

    def pop(self) -> int:
        val = self.groups[self.max_frequency].pop()
        self.frequency[val] -= 1
        if not self.groups[self.max_frequency]:
            self.max_frequency -= 1
        return val
