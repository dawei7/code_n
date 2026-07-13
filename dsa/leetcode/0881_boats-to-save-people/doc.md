# Boats to Save People

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 881 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [boats-to-save-people](https://leetcode.com/problems/boats-to-save-people/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/boats-to-save-people/).

### Goal
Given an integer array `nums` and an integer `k`, you can increment any element by 1 at most `k` times total. Find the maximum frequency of any element after these operations.

### Function Contract
**Inputs**

- `nums`: List[int]
- `k`: int

**Return value**

int - maximum achievable frequency

### Examples
**Example 1**

- Input: `nums = [1, 2, 4], k = 5`
- Output: `3`

**Example 2**

- Input: `nums = [25, 49], k = 3`
- Output: `1`

**Example 3**

- Input: `nums = [9, 37], k = 1`
- Output: `1`

---

## Solution
### Approach
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

### Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
