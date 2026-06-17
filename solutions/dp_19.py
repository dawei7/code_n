"""Solution for dp_19: Longest Palindromic Subsequence.

Return the length of the longest subsequence of s that is
also a palindrome. Standard interval DP: dp[i][j] = LPS
length in s[i..j]. dp[i][i] = 1. If s[i] == s[j],
dp[i][j] = dp[i+1][j-1] + 2; else dp[i][j] = max(
dp[i+1][j], dp[i][j-1]). O(n^2) time and space.
Source: https://www.geeksforgeeks.org/longest-palindromic-subsequence-dp-12/

Inputs passed to solve():
    s: string of n lower-case characters (capped at 10 in the setup).
    n: length of s.

Goal:
    the length of the longest palindromic subsequence.

Samples:
Sample 1 input:  s = "bbbab", n = 5
Sample 1 output: 4 (bbbb)

Sample 2 input:  s = "cbbd", n = 4
Sample 2 output: 2 (bb)


"""

def solve(s, n):
    # Write your code here.
    return None
