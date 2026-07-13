# Minimum Swaps to Group All 1's Together

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1151 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-swaps-to-group-all-1s-together](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/).

### Goal
Given a binary array, return the fewest swaps needed so that every `1` appears in one contiguous block. A swap may exchange any two positions.

### Function Contract
**Inputs**

- `data`: List containing only `0` and `1`.

**Return value**

Minimum number of swaps required.

### Examples
**Example 1**

- Input: `data = [1, 0, 1, 0, 1]`
- Output: `1`

**Example 2**

- Input: `data = [0, 0, 0, 1, 0]`
- Output: `0`

**Example 3**

- Input: `data = [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1]`
- Output: `3`

---

## Solution
### Approach
Let `ones` be the total number of `1` values. Any final grouped block must have length `ones`, and every `0` inside that block must be swapped with a `1` outside it.

Slide a window of length `ones` across the array and count how many `0` values it contains. The minimum such count is the answer.

### Complexity Analysis
- **Time Complexity**: `O(n)`, where `n` is the length of `data`.
- **Space Complexity**: `O(1)`.

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
