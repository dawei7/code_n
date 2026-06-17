"""Solution for hash_04: Group Anagrams.

Group strings that are anagrams of each other. The canonical
key is the sorted tuple of characters. Return a list of groups;
each group's inner list is sorted; the outer list is sorted by
the smallest element of each group.
Requirement: O(n * k log k) where k is the string length.
Source: https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/

Inputs passed to solve():
    strs: list of n short strings.
    n: length of strs.

Goal:
    a list of groups; each group is a sorted list of anagrams; outer list sorted by group min.

Samples:
Sample 1 input:  strs = ["eat", "tea", "tan", "ate", "nat", "bat"], n = 6
Sample 1 output: [["ate","eat","tea"], ["bat"], ["nat","tan"]]

Sample 2 input:  strs = [""], n = 1
Sample 2 output: [[""]]


"""

def solve(strs, n):
    # Write your code here.
    return None
