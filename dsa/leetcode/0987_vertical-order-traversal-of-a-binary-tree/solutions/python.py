"""Optimal app-local solution for LeetCode 987."""


def solve(root):
    coordinates = []
    stack = [(root, 0, 0)]

    while stack:
        node, row, column = stack.pop()
        coordinates.append((column, row, node.val))
        if node.left is not None:
            stack.append((node.left, row + 1, column - 1))
        if node.right is not None:
            stack.append((node.right, row + 1, column + 1))

    coordinates.sort()
    answer = []
    previous_column = None
    for column, _, value in coordinates:
        if column != previous_column:
            answer.append([])
            previous_column = column
        answer[-1].append(value)
    return answer
