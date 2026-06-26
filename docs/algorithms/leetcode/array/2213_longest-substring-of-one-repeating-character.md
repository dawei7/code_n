# Longest Substring of One Repeating Character

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2213 |
| Difficulty | Hard |
| Topics | Array, String, Segment Tree, Ordered Set |
| Official Link | [longest-substring-of-one-repeating-character](https://leetcode.com/problems/longest-substring-of-one-repeating-character/) |

## Problem Description & Examples
### Goal
Apply point updates to a string. After each replacement, report the length of its longest contiguous substring made of one repeated character.

### Function Contract
**Inputs**

- `s`: the initial lowercase string.
- `queryCharacters`: replacement characters, one per query.
- `queryIndices`: matching zero-based positions to update.

**Return value**

An array where each value is the longest equal-character run after the corresponding update.

### Examples
**Example 1**

- Input: `s = "babacc"`, `queryCharacters = "bcb"`, `queryIndices = [1, 3, 3]`
- Output: `[3, 3, 4]`

**Example 2**

- Input: `s = "abyzz"`, `queryCharacters = "aa"`, `queryIndices = [2, 1]`
- Output: `[2, 3]`

**Example 3**

- Input: `s = "a"`, `queryCharacters = "b"`, `queryIndices = [0]`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
Build a segment tree. Each node stores its segment length, leftmost and rightmost characters, longest equal-character prefix and suffix, and best run anywhere in the segment. Merge children by extending prefixes or suffixes when boundary characters match and by considering the joined suffix-plus-prefix run. A point update changes one leaf and recomputes `O(log n)` ancestors; the root's best value answers each query.

---

## Complexity Analysis
- **Time Complexity**: `O(n + q log n)`
- **Space Complexity**: `O(n)`
