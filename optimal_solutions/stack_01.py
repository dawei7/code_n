"""Optimal solution for stack_01: Balanced Parentheses.

Walk the string; push each opening bracket, and on a closing
bracket pop the top and check that it pairs correctly. Return
True iff the stack is empty at the end. O(n).
"""


def solve(s, n):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
