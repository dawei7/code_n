import random


class Node:
    __slots__ = ["val", "next"]

    def __init__(self, val: int, level: int):
        self.val = val
        self.next = [None] * level


class Skiplist:
    MAX_LEVEL = 16
    P = 0.5

    def __init__(self):
        self.head = Node(-1, self.MAX_LEVEL)
        self.level = 1

    def _random_level(self) -> int:
        lvl = 1
        while lvl < self.MAX_LEVEL and random.random() < self.P:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * self.MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr

        lvl = self._random_level()
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl

        new_node = Node(num, lvl)
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [self.head] * self.MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr

        target_node = curr.next[0]
        if target_node is None or target_node.val != num:
            return False

        for i in range(self.level):
            if update[i].next[i] is not target_node:
                break
            update[i].next[i] = target_node.next[i]

        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1

        return True


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)
