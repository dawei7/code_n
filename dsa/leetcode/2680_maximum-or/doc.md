# Maximum OR

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2680 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Bit Manipulation, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/maximum-or/) |

## Problem Description

### Goal

You are given a 0-indexed integer array `nums` and an integer `k`. One operation chooses any array element and multiplies it by 2. You may perform at most `k` operations, choosing the same or different elements on different operations.

Maximize the bitwise OR of every array element after the operations, and return that maximum possible value. For integers `a` and `b`, `a | b` denotes their bitwise OR.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \leq n \leq 10^5$ and every value is at most $10^9$.
- `k`: The maximum number of doubling operations, with $1 \leq k \leq 15$.

**Return value**

Return the largest bitwise OR obtainable after using at most `k` operations.

### Examples

#### Example 1

- **Input:** `nums = [12,9], k = 1`
- **Output:** `30`
- **Explanation:** Doubling 9 produces `[12,18]`, whose bitwise OR is 30.

#### Example 2

- **Input:** `nums = [8,1,2], k = 2`
- **Output:** `35`
- **Explanation:** Applying both operations to 8 produces `[32,1,2]`, whose bitwise OR is 35.
