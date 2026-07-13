# Minimum Deletions to Make Array Beautiful

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2216 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-deletions-to-make-array-beautiful](https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/).

### Goal
Delete the fewest elements so the resulting array has even length and every pair starting at an even index contains two different values.

### Function Contract
**Inputs**

- `nums`: an integer array.

**Return value**

The minimum number of deletions needed to make the array beautiful.

### Examples
**Example 1**

- Input: `nums = [1, 1, 2, 3, 5]`
- Output: `1`

**Example 2**

- Input: `nums = [1, 1, 2, 2, 3, 3]`
- Output: `2`

**Example 3**

- Input: `nums = [1, 2]`
- Output: `0`

---

## Solution
### Approach
Greedily build valid pairs from left to right. Keep the first value of the current pair; delete every following equal value until a different value can complete that pair. Start a new pair afterward. If one unpaired value remains at the end, delete it too.

### Complexity Analysis
- **Time Complexity**: `O(n)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
