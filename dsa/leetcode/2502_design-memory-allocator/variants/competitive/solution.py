class Allocator:
    def __init__(self, n: int):
        self.memory = [0] * n

    def allocate(self, size: int, mID: int) -> int:
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

    def freeMemory(self, mID: int) -> int:
        released = 0
        for index, owner in enumerate(self.memory):
            if owner == mID:
                self.memory[index] = 0
                released += 1
        return released
