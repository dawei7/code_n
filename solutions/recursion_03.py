"""Solution for recursion_03: Print Subsequences.

Return every subsequence of s as a list of strings (the
empty string included). The recursion branches on
include/exclude at every position. Sorted so the verify
can do a plain equality check.
Requirement: O(2^n) time.
Source: https://www.geeksforgeeks.org/subsequence-substring-string/

Inputs passed to solve():
    s: string of n lower-case characters (capped at 6 in the setup).
    n: length of s.

Goal:
    a list of 2^n subsequences, sorted.

Samples:
Sample 1 input:  s = "abc", n = 3
Sample 1 output: ["", "a", "ab", "abc", "ac", "b", "bc", "c"]

Sample 2 input:  s = "ab", n = 2
Sample 2 output: ["", "a", "ab", "b"]


"""

def solve(s, n):
    # Write your code here.
    return None
