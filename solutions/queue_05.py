"""Solution for queue_05: Circular Queue (Array-based).


            Implement a fixed-capacity circular queue using
            an array. Maintain front, rear, and size. Enqueue
            writes at (rear + 1) % capacity and increments size;
            dequeue reads at front and advances front by 1 mod
            capacity. Return False (not raise) on overflow /
            underflow so the verifier can check the result
            directly. Operations are O(1).
            Source: https://www.geeksforgeeks.org/circular-queue-set-1-introduction-array-implementation/
            

Inputs passed to solve():
    operations: list of operation tuples (op_name, *args).
    capacity: fixed capacity of the circular queue.
    n: number of operations.

Goal:
    a list of dequeued values (in order) for each successful dequeue.

Samples:
Sample 1 input:  ops = [('enqueue', 1), ('enqueue', 2), ('dequeue'), ('enqueue', 3), ('dequeue')], capacity = 3, n = 5
Sample 1 output: [1, 2]


"""

def solve(operations, capacity, n):
    # Write your code here.
    return None
