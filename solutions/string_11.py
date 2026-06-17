"""Solution for string_11: Longest Common Substring.

Length of the longest common substring (consecutive, not
subsequence) of s1 and s2. Standard DP: dp[i][j] = length
of the common suffix of s1[..i] and s2[..j]. The answer
is the max over the table.
Source: https://www.geeksforgeeks.org/longest-common-substring-dp-29/

Inputs passed to solve():
    s1: first string (capped at 6 in the setup).
    s2: second string (capped at 6 in the setup).
    n1: length of s1.
    n2: length of s2.

Goal:
    the length of the longest common substring.

Samples:
Sample 1 input:  s1 = "abcdxyz", s2 = "xyzabcd", n1 = 7, n2 = 7
Sample 1 output: 4 (abcd or xyzd)

Sample 2 input:  s1 = "geeks", s2 = "geekfor", n1 = 5, n2 = 7
Sample 2 output: 4 (geek)


"""

def solve(s1, s2, n1, n2):
    # Write your code here.
    return None
