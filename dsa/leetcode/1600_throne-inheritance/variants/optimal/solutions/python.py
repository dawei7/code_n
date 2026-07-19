from collections import defaultdict


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = kingName
        self.children = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.children[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> list[str]:
        order = []
        stack = [self.king]
        while stack:
            person = stack.pop()
            if person not in self.dead:
                order.append(person)
            stack.extend(reversed(self.children[person]))
        return order


def solve(kingName: str, operations: list[list]) -> list:
    inheritance = ThroneInheritance(kingName)
    output = []
    for name, arguments in operations:
        if name == "birth":
            inheritance.birth(*arguments)
            output.append(None)
        elif name == "death":
            inheritance.death(*arguments)
            output.append(None)
        else:
            output.append(inheritance.getInheritanceOrder())
    return output
