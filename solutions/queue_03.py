"""Solution for queue_03: Generate Binary Numbers (1 to n).


            Generate the binary representations of 1, 2, ..., n
            in order, using a queue. Start with the queue
            containing '1'. Each iteration: dequeue the front
            string s, append s + '0' and s + '1' to the back.
            This generates the binary strings in BFS order,
            which matches the natural numerical order for
            positive integers. O(n) overall.
            Source: https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/
            

Inputs passed to solve():
    n: positive integer.

Goal:
    a list of n binary strings (the binary representations of 1..n).

Samples:
Sample 1 input:  n = 5
Sample 1 output: ['1', '10', '11', '100', '101']

Sample 2 input:  n = 1
Sample 2 output: ['1']


"""

def solve(n):
    # Write your code here.
    return None
