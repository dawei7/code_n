"""Solution for dp_20: Shortest Common Supersequence (Length).

The shortest string that has both s1 and s2 as subsequences.
Length is n1 + n2 - LCS(s1, s2). Compute the LCS length via
the standard DP table.
Source: https://www.geeksforgeeks.org/shortest-common-supersequence/

Inputs passed to solve():
    s1: first string (capped at 6 in the setup).
    s2: second string (capped at 6 in the setup).
    n1: length of s1.
    n2: length of s2.

Goal:
    the length of the shortest common supersequence.

Samples:
Sample 1 input:  s1 = "abac", s2 = "cab", n1 = 4, n2 = 3
Sample 1 output: 5 (cabac)

Sample 2 input:  s1 = "abc", s2 = "abc", n1 = 3, n2 = 3
Sample 2 output: 3


"""

def solve(s1, s2, n1, n2):
    # Write your code here.
    return None
