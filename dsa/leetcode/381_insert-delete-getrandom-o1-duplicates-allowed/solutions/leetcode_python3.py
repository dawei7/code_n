from collections import defaultdict
from random import choice


class RandomizedCollection:

    def __init__(self):
        self.values = []
        self.indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        is_new = not self.indices[val]
        self.indices[val].add(len(self.values))
        self.values.append(val)
        return is_new

    def remove(self, val: int) -> bool:
        if not self.indices.get(val):
            return False

        remove_index = self.indices[val].pop()
        final_index = len(self.values) - 1
        final_value = self.values[final_index]
        if remove_index != final_index:
            self.values[remove_index] = final_value
            self.indices[final_value].add(remove_index)
            self.indices[final_value].discard(final_index)
        self.values.pop()
        if not self.indices[val]:
            del self.indices[val]
        return True

    def getRandom(self) -> int:
        return choice(self.values)

