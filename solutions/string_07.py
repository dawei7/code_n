"""
Description
-----------
Find the first index where pattern occurs in text using
the Z-algorithm. Builds the Z-array over (pattern + '$' + text)
in linear time, then scans for positions where Z[i] == len(pattern).
Requirement: O(n + m) — strictly linear.
Source: https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

Examples
--------
Example 1:
Input:  text = 'hello', pattern = 'll'
Output: 2

Example 2:
Input:  text = 'aaaa', pattern = 'aa'
Output: 0

Example 3:
Input:  text = 'abcde', pattern = 'xyz'
Output: -1
"""

def solve(text, pattern):
    # Write your code here.
    return None
