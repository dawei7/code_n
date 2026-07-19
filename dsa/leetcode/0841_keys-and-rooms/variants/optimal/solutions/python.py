"""Optimal app-local solution for LeetCode 841."""


def solve(rooms):
    seen = {0}
    stack = [0]

    while stack:
        room = stack.pop()
        for key in rooms[room]:
            if key not in seen:
                seen.add(key)
                stack.append(key)

    return len(seen) == len(rooms)
