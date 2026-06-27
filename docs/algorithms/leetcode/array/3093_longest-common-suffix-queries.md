# Longest Common Suffix Queries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3093 |
| Difficulty | Hard |
| Topics | Array, String, Trie |
| Official Link | [longest-common-suffix-queries](https://leetcode.com/problems/longest-common-suffix-queries/) |

## Problem Description & Examples
### Goal
Given two arrays of strings, `wordsContainer` and `wordsQuery`, determine the index of the string in `wordsContainer` that shares the longest common suffix with each string in `wordsQuery`. If multiple strings in `wordsContainer` share the same maximum suffix length, choose the one with the minimum length. If there is still a tie, choose the one with the smallest original index.

### Function Contract
**Inputs**

- `wordsContainer`: A list of strings representing the dictionary to search within.
- `wordsQuery`: A list of strings representing the queries to perform.

**Return value**

- A list of integers where each integer corresponds to the index of the best-matching string in `wordsContainer` for the respective query in `wordsQuery`.

### Examples
**Example 1**

- Input: `wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]`
- Output: `[1,1,1]`

**Example 2**

- Input: `wordsContainer = ["abcdef","bcd","xyz"], wordsQuery = ["xyz","abc"]`
- Output: `[2,0]`

**Example 3**

- Input: `wordsContainer = ["a","b","c"], wordsQuery = ["d","e","f"]`
- Output: `[0,0,0]`

---

## Underlying Base Algorithm(s)
The problem is solved using a **Trie (Prefix Tree)**. Since we are matching suffixes, we insert the reversed strings of `wordsContainer` into the Trie. Each node in the Trie stores the index of the "best" string encountered so far that passes through that node (based on the criteria: longest suffix, shortest length, smallest index). During query time, we reverse the query string and traverse the Trie until we can no longer match characters, returning the index stored at the last reachable node.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L + M \cdot K)$, where $N$ is the number of words in `wordsContainer`, $L$ is the average length of these words, $M$ is the number of queries, and $K$ is the average length of query strings.
- **Space Complexity**: $O(N \cdot L \cdot \Sigma)$, where $\Sigma$ is the alphabet size (26), representing the space required to store the Trie nodes.
