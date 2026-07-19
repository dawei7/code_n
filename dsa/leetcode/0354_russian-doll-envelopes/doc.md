# Russian Doll Envelopes

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 354 |
| Difficulty | Hard |
| Topics | Array, Binary Search, Dynamic Programming, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/russian-doll-envelopes/) |

## Problem Description
### Goal
Given envelope dimensions `[width, height]`, build a nested chain by placing one envelope strictly inside the next. Envelope `a` fits inside envelope `b` only when both `a.width < b.width` and `a.height < b.height`; rotation is forbidden.

Return the maximum number of envelopes in any valid chain. Equal width or equal height prevents one envelope from containing the other, even when the remaining dimension is larger. Each input envelope occurrence may appear at most once, and the function returns only the optimal chain length rather than the envelopes or their nesting order. A one-envelope input returns `1` because that envelope alone forms a valid chain.

### Function Contract
**Inputs**

- `envelopes`: a list of `[width, height]` pairs

**Return value**

- The maximum length of a strictly nested envelope chain.

### Examples
**Example 1**

- Input: `envelopes = [[5,4],[6,4],[6,7],[2,3]]`
- Output: `3`
- Explanation: `[2,3] -> [5,4] -> [6,7]` is a valid chain.

**Example 2**

- Input: `envelopes = [[1,1],[1,1],[1,1]]`
- Output: `1`

**Example 3**

- Input: `envelopes = [[4,5],[4,6],[6,7],[2,3],[1,1]]`
- Output: `4`
