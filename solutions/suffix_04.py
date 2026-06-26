"""
Description
-----------
Count the number of distinct non-empty substrings
            of a string s. A substring starting at index i has
            length in [1, n-i]. Equivalently, the number of
            distinct substrings equals the sum over all suffixes
            of (length of suffix - LCP with the previous suffix
            in the suffix array). Build the suffix array and
            LCP array; return the sum of (n - sa[i] - lcp[i])
            for i in [0, n-1]. O(n) after the suffix array and
            LCP are built.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-application-count-distinct-substrings/

Examples
--------
Example 1:
Input:  s = 'banana', n = 6
Output: 15 (the 15 distinct substrings of 'banana')

Example 2:
Input:  s = 'aaa', n = 3
Output: 3 ('a', 'aa', 'aaa')

Example 3:
Input:  s = 'abcd', n = 4
Output: 10 (each substring is unique)
"""

def solve(s, n):
    # Write your code here.
    return None
