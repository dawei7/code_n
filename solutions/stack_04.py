"""Solution for stack_04: Largest Rectangle in Histogram.

Given an array of bar heights, return the area of the
largest rectangle that fits entirely within the bars.
Monotonic stack of indices with increasing heights; for
each bar popped, the rectangle's width is the run of
indices with height >= that bar.
Source: https://www.geeksforgeeks.org/largest-rectangular-area-in-a-histogram-using-stack/

Inputs passed to solve():
    heights: list of n bar heights.
    n: length of heights.

Goal:
    the largest rectangle area.

Samples:
Sample 1 input:  heights = [2, 1, 5, 6, 2, 3], n = 6
Sample 1 output: 10 (5 * 2)

Sample 2 input:  heights = [2, 4], n = 2
Sample 2 output: 4


"""

def solve(heights, n):
    # Write your code here.
    return None
