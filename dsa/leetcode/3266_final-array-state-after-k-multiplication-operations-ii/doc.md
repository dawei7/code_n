# Final Array State After K Multiplication Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3266 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/) |

## Problem Description

### Goal

Given `nums`, perform exactly `k` operations. Each operation selects the current minimum value; if several positions share that value, it selects the smallest index. Replace the selected value by its product with `multiplier`, and use the full product when deciding every later minimum.

Only after all operations are finished, reduce every final value modulo $10^9 + 7$. The modulus must not be applied during the simulation because doing so could change later ordering. Return the reduced values in their original array positions.

### Function Contract

**Inputs**

- `nums`: A positive integer list of length $n$, where $1 \le n \le 10^4$ and each initial value is at most $10^9$.
- `k`: The exact operation count, where $1 \le k \le 10^9$.
- `multiplier`: A positive integer factor, where $1 \le \texttt{multiplier} \le 10^6$.

Let $M = \max(\texttt{nums})$ before any operation.

**Return value**

- The length-$n$ final array in original index order after all operations, with each value reduced modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `nums = [2,1,3,5,6], k = 5, multiplier = 2`
- Output: `[8,4,6,5,6]`

**Example 2**

- Input: `nums = [100000,2000], k = 2, multiplier = 1000000`
- Output: `[999999307,999999993]`

The unreduced final values are `100000000000` and `2000000000`; modulo is applied afterward.

**Example 3**

- Input: `nums = [7,3,3], k = 1000000000, multiplier = 1`
- Output: `[7,3,3]`

Multiplication by one never changes the array, even though the operation count is large.
