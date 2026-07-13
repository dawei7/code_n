# Koko Eating Bananas

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 875 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [koko-eating-bananas](https://leetcode.com/problems/koko-eating-bananas/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/koko-eating-bananas/).

### Goal
Given a linked list (as a list) and integers `left` and `right` (1-indexed), reverse the nodes from position `left` to `right`. Return the modified list.

### Function Contract
**Inputs**

- `head`: List[int]
- `left`: int - start position (1-indexed)
- `right`: int - end position

**Return value**

List[int] - list with sublist reversed

### Examples
**Example 1**

- Input: `head = [1, 2, 3, 4, 5], left = 2, right = 4`
- Output: `[1, 4, 3, 2, 5]`

**Example 2**

- Input: `head = [50, 98], left = 2, right = 2`
- Output: `[50, 98]`

**Example 3**

- Input: `head = [18, 73], left = 1, right = 2`
- Output: `[73, 18]`

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
