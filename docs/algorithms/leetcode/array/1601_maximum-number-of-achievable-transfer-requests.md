# Maximum Number of Achievable Transfer Requests

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1601 |
| Difficulty | Hard |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Official Link | [maximum-number-of-achievable-transfer-requests](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) |

## Problem Description & Examples
### Goal
Choose as many employee transfer requests as possible while keeping the net
employee count of every building unchanged.

### Function Contract
**Inputs**

- `n`: the number of buildings.
- `requests`: transfer pairs `[from, to]`.

**Return value**

The maximum number of requests that can be accepted together.

### Examples
**Example 1**

- Input: `n = 5, requests = [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]]`
- Output: `5`

**Example 2**

- Input: `n = 3, requests = [[0, 0], [1, 2], [2, 1]]`
- Output: `3`

**Example 3**

- Input: `n = 4, requests = [[0, 3], [3, 1], [1, 2], [2, 0]]`
- Output: `4`

---

## Underlying Base Algorithm(s)
Backtrack over requests, either taking or skipping each one. Maintain a balance
array where outgoing transfers decrement and incoming transfers increment. At
the end of a branch, the accepted set is valid only if every balance is zero.
Prune branches that cannot beat the best answer already found.

---

## Complexity Analysis
- **Time Complexity**: `O(2^r * n)` in the direct subset search, where `r` is the number of requests.
- **Space Complexity**: `O(n + r)` for balances and recursion depth.
