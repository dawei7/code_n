# Time Based Key-Value Store

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 981 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Hash Table, String, Binary Search, Design |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [time-based-key-value-store](https://leetcode.com/problems/time-based-key-value-store/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/time-based-key-value-store/).

### Goal
Given two linked lists `list_a` and `list_b` (as arrays) and an `intersection_val` (the value at their intersection, or -1 if none), return the value of the intersection node or -1.

### Function Contract
**Inputs**

- `list_a`: List[int]
- `list_b`: List[int]
- `intersection_val`: int - value at intersection or -1

**Return value**

int - intersection node value or -1

### Examples
**Example 1**

- Input: `list_a = [4, 1, 8, 4, 5], intersection_val = 8`
- Output: `8`

**Example 2**

- Input: `list_a = [6, 50], list_b = [66, 50], intersection_val = 50`
- Output: `50`

**Example 3**

- Input: `list_a = [33, 18], list_b = [64, 18], intersection_val = 18`
- Output: `18`

---

## Solution
### Approach
- [Binary search](search_02_binary-search.md)
- [Search in rotated sorted array](search_12_search-in-rotated-sorted-array.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
