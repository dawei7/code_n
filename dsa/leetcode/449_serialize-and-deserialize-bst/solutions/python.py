"""Optimal app-local round-trip codec for LeetCode 449."""

from collections import deque


def solve(root: list) -> list:
    def from_level(values):
        if not values:
            return None
        nodes = [None if value is None else {"value": value, "left": None, "right": None} for value in values]
        child = 1
        for node in nodes:
            if node is None:
                continue
            if child < len(nodes):
                node["left"] = nodes[child]
                child += 1
            if child < len(nodes):
                node["right"] = nodes[child]
                child += 1
        return nodes[0]

    def serialize(node) -> str:
        values: list[str] = []

        def preorder(current) -> None:
            if current is None:
                return
            values.append(str(current["value"]))
            preorder(current["left"])
            preorder(current["right"])

        preorder(node)
        return " ".join(values)

    def deserialize(data: str):
        values = [int(token) for token in data.split()]
        index = 0

        def build(lower: float, upper: float):
            nonlocal index
            if index == len(values) or not lower < values[index] < upper:
                return None
            value = values[index]
            index += 1
            node = {"value": value, "left": None, "right": None}
            node["left"] = build(lower, value)
            node["right"] = build(value, upper)
            return node

        return build(float("-inf"), float("inf"))

    def to_level(node) -> list:
        if node is None:
            return []
        values = []
        queue = deque([node])
        while queue:
            current = queue.popleft()
            if current is None:
                values.append(None)
            else:
                values.append(current["value"])
                queue.append(current["left"])
                queue.append(current["right"])
        while values and values[-1] is None:
            values.pop()
        return values

    return to_level(deserialize(serialize(from_level(root))))
