"""Solution for suffix_03: LCP Array (Kasai's Algorithm).


            Given a string s, return its suffix array sa and
            the LCP (Longest Common Prefix) array. LCP[i] is
            the length of the longest common prefix of the
            suffixes s[sa[i]:] and s[sa[i-1]:]. Use Kasai's
            linear-time algorithm: walk the original string in
            order, and for each position i, walk forward from
            the previous LCP to compute the LCP of the current
            suffix and its neighbor in the suffix array.
            O(n) time after O(n log n) for the suffix array.
            Source: https://www.geeksforgeeks.org/dsa/suffix-array-set-2-a-kasai-algorithm-for-construction-of-lcp-array/
            

Inputs passed to solve():
    s: the input string.
    n: length of s.

Goal:
    a tuple (sa, lcp) where sa is the suffix array of s and lcp is the LCP array of length n (lcp[0] = 0).

Samples:
Sample 1 input:  s = 'banana', n = 6
Sample 1 output: ([5, 3, 1, 0, 4, 2], [0, 0, 3, 1, 0, 2])

Sample 2 input:  s = 'aaaa', n = 4
Sample 2 output: ([3, 2, 1, 0], [0, 1, 2, 3])


"""

def solve(s, n):
    # Write your code here.
    return None
