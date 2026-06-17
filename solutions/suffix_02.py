"""Solution for suffix_02: Pattern Search with Suffix Array.

Search for ``pattern`` in ``s`` using a suffix array.
Build the SA, then binary-search for the range of
suffixes that start with pattern. The pattern occurs
at every index in that range.
Source: https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/

Inputs passed to solve():
    s: string to search in.
    n: length of s.
    pattern: the pattern to find.
    m: length of pattern.

Goal:
    a sorted list of starting indices in s where pattern occurs.

Samples:
Sample 1 input:  s = 'banana', n = 6, pattern = 'ana', m = 3
Sample 1 output: [1, 3]


"""

def solve(s, n, pattern, m):
    # Write your code here.
    return None
