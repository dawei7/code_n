# Minimum Cost to Convert String II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2977 |
| Difficulty | Hard |
| Topics | Array, String, Dynamic Programming, Graph Theory, Trie, Shortest Path |
| Official Link | [minimum-cost-to-convert-string-ii](https://leetcode.com/problems/minimum-cost-to-convert-string-ii/) |

## Problem Description & Examples
### Goal
Given two strings `source` and `target` of equal length, and a set of transformation rules where converting a substring `original[i]` to `changed[i]` incurs a specific `cost[i]`, determine the minimum total cost to transform `source` into `target`. If the transformation is impossible, return -1.

### Function Contract
**Inputs**

- `source` (str): The initial string.
- `target` (str): The desired string.
- `original` (List[str]): List of starting substrings for transformations.
- `changed` (List[str]): List of resulting substrings for transformations.
- `cost` (List[int]): List of costs associated with each transformation.

**Return value**

- `int`: The minimum cost to transform `source` to `target`, or -1 if impossible.

### Examples
**Example 1**

- Input: `source = "abcd"`, `target = "acde"`, `original = ["ab","ac"], changed = ["ac","bc"], cost = [2,1]`
- Output: `-1`

**Example 2**

- Input: `source = "abcdefgh"`, `target = "acdeeghh"`, `original = ["bcd","fgh","th"], changed = ["cde","thh","gh"], cost = [1,3,5]`
- Output: `9`

**Example 3**

- Input: `source = "abcdefg"`, `target = "affgefg"`, `original = ["bcd","efg"], changed = ["fge","fge"], cost = [1,2]`
- Output: `3`

---

## Underlying Base Algorithm(s)
The problem is solved using a combination of:
1. **Trie (Prefix Tree)**: To efficiently map all unique substrings involved in transformations to integer IDs.
2. **Floyd-Warshall Algorithm**: To compute the all-pairs shortest paths between all unique substrings identified in the Trie.
3. **Dynamic Programming**: A linear DP approach where `dp[i]` represents the minimum cost to transform the prefix of `source` up to index `i` into the corresponding prefix of `target`.

---

## Complexity Analysis
- **Time Complexity**: $O(N \cdot L^2 + K^3)$, where $N$ is the length of the strings, $L$ is the maximum length of a transformation substring, and $K$ is the number of unique substrings. The $K^3$ comes from Floyd-Warshall, and $N \cdot L^2$ from the DP transitions.
- **Space Complexity**: $O(K^2 + K \cdot L)$, primarily for the distance matrix and the Trie structure.
