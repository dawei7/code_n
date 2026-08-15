# Jump Game IX

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3660 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/jump-game-ix/) |

## Problem Description

### Goal

Given an integer array `nums`, begin at any index `i` and make zero or more valid jumps between indices. A forward jump from `i` to a larger index `j` is allowed only when `nums[j] < nums[i]`.

A backward jump from `i` to a smaller index `j` follows the opposite value relation: it is allowed only when `nums[j] > nums[i]`. Both inequalities are strict, and a jump may skip any number of intermediate positions.

For every starting index, determine the largest array value present at any index reachable by a valid jump sequence, including the starting index itself. Return these maxima in an array `ans`, where `ans[i]` corresponds to start index `i`.

### Function Contract

**Inputs**

- `nums`: a nonempty integer array of length $n$, where $1\le n\le 10^5$ and $1\le\texttt{nums[i]}\le 10^9$.

**Return value**

Return an integer array of length $n$. Its value at index `i` is the maximum value reachable from `i` through any sequence of valid forward and backward jumps.

### Examples

#### Example 1

- **Input:** `nums = [2, 1, 3]`
- **Output:** `[2, 2, 3]`
- Indices `0` and `1` can reach one another, while the final value `3` is separate.

#### Example 2

- **Input:** `nums = [2, 3, 1]`
- **Output:** `[3, 3, 3]`
- Index `0` can jump to the smaller value at index `2`, then backward to the larger value `3` at index `1`.

#### Example 3

- **Input:** `nums = [1, 2, 3]`
- **Output:** `[1, 2, 3]`
- No pair forms the strict inversion required for a jump, so each index reaches only itself.
