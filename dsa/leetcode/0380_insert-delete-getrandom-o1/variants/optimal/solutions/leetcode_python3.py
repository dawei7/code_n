from random import choice


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False

        remove_index = self.indices[val]
        final_value = self.values[-1]
        self.values[remove_index] = final_value
        self.indices[final_value] = remove_index
        self.values.pop()
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.values)

