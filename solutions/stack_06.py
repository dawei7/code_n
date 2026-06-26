"""
Description
-----------
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

Examples
--------
Example 1:
Input:  heights = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], n = 12
Output: 6

Example 2:
Input:  heights = [4, 2, 0, 3, 2, 5], n = 6
Output: 9
"""

def solve(heights, n):
    # Write your code here.
    return None
