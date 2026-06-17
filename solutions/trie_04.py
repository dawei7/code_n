"""Solution for trie_04: Delete Word from Trie.

Build a trie from a list of words, delete a target word,
and return True iff the trie still contains the target.
The trie keeps a per-node counter (number of words
passing through); delete decrements them. The word is
still present iff some other word shares the same path.
Source: https://www.geeksforgeeks.org/trie-delete/

Inputs passed to solve():
    words: list of n words (>= 2).
    n: number of words.
    target: the word to delete.

Goal:
    True iff target is still in the trie after deletion.

Samples:
Sample 1 input:  words = ["abc", "abd"], n = 2, target = "abc"
Sample 1 output: False (deleted)

Sample 2 input:  words = ["abc", "abc"], n = 2, target = "abc"
Sample 2 output: True (one remains)


"""

def solve(words, n, target):
    # Write your code here.
    return None
