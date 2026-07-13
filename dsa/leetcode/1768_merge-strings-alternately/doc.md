# Merge Strings Alternately

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1768 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Two Pointers, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [merge-strings-alternately](https://leetcode.com/problems/merge-strings-alternately/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/merge-strings-alternately/).

### Goal
Given `n` non-negative integers `height` where each represents a vertical line at position `i`, find two lines that together with the x-axis form a container that can hold the most water.

### Function Contract
**Inputs**

- `height`: List[int]

**Return value**

int - maximum water the container can hold

### Examples
**Example 1**

- Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- Output: `49`

**Example 2**

- Input: `height = [1, 1]`
- Output: `1`

**Example 3**

- Input: `height = [4, 3, 2, 1, 4]`
- Output: `16`

---

## Solution
### Approach
- [Binary-search-style boundary reasoning](search_02_binary-search.md)

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)` auxiliary space, excluding the output object unless the output itself is the constructed result.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
