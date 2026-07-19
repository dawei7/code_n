"""Optimal app-local solution for LeetCode 1522."""


def solve(tree):
    children = {value: list(child_values) for value, child_values in tree}
    child_values = {child for values in children.values() for child in values}
    root = next(value for value in children if value not in child_values)
    order = []
    stack = [root]
    while stack:
        node = stack.pop()
        order.append(node)
        stack.extend(children[node])

    height = {}
    answer = 0
    for node in reversed(order):
        longest = second = 0
        for child in children[node]:
            candidate = height[child] + 1
            if candidate > longest:
                longest, second = candidate, longest
            elif candidate > second:
                second = candidate
        answer = max(answer, longest + second)
        height[node] = longest
    return answer
