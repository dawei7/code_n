"""
Description
-----------
Implement a FIFO queue using only two LIFO stacks.
            The trick: use one stack for enqueue (push) and
            another for dequeue (peek). When the dequeue stack
            is empty, transfer everything from the enqueue
            stack into it (reversing the order). Amortized
            O(1) per operation. The returned object supports
            push, pop, peek, and empty (with the same
            semantics as collections.deque).
            Source: https://www.geeksforgeeks.org/queue-using-stacks/

Examples
--------
Example 1:
Input:  ops = [('push', 1), ('push', 2), ('peek'), ('pop'), ('peek')], n = 5
Output: [1, 2]

Example 2:
Input:  ops = [('push', 5), ('pop'), ('pop')], n = 3
Output: [] (pop on empty doesn't crash)
"""

def solve(operations, n):
    # Write your code here.
    return None
