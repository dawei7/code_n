class Allocator:
    def __init__(self, n):
        self.memory = [0] * n

    def allocate(self, size, mID):
        free = 0
        for index, owner in enumerate(self.memory):
            if owner == 0:
                free += 1
                if free == size:
                    start = index - size + 1
                    self.memory[start : index + 1] = [mID] * size
                    return start
            else:
                free = 0
        return -1

    def freeMemory(self, mID):
        released = 0
        for index, owner in enumerate(self.memory):
            if owner == mID:
                self.memory[index] = 0
                released += 1
        return released


def solve(commands, inputs):
    allocator = None
    results = []
    for command, arguments in zip(commands, inputs):
        if command == "Allocator":
            allocator = Allocator(arguments[0])
            results.append(None)
        elif command == "allocate":
            results.append(allocator.allocate(arguments[0], arguments[1]))
        else:
            results.append(allocator.freeMemory(arguments[0]))
    return results
