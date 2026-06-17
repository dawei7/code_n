"""Solution for string_13: Z-Algorithm (Pattern Search).

Find every position in s where pattern occurs, using the
Z-algorithm. Build the Z-array of pattern + '$' + s;
Z[i] is the longest prefix of the combined string that
starts at position i. Z[i] == |pattern| in the s region
iff pattern matches there. O(n + m) total.
Source: https://www.geeksforgeeks.org/z-algorithm-linear-time-pattern-searching-algorithm/

Inputs passed to solve():
    s: string to search in.
    n: length of s.
    pattern: the pattern.
    m: length of pattern.

Goal:
    a sorted list of starting indices where pattern occurs.

Samples:
Sample 1 input:  s = 'aabxaayaab', n = 10, pattern = 'aab', m = 3
Sample 1 output: [0, 6]

Sample 2 input:  s = 'aaaa', n = 4, pattern = 'aa', m = 2
Sample 2 output: [0, 1, 2]


"""

def solve(s, n, pattern, m):
    # Write your code here.
    return None
