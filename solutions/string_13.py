"""
Description
-----------
Find every position in s where pattern occurs, using the
Z-algorithm. Build the Z-array of pattern + '$' + s;
Z[i] is the longest prefix of the combined string that
starts at position i. Z[i] == |pattern| in the s region
iff pattern matches there. O(n + m) total.
Source: https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

Examples
--------
Example 1:
Input:  s = 'aabxaayaab', n = 10, pattern = 'aab', m = 3
Output: [0, 6]

Example 2:
Input:  s = 'aaaa', n = 4, pattern = 'aa', m = 2
Output: [0, 1, 2]
"""

def solve(s, n, pattern, m):
    # Write your code here.
    return None
