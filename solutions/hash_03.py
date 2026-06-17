"""Solution for hash_03: Longest Substring Without Repeating.

Return the length of the longest substring with no repeated
characters. Sliding window: keep a last-seen-position map;
when a repeat is inside the window, jump the left end past
the previous occurrence. O(n).
Source: https://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

Inputs passed to solve():
    s: string of n lower-case ASCII characters.
    n: length of s.

Goal:
    the length of the longest substring with all distinct characters.

Samples:
Sample 1 input:  s = "geeksforgeeks", n = 13
Sample 1 output: 7 (eksforg)

Sample 2 input:  s = "aaaa", n = 4
Sample 2 output: 1

Sample 3 input:  s = "abcdef", n = 6
Sample 3 output: 6

"""

def solve(s, n):
    # Write your code here.
    return None
