"""Solution for string_06: Rabin-Karp.

Find the first index where pattern occurs in text using
the Rabin-Karp rolling-hash algorithm. Uses a base-256
polynomial hash mod a large prime; on a hash match we
verify by direct comparison to avoid false positives.
Requirement: O(n + m) average; worst-case O(n*m) on
spurious hash collisions (vanishingly rare in practice).
Source: https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching/

Inputs passed to solve():
    text: the string to search in.
    pattern: the string to search for.

Goal:
    the first index of pattern in text, or -1 if not found.

Samples:
Sample 1 input:  text = 'hello', pattern = 'll'
Sample 1 output: 2

Sample 2 input:  text = 'aaaa', pattern = 'aa'
Sample 2 output: 0

Sample 3 input:  text = 'abcde', pattern = 'xyz'
Sample 3 output: -1

"""

def solve(text, pattern):
    # Write your code here.
    return None
