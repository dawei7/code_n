"""
Description
-----------
Return the minimum number of cuts to partition s into
palindromes. Precompute is_pal[i][j] (whether s[i..j] is a
palindrome) in O(n^2), then dp[i] = min over j with
is_pal[i][j] of (0 if j == n-1 else 1 + dp[j+1]).
Source: https://www.geeksforgeeks.org/palindromic-partitioning-dp-17/

Examples
--------
Example 1:
Input:  s = "ababbbabbababa", n = 13
Output: 3 (a|babbbab|b|ababa)

Example 2:
Input:  s = "aab", n = 3
Output: 1 (aa|b)
"""

def solve(s, n):
    # Write your code here.
    return None
