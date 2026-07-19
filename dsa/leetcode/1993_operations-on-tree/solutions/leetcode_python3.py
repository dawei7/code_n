from typing import List


class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        self.children = [[] for _ in parent]
        for node in range(1, len(parent)):
            self.children[parent[node]].append(node)
        self.locked_by = [0] * len(parent)

    def lock(self, num: int, user: int) -> bool:
        if self.locked_by[num] != 0:
            return False
        self.locked_by[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if self.locked_by[num] != user:
            return False
        self.locked_by[num] = 0
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if self.locked_by[num] != 0:
            return False

        ancestor = self.parent[num]
        while ancestor != -1:
            if self.locked_by[ancestor] != 0:
                return False
            ancestor = self.parent[ancestor]

        found_locked_descendant = False
        stack = list(self.children[num])
        while stack:
            node = stack.pop()
            if self.locked_by[node] != 0:
                found_locked_descendant = True
                self.locked_by[node] = 0
            stack.extend(self.children[node])

        if not found_locked_descendant:
            return False
        self.locked_by[num] = user
        return True
