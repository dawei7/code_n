"""Solution for suffix_05: Longest Repeated Substring.


            Find the length of the longest substring of s
            that occurs at least twice (in two different
            positions, with non-overlapping allowed). Build
            the suffix array and the LCP array; the answer is
            the maximum value in the LCP array. Return 0 if
            no substring repeats. O(n) after the suffix and
            LCP arrays are built.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-1-introduction/
            

Inputs passed to solve():
    s: the input string.
    n: length of s.

Goal:
    the length of the longest repeated substring of s (0 if none), as an int.

Samples:
Sample 1 input:  s = 'banana', n = 6
Sample 1 output: 3 ('ana' or 'nan' appears twice)

Sample 2 input:  s = 'abcd', n = 4
Sample 2 output: 0 (all substrings unique)

Sample 3 input:  s = 'aaaa', n = 4
Sample 3 output: 3 ('aaa' appears at positions 0, 1)

"""

def solve(s, n):
    # Write your code here.
    return None
