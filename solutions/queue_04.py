"""Solution for queue_04: First Non-Repeating Character in a Stream.


            Given a stream of characters (a string), for each
            prefix of length i, return the first non-repeating
            character in that prefix, or '_' if none exists.
            Use a queue to maintain the candidate set (characters
            seen exactly once so far, in order of first
            appearance) and a frequency counter to detect
            repeats. When a character's count becomes 2, remove
            it from the queue. O(n) time, O(1) space (26 letters).
            Source: https://www.geeksforgeeks.org/first-non-repeating-character-in-a-stream/
            

Inputs passed to solve():
    stream: string of n lowercase letters.
    n: length of stream.

Goal:
    string of length n: for each prefix, the first non-repeating char or '_'.

Samples:
Sample 1 input:  stream = 'aabc', n = 4
Sample 1 output: 'aa_b' (a, a, _, b)

Sample 2 input:  stream = 'aabbccd', n = 7
Sample 2 output: 'aa____d' (a, a, _, _, _, _, d)


"""

def solve(stream, n):
    # Write your code here.
    return None
