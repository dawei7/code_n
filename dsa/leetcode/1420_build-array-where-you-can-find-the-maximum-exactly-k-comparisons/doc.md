# Build Array Where You Can Find The Maximum Exactly K Comparisons

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1420 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons/) |

## Problem Description

### Goal

Consider arrays of length `n` whose elements are integers from $1$ through `m`. Scan one such array from left to right while maintaining the largest value seen. Its search cost increases whenever the current element is strictly greater than every earlier element, including the first element.

Count how many possible arrays have search cost exactly `k`. Arrays are distinguished by their complete sequence of values, and the answer must be returned modulo $10^9 + 7$.

### Function Contract

**Inputs**

- `n`: the array length, where $1 \le n \le 50$.
- `m`: the largest allowed element value, where $1 \le m \le 50$.
- `k`: the required search cost, where $1 \le k \le n$.

**Return value**

- The number of length-`n` arrays over values $1$ through `m` whose running maximum changes exactly `k` times, modulo $10^9 + 7$.

### Examples

**Example 1**

- Input: `n = 2, m = 3, k = 1`
- Output: `6`

**Example 2**

- Input: `n = 5, m = 2, k = 3`
- Output: `0`

**Example 3**

- Input: `n = 9, m = 1, k = 1`
- Output: `1`
