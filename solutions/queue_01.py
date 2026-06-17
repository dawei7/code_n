"""Solution for queue_01: Implement Queue using Stacks.


            Implement a FIFO queue using only two LIFO stacks.
            The trick: use one stack for enqueue (push) and
            another for dequeue (peek). When the dequeue stack
            is empty, transfer everything from the enqueue
            stack into it (reversing the order). Amortized
            O(1) per operation. The returned object supports
            push, pop, peek, and empty (with the same
            semantics as collections.deque).
            Source: https://www.geeksforgeeks.org/queue-using-stacks/
            

Inputs passed to solve():
    operations: list of operation tuples, each (op_name, *args).
    n: number of operations.

Goal:
    a list of results (the outputs of peek/pop in order, or []).

Samples:
Sample 1 input:  ops = [('push', 1), ('push', 2), ('peek'), ('pop'), ('peek')], n = 5
Sample 1 output: [1, 2]

Sample 2 input:  ops = [('push', 5), ('pop'), ('pop')], n = 3
Sample 2 output: [] (pop on empty doesn't crash)


"""

def solve(operations, n):
    # Write your code here.
    return None
