"""
Description
-----------
Implement a LIFO stack using only FIFO queues
            (the one-queue variant). On push, enqueue the new
            element, then rotate the queue: dequeue and re-enqueue
            the existing elements one by one. This puts the new
            element at the FRONT of the queue, so the next pop
            returns it. Amortized O(1) per op, O(n) for the single
            rotation on each push.
            Source: https://www.geeksforgeeks.org/stack-using-two-queues/

Examples
--------
Example 1:
Input:  ops = [('push', 1), ('push', 2), ('top'), ('pop'), ('top')], n = 5
Output: [2, 1]
"""

def solve(operations, n):
    # Write your code here.
    return None
