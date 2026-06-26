"""
Description
-----------
Given a stream of characters (a string), for each
            prefix of length i, return the first non-repeating
            character in that prefix, or '_' if none exists.
            Use a queue to maintain the candidate set (characters
            seen exactly once so far, in order of first
            appearance) and a frequency counter to detect
            repeats. When a character's count becomes 2, remove
            it from the queue. O(n) time, O(1) space (26 letters).
            Source: https://www.geeksforgeeks.org/first-non-repeating-character-in-a-stream/

Examples
--------
Example 1:
Input:  stream = 'aabc', n = 4
Output: 'aa_b' (a, a, _, b)

Example 2:
Input:  stream = 'aabbccd', n = 7
Output: 'aa____d' (a, a, _, _, _, _, d)
"""

def solve(stream, n):
    # Write your code here.
    return None
