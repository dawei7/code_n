# Construct the Minimum Bitwise Array II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3315 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/) |

## Problem Description

### Goal

An input array `nums` contains $n$ prime integers. Build an array `ans` of equal length such that each value and its immediate successor combine under bitwise OR to reproduce the corresponding prime: `ans[i] | (ans[i] + 1) == nums[i]`.

Each position is independent. Select the smallest non-negative `ans[i]` that satisfies the relation for `nums[i]`; if no non-negative integer works, place `-1` there. Prime values may be as large as $10^9$, so searching through all smaller candidates is not feasible.

### Function Contract

**Inputs**

- `nums`: An array of $n$ prime integers, where $1\leq n\leq100$ and $2\leq\texttt{nums[i]}\leq10^9$.

**Return value**

Return the length-$n$ array of minimum valid predecessors, using `-1` exactly where the required OR value cannot be formed.

### Examples

#### Example 1

- **Input:** `nums = [2, 3, 5, 7]`
- **Output:** `[-1, 1, 4, 3]`

Prime 2 is impossible, while `1 | 2 == 3`, `4 | 5 == 5`, and `3 | 4 == 7`.

#### Example 2

- **Input:** `nums = [11, 13, 31]`
- **Output:** `[9, 12, 15]`

#### Example 3

- **Input:** `nums = [99991, 999983]`
- **Output:** `[99987, 999975]`
