# Minimum Cost to Convert String I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2976 |
| Difficulty | Medium |
| Topics | Array, String, Graph Theory, Shortest Path |
| Official Link | [minimum-cost-to-convert-string-i](https://leetcode.com/problems/minimum-cost-to-convert-string-i/) |

## Problem Description & Examples
### Goal
Given two strings of equal length and a set of transformation rules between individual characters with associated costs, calculate the minimum total cost required to transform the source string into the target string. If a character cannot be transformed into the target character, return -1.

### Function Contract
**Inputs**

- `source`: A string representing the starting sequence.
- `target`: A string representing the desired final sequence.
- `original`: A list of characters representing the starting point of a transformation rule.
- `changed`: A list of characters representing the destination of a transformation rule.
- `cost`: A list of integers representing the cost of each transformation rule.

**Return value**

- An integer representing the minimum total cost to convert `source` to `target`, or -1 if the transformation is impossible.

### Examples
**Example 1**

- Input: `source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]`
- Output: `28`

**Example 2**

- Input: `source = "aaaa", target = "bbbb", original = ["a","c"], changed = ["c","b"], cost = [1,2]`
- Output: `12`

**Example 3**

- Input: `source = "abcd", target = "abdc", original = ["a","b"], changed = ["b","c"], cost = [1,2]`
- Output: `-1`

---

## Underlying Base Algorithm(s)
The problem is modeled as a shortest-path problem on a directed graph where nodes are the 26 lowercase English letters. Since the number of nodes is small (26), the **Floyd-Warshall algorithm** is the optimal choice to precompute the all-pairs shortest paths between all character pairs.

---

## Complexity Analysis
- **Time Complexity**: O(N + V³), where N is the length of the source string and V is the number of possible characters (26). The Floyd-Warshall precomputation takes O(V³), and the final string transformation takes O(N).
- **Space Complexity**: O(V²), required to store the adjacency matrix representing the minimum transformation costs between all character pairs.
