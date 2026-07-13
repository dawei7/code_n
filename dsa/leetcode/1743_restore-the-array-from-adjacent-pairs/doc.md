# Restore the Array From Adjacent Pairs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1743 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Depth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [restore-the-array-from-adjacent-pairs](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/).

### Goal
Given all adjacent pairs from an unknown array of distinct numbers, reconstruct one valid original array.

### Function Contract
**Inputs**

- `adjacentPairs`: a list of unordered adjacent value pairs.

**Return value**

Return the restored array.

### Examples
**Example 1**

- Input: `adjacentPairs = [[2,1],[3,4],[3,2]]`
- Output: `[1,2,3,4]`

**Example 2**

- Input: `adjacentPairs = [[4,-2],[1,4],[-3,1]]`
- Output: `[-2,4,1,-3]`

**Example 3**

- Input: `adjacentPairs = [[100000,-100000]]`
- Output: `[100000,-100000]`

---

## Solution
### Approach
Build an adjacency list graph where each value connects to its neighbors. The original array forms a path, so endpoints have degree one. Start from either endpoint and walk to the next neighbor that is not the previous value until all values are restored.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(n)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
