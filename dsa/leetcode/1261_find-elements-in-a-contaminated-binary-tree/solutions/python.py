from typing import Any, List


class FindElements:
    def __init__(self, root: Any) -> None:
        self.values: set[int] = set()
        root.val = 0
        stack = [root]
        while stack:
            node = stack.pop()
            self.values.add(node.val)
            if node.left is not None:
                node.left.val = 2 * node.val + 1
                stack.append(node.left)
            if node.right is not None:
                node.right.val = 2 * node.val + 2
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return target in self.values


def solve(root: Any, queries: List[int]) -> List[bool]:
    recovered = FindElements(root)
    return [recovered.find(target) for target in queries]
