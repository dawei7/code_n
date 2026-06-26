"""
Description
-----------
For each day i, the span is the number of consecutive days
ending at i with a price <= arr[i] (including today).
Monotonic stack of strictly-greater indices: pop while
arr[top] <= arr[i]; the span is i - top_index, or i + 1
if the stack is empty.
Source: https://www.geeksforgeeks.org/the-stock-span-problem/

Examples
--------
Example 1:
Input:  arr = [100, 80, 60, 70, 60, 75, 85], n = 7
Output: [1, 1, 1, 2, 1, 4, 6]

Example 2:
Input:  arr = [10, 4, 5, 90, 120, 80], n = 6
Output: [1, 1, 2, 4, 5, 1]
"""

def solve(arr, n):
    # Write your code here.
    return None
