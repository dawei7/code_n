"""Solution for stack_06: Trapping Rain Water.


            Given a non-negative integer array heights where each
            element represents a bar of width 1, compute how much
            rainwater can be trapped between the bars after it
            rains. A classic stack-based solution: walk through
            the bars; whenever you see a bar taller than the
            stack's top, pop until the stack is empty or the
            new bar is shorter than the top. The trapped water
            at each pop is bounded by the popped bar's height,
            the current bar, and the new stack top. O(n) time,
            O(n) extra space.
            Source: https://www.geeksforgeeks.org/trapping-rain-water/
            

Inputs passed to solve():
    heights: list of n non-negative integers (bar heights).
    n: length of heights.

Goal:
    the total units of trapped rainwater.

Samples:
Sample 1 input:  heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], n = 12
Sample 1 output: 6

Sample 2 input:  heights = [4, 2, 0, 3, 2, 5], n = 6
Sample 2 output: 9


"""

def solve(heights, n):
    # Write your code here.
    return None
