# Find the Number of K-Even Arrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3339 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Dynamic Programming |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/find-the-number-of-k-even-arrays/) |

## Problem Description

### Goal

You are given integers `n`, `m`, and `k`. Consider every length-`n` array whose elements are selected independently from the inclusive range `[1, m]`. For each adjacent index $i$, evaluate `(arr[i] * arr[i + 1]) - arr[i] - arr[i + 1]`.

An array is **k-even** when that expression is even at exactly `k` of the $n-1$ adjacent positions. Count all possible k-even arrays. Different value choices or positions form different arrays, and the answer must be returned modulo $10^9+7$.

### Function Contract

**Inputs**

- `n`: The array length, where $1 \le n \le 750$.
- `m`: The inclusive upper bound for every element, where $1 \le m \le 1000$.
- `k`: The exact number of qualifying adjacent positions, where $0 \le k \le n-1$.

**Return value**

- The number of length-`n` arrays over `[1,m]` that have exactly `k` adjacent positions with an even expression, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `n = 3, m = 4, k = 2`
- **Output:** `8`
- **Explanation:** Both adjacent positions qualify only when all three values are even. Each position can independently be `2` or `4`.

#### Example 2

- **Input:** `n = 5, m = 1, k = 0`
- **Output:** `1`
- **Explanation:** The only possible array is `[1, 1, 1, 1, 1]`, and no adjacent pair qualifies.

#### Example 3

- **Input:** `n = 7, m = 7, k = 5`
- **Output:** `5832`
