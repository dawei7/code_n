"""Solution for dp_24: Palindromic Partitioning (Min Cuts).

Return the minimum number of cuts to partition s into
palindromes. Precompute is_pal[i][j] (whether s[i..j] is a
palindrome) in O(n^2), then dp[i] = min over j with
is_pal[i][j] of (0 if j == n-1 else 1 + dp[j+1]).
Source: https://www.geeksforgeeks.org/palindromic-partitioning-dp-17/

Inputs passed to solve():
    s: string of n lower-case characters (capped at 10 in the setup).
    n: length of s.

Goal:
    the minimum number of cuts to partition s into palindromes.

Samples:
Sample 1 input:  s = "ababbbabbababa", n = 13
Sample 1 output: 3 (a|babbbab|b|ababa)

Sample 2 input:  s = "aab", n = 3
Sample 2 output: 1 (aa|b)


"""

def solve(s, n):
    # Write your code here.
    return None
