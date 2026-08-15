# Find Xor-Beauty of Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2527 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-xor-beauty-of-array/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums`. For any ordered triplet of indices $(i,j,k)$, define its effective value as `((nums[i] | nums[j]) & nums[k])`, where `|` and `&` are bitwise OR and bitwise AND.

Consider every ordered triplet satisfying $0 \le i,j,k < n$; indices may be equal, and changing their order produces a different triplet. Return the bitwise XOR of all $n^3$ effective values. This combined result is the array's xor-beauty.

### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $n = \lvert\texttt{nums}\rvert$. The input satisfies $1 \le n \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.

**Return value**

Return the XOR of `((nums[i] | nums[j]) & nums[k])` over every ordered index triplet $(i,j,k)$.

### Examples

#### Example 1

- **Input:** `nums = [1, 4]`
- **Output:** `5`
- **Explanation:** XORing the eight ordered triplets' effective values gives `1 ^ 0 ^ 1 ^ 4 ^ 1 ^ 4 ^ 0 ^ 4 = 5`.

#### Example 2

- **Input:** `nums = [15, 45, 20, 2, 34, 35, 5, 44, 32, 30]`
- **Output:** `34`
