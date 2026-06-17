"""Solution for trie_01: Trie Insert and Search.

Build a trie from a list of words, then return True iff
a given target word is in the trie. To insert, walk from
the root creating nodes as needed. To search, walk from
the root and check that every character exists, and that
the final node is marked as a word end. O(total chars).
Source: https://www.geeksforgeeks.org/trie-insert-and-search/

Inputs passed to solve():
    words: list of n words (single lower-case ASCII each).
    n: number of words.
    target: the word to search for.

Goal:
    True iff target is in the trie (the setup guarantees True).

Samples:
Sample 1 input:  words = ["cat", "car", "dog"], n = 3, target = "car"
Sample 1 output: True

Sample 2 input:  words = ["cat", "car", "dog"], n = 3, target = "cap"
Sample 2 output: True (setup only tests positive cases)


"""

def solve(words, n, target):
    # Write your code here.
    return None
