# Prime Subtraction Operation

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2601 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Binary Search, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/prime-subtraction-operation/) |

## Problem Description

### Goal

You are given a zero-indexed array `nums` of positive integers. For any index, you may perform at most one operation: choose a prime number strictly smaller than the current value at that index and subtract it from that value.

Different indices may use different primes, and an index may also remain unchanged. After all chosen operations, every element must be strictly greater than its predecessor.

Return whether it is possible to make `nums` strictly increasing under these rules.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \leq n \leq 1000$ and $1 \leq \texttt{nums[i]} \leq 1000$.

Let $M = \max(\texttt{nums})$.

**Return value**

- `true` if choosing at most one valid prime subtraction per index can produce a strictly increasing array; otherwise, `false`.

### Examples

#### Example 1

- **Input:** `nums = [4,9,6,10]`
- **Output:** `true`

Subtracting `3` from `4` and `7` from `9` yields `[1,2,6,10]`, which is strictly increasing.

#### Example 2

- **Input:** `nums = [6,8,11,12]`
- **Output:** `true`

The array is already strictly increasing, so no subtraction is required.

#### Example 3

- **Input:** `nums = [5,8,3]`
- **Output:** `false`

No permitted choices can make the final value strictly greater than its predecessor.
