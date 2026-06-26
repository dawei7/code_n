# Sort the People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2418 |
| Difficulty | Easy |
| Topics | Array, Hash Table, String, Sorting |
| Official Link | [sort-the-people](https://leetcode.com/problems/sort-the-people/) |

## Problem Description & Examples
### Goal
Given two parallel arrays representing names and heights of individuals, return a list of names sorted in descending order based on their corresponding heights.

### Function Contract
**Inputs**

- `names`: A list of strings where `names[i]` is the name of the i-th person.
- `heights`: A list of integers where `heights[i]` is the height of the i-th person.

**Return value**

- A list of strings containing the names sorted by height from tallest to shortest.

### Examples
**Example 1**

- Input: `names = ["Mary","John","Emma"], heights = [180,165,170]`
- Output: `["Mary","Emma","John"]`

**Example 2**

- Input: `names = ["Alice","Bob","Bob"], heights = [155,185,150]`
- Output: `["Bob","Alice","Bob"]`

**Example 3**

- Input: `names = ["Alex"], heights = [100]`
- Output: `["Alex"]`

---

## Underlying Base Algorithm(s)
The problem is solved by creating pairs of (height, name) and applying a sorting algorithm. Since we need to sort by height in descending order, we can use Python's built-in Timsort (via `sort` or `sorted`), which provides an efficient $O(N \log N)$ performance.

---

## Complexity Analysis
- **Time Complexity**: $O(N \log N)$, where $N$ is the number of people, due to the sorting operation.
- **Space Complexity**: $O(N)$ to store the zipped list of pairs and the resulting list of names.
