"""
Description
-----------
Return the length of the longest subsequence of s that is
also a palindrome. Standard interval DP: dp[i][j] = LPS
length in s[i..j]. dp[i][i] = 1. If s[i] == s[j],
dp[i][j] = dp[i+1][j-1] + 2; else dp[i][j] = max(
dp[i+1][j], dp[i][j-1]). O(n^2) time and space.
Source: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/

Examples
--------
Example 1:
Input:  s = "bbbab", n = 5
Output: 4 (bbbb)

Example 2:
Input:  s = "cbbd", n = 4
Output: 2 (bb)
"""

def solve(s, n):
    # Write your code here.
    return None
