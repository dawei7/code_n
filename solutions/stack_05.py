"""Solution for stack_05: Min Stack.

Implement a stack that supports push, pop, and get_min
in O(1). Two parallel stacks: the main one and a stack
of running minimums. Return a list of results: for each
get_min, the current min; for each pop, the popped value.
Source: https://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/

Inputs passed to solve():
    ops: list of (cmd, value) tuples; cmd in {push, pop, get_min}.
    n: length of ops.

Goal:
    a list of results - one per pop or get_min op.

Samples:
Sample 1 input:  ops = [("push", 2), ("push", 0), ("get_min", 0), ("pop", 0), ("get_min", 0)], n = 5
Sample 1 output: [0, 2, 2]


"""

def solve(ops, n):
    # Write your code here.
    return None
