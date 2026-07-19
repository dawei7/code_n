"""Optimal app-local solution for LeetCode 968."""


def solve(root):
    uncovered, camera, covered = 0, 1, 2
    states = {None: covered}
    stack = [(root, False)]
    cameras = 0

    while stack:
        node, visited = stack.pop()
        if not visited:
            stack.append((node, True))
            if node.right is not None:
                stack.append((node.right, False))
            if node.left is not None:
                stack.append((node.left, False))
            continue

        left_state = states[node.left]
        right_state = states[node.right]
        if left_state == uncovered or right_state == uncovered:
            cameras += 1
            states[node] = camera
        elif left_state == camera or right_state == camera:
            states[node] = covered
        else:
            states[node] = uncovered

    return cameras + (states[root] == uncovered)
