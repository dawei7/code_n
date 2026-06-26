"""Optimal solution for stack_05: Min Stack.

Two parallel stacks: one for values, one for the running minimum.
push, pop, top, get_min are all O(1).
"""


def solve(ops, n):
    stack = []
    mins = []
    out = []
    for op in ops:
        cmd = op[0]
        if cmd == "push":
            v = op[1]
            stack.append(v)
            if not mins or v <= mins[-1]:
                mins.append(v)
        elif cmd == "pop":
            if not stack:
                out.append(-1)
            else:
                v = stack.pop()
                if mins and v == mins[-1]:
                    mins.pop()
                out.append(v)
        elif cmd == "get_min":
            out.append(mins[-1] if mins else -1)
    return out
