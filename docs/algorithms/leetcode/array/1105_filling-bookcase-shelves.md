# Filling Bookcase Shelves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1105 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming |
| Official Link | [filling-bookcase-shelves](https://leetcode.com/problems/filling-bookcase-shelves/) |

## Problem Description & Examples
### Goal
Place books in their given order onto shelves of fixed width. Each book has a width and height. Minimize the sum of shelf heights.

### Function Contract
**Inputs**

- `books`: list of `[thickness, height]` pairs in the order they must be placed.
- `shelfWidth`: maximum total thickness allowed on one shelf.

**Return value**

The minimum possible total height of the bookcase.

### Examples
**Example 1**

- Input: `books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]`, `shelfWidth = 4`
- Output: `6`

**Example 2**

- Input: `books = [[1,3],[2,4],[3,2]]`, `shelfWidth = 6`
- Output: `4`

**Example 3**

- Input: `books = [[2,5],[2,6],[2,7]]`, `shelfWidth = 4`
- Output: `12`

---

## Underlying Base Algorithm(s)
Dynamic programming over ordered partitions.

---

## Complexity Analysis
- **Time Complexity**: `O(n^2)`
- **Space Complexity**: `O(n)`
