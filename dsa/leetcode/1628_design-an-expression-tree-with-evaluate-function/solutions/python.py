from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        raise NotImplementedError


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
        magnitude = abs(left_value) // abs(right_value)
        return -magnitude if (left_value < 0) != (right_value < 0) else magnitude


class TreeBuilder:
    def buildTree(self, postfix: list[str]) -> Node:
        stack: list[ExpressionNode] = []
        for token in postfix:
            if token in {"+", "-", "*", "/"}:
                right = stack.pop()
                left = stack.pop()
                stack.append(ExpressionNode(token, left, right))
            else:
                stack.append(ExpressionNode(token))
        return stack[-1]


def solve(postfix: list[str]) -> int:
    return TreeBuilder().buildTree(postfix).evaluate()
