from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass


class ExpressionNode(Node):
    def __init__(
        self,
        value: str,
        left: "ExpressionNode | None" = None,
        right: "ExpressionNode | None" = None,
    ):
        self.value = value
        self.left = left
        self.right = right

    def evaluate(self) -> int:
        if self.left is None or self.right is None:
            return int(self.value)
        left_value = self.left.evaluate()
        right_value = self.right.evaluate()
        if self.value == "+":
            return left_value + right_value
        if self.value == "-":
            return left_value - right_value
        if self.value == "*":
            return left_value * right_value
        return int(left_value / right_value)


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> "Node":
        stack = []
        for token in postfix:
            if token in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()
                stack.append(ExpressionNode(token, left, right))
            else:
                stack.append(ExpressionNode(token))
        return stack[-1]
