# Maximum Number of Achievable Transfer Requests

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1601 |
| Difficulty | Hard |
| Topics | Array, Backtracking, Bit Manipulation, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/) |

## Problem Description
### Goal
There are `n` full office buildings numbered from `0` through `n - 1`. Each entry `requests[i] = [from_i, to_i]` represents one employee who wants to leave building `from_i` and move into building `to_i`.

Choose as many requests as possible while leaving every building's employee count unchanged. For each building, the number of accepted requests leaving it must equal the number entering it. A request whose source and destination are equal is already balanced and may be accepted without affecting any other building. Return the maximum size of an achievable subset.

### Function Contract
**Inputs**

- `n`: the number of buildings, with $1 \le n \le 20$.
- `requests`: a list of $m$ source-destination pairs, with $1 \le m \le 16$ and both endpoints in $[0,n-1]$.

**Return value**

Return the greatest number of requests whose combined net employee change is zero at every building.

### Examples
**Example 1**

- Input: `n = 5`, `requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]`
- Output: `5`

**Example 2**

- Input: `n = 3`, `requests = [[0,0],[1,2],[2,1]]`
- Output: `3`

**Example 3**

- Input: `n = 4`, `requests = [[0,3],[3,1],[1,2],[2,0]]`
- Output: `4`
