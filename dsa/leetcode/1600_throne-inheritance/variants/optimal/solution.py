from collections import defaultdict
from typing import List


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        order = []
        stack = [self.king]
        while stack:
            person = stack.pop()
            if person not in self.dead:
                order.append(person)
            stack.extend(reversed(self.children[person]))
        return order
