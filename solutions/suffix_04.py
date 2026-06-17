"""Solution for suffix_04: Count Distinct Substrings.


            Count the number of distinct non-empty substrings
            of a string s. A substring starting at index i has
            length in [1, n-i]. Equivalently, the number of
            distinct substrings equals the sum over all suffixes
            of (length of suffix - LCP with the previous suffix
            in the suffix array). Build the suffix array and
            LCP array; return the sum of (n - sa[i] - lcp[i])
            for i in [0, n-1]. O(n) after the suffix array and
            LCP are built.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-application-count-distinct-substrings/
            

Inputs passed to solve():
    s: the input string.
    n: length of s.

Goal:
    the number of distinct non-empty substrings of s, as an int.

Samples:
Sample 1 input:  s = 'banana', n = 6
Sample 1 output: 15 (the 15 distinct substrings of 'banana')

Sample 2 input:  s = 'aaa', n = 3
Sample 2 output: 3 ('a', 'aa', 'aaa')

Sample 3 input:  s = 'abcd', n = 4
Sample 3 output: 10 (each substring is unique)

"""

def solve(s, n):
    # Write your code here.
    return None
