"""Optimal app-local solution for LeetCode 895."""

from collections import defaultdict


class FreqStack:
    def __init__(self):
        self.frequency = defaultdict(int)
        self.groups = defaultdict(list)
        self.max_frequency = 0

    def push(self, val):
        frequency = self.frequency[val] + 1
        self.frequency[val] = frequency
        self.groups[frequency].append(val)
        self.max_frequency = max(self.max_frequency, frequency)

    def pop(self):
        val = self.groups[self.max_frequency].pop()
        self.frequency[val] -= 1
        if not self.groups[self.max_frequency]:
            self.max_frequency -= 1
        return val


def solve(operations):
    stack = FreqStack()
    output = []
    for operation in operations:
        if operation[0] == "push":
            stack.push(operation[1])
            output.append(None)
        else:
            output.append(stack.pop())
    return output
