# Minimum Number of Operations to Reinitialize a Permutation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1806 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [minimum-number-of-operations-to-reinitialize-a-permutation](https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation/).

### Goal
Start with the identity permutation of length `n`. Repeatedly apply the given even-length permutation transformation until the identity permutation returns. Count the operations.

### Function Contract
**Inputs**

- `n`: an even positive integer.

**Return value**

Return the minimum positive number of transformations needed to restore the original permutation.

### Examples
**Example 1**

- Input: `n = 2`
- Output: `1`

**Example 2**

- Input: `n = 4`
- Output: `2`

**Example 3**

- Input: `n = 6`
- Output: `4`

---

## Solution
### Approach
Track where one representative index, usually index `1`, moves under the transformation. The whole permutation returns when that index returns to `1`. Each step maps an index `i` to `i / 2` if even, otherwise `n / 2 + (i - 1) / 2`.

### Complexity Analysis
- **Time Complexity**: `O(answer)`
- **Space Complexity**: `O(1)`

### Reference Implementations
_No local optimal implementation has been authored for this challenge yet._
