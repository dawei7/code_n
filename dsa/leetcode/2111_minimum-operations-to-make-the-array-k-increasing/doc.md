# Minimum Operations to Make the Array K-Increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2111 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [minimum-operations-to-make-the-array-k-increasing](https://leetcode.com/problems/minimum-operations-to-make-the-array-k-increasing/) |

## Problem Description

### Goal

You are given a 0-indexed array `arr` of $n$ positive integers and a positive integer `k`. The array is K-increasing when `arr[i - k] <= arr[i]` for every index $i$ from `k` through $n-1$. Thus, values whose indices have the same remainder modulo `k` must appear in non-decreasing order.

In one operation, choose any index and replace its value with any positive integer. Determine the minimum number of such replacements needed to make all K-spaced comparisons valid. Unchanged values may be equal because the required relation is non-decreasing, not strictly increasing.

### Function Contract

**Inputs**

- `arr`: A positive integer array of length $n$, where $1 \le n \le 10^5$ and $1 \le \texttt{arr[i]} \le n$.
- `k`: The positive index distance in the K-increasing relation, where $1 \le k \le n$.

**Return value**

Return the minimum number of array elements that must be replaced to make `arr` K-increasing.

### Examples

#### Example 1

- **Input:** `arr = [5, 4, 3, 2, 1], k = 1`
- **Output:** `4`
- **Explanation:** With `k = 1`, the whole array must become non-decreasing; at most one value can remain unchanged.

#### Example 2

- **Input:** `arr = [4, 1, 5, 2, 6, 2], k = 2`
- **Output:** `0`
- **Explanation:** Both modulo-$2$ sequences, `[4, 5, 6]` and `[1, 2, 2]`, are already non-decreasing.

#### Example 3

- **Input:** `arr = [4, 1, 5, 2, 6, 2], k = 3`
- **Output:** `2`
