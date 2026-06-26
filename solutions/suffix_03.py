"""
Description
-----------
Given a string s, return its suffix array sa and
            the LCP (Longest Common Prefix) array. LCP[i] is
            the length of the longest common prefix of the
            suffixes s[sa[i]:] and s[sa[i-1]:]. Use Kasai's
            linear-time algorithm: walk the original string in
            order, and for each position i, walk forward from
            the previous LCP to compute the LCP of the current
            suffix and its neighbor in the suffix array.
            O(n) time after O(n log n) for the suffix array.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-kasai-algorithm-for-construction-of-lcp-array/

Examples
--------
Example 1:
Input:  s = 'banana', n = 6
Output: ([5, 3, 1, 0, 4, 2], [0, 0, 3, 1, 0, 2])

Example 2:
Input:  s = 'aaaa', n = 4
Output: ([3, 2, 1, 0], [0, 1, 2, 3])
"""

def solve(s, n):
    # Write your code here.
    return None
