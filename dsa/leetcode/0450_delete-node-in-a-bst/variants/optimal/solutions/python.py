"""Optimal app-local BST deletion for LeetCode 450."""

from collections import deque


def solve(root: list, key: int) -> list:
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

    def delete(node, target):
        if node is None:
            return None
        if target < node["value"]:
            node["left"] = delete(node["left"], target)
        elif target > node["value"]:
            node["right"] = delete(node["right"], target)
        else:
            if node["left"] is None:
                return node["right"]
            if node["right"] is None:
                return node["left"]
            successor = node["right"]
            while successor["left"] is not None:
                successor = successor["left"]
            node["value"] = successor["value"]
            node["right"] = delete(node["right"], successor["value"])
        return node

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

    return to_level(delete(from_level(root), key))
