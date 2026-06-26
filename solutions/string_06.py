"""
Description
-----------
Find the first index where pattern occurs in text using
the Rabin-Karp rolling-hash algorithm. Uses a base-256
polynomial hash mod a large prime; on a hash match we
verify by direct comparison to avoid false positives.
Requirement: O(n + m) average; worst-case O(n*m) on
spurious hash collisions (vanishingly rare in practice).
Source: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

Examples
--------
Example 1:
Input:  text = 'hello', pattern = 'll'
Output: 2

Example 2:
Input:  text = 'aaaa', pattern = 'aa'
Output: 0

Example 3:
Input:  text = 'abcde', pattern = 'xyz'
Output: -1
"""

def solve(text, pattern):
    # Write your code here.
    return None
