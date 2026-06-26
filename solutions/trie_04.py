"""
Description
-----------
Build a trie from a list of words, delete a target word,
and return True iff the trie still contains the target.
The trie keeps a per-node counter (number of words
passing through); delete decrements them. The word is
still present iff some other word shares the same path.
Source: https://www.geeksforgeeks.org/trie-delete/

Examples
--------
Example 1:
Input:  words = ["abc", "abd"], n = 2, target = "abc"
Output: False (deleted)

Example 2:
Input:  words = ["abc", "abc"], n = 2, target = "abc"
Output: True (one remains)
"""

def solve(words, n, target):
    # Write your code here.
    return None
