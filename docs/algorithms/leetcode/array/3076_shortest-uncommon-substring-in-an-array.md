# Shortest Uncommon Substring in an Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3076 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Trie |
| Official Link | [shortest-uncommon-substring-in-an-array](https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/) |

## Problem Description & Examples
### Goal
Given an array of strings, determine the shortest substring for each string that does not appear as a substring in any other string within the array. If multiple such substrings exist for a given string, choose the lexicographically smallest one. If no such substring exists, return an empty string for that index.

### Function Contract
**Inputs**

- `arr`: A list of strings (`List[str]`) where each string consists of lowercase English letters.

**Return value**

- A list of strings (`List[str]`) where the $i$-th element is the shortest, lexicographically smallest uncommon substring of `arr[i]`.

### Examples
**Example 1**

- Input: `arr = ["cab","ad","bad","c"]`
- Output: `["ab","ad","ba",""]`

**Example 2**

- Input: `arr = ["abc","bcd","abcd"]`
- Output: `["","","abcd"]`

**Example 3**

- Input: `arr = ["xyz","xyz","xyz"]`
- Output: `["","",""]`

---

## Underlying Base Algorithm(s)
The problem is solved by generating all possible substrings for each string in the input array. We use a frequency map (Hash Table) to count the occurrences of every substring across all strings. A substring is "uncommon" if its frequency count is exactly 1 and it belongs to the string currently being processed. We iterate through lengths from 1 to the string length to ensure we find the shortest substring first, and sort lexicographically for ties.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L^3)$, where $N$ is the number of strings and $L$ is the maximum length of a string. Generating all substrings takes $O(L^2)$ and string slicing/hashing takes $O(L)$, resulting in $O(N \cdot L^3)$.
- **Space Complexity**: $O(N \cdot L^3)$ to store all possible substrings in a hash map.
