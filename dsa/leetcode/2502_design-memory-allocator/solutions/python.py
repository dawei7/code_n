class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n
        self.size = n

    def allocate(self, size: int, mID: int) -> int:
        count = 0
        for i in range(self.size):
            if self.memory[i] == 0:
                count += 1
                if count == size:
                    start_index = i - size + 1
                    for j in range(start_index, i + 1):
                        self.memory[j] = mID
                    return start_index
            else:
                count = 0
        return -1

    def freeMemory(self, mID: int) -> int:
        freed_count = 0
        for i in range(self.size):
            if self.memory[i] == mID:
                self.memory[i] = 0
                freed_count += 1
        return freed_count

def solve(commands, inputs):
    results = []
    allocator = None
    for cmd, args in zip(commands, inputs):
        if cmd == "Allocator":
            allocator = Allocator(args[0])
            results.append(None)
        elif cmd == "allocate":
            results.append(allocator.allocate(args[0], args[1]))
        elif cmd in {"freeMemory", "free"}:
            results.append(allocator.freeMemory(args[0]))
    return results
