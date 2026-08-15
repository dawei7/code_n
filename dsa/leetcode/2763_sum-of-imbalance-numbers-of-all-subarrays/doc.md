# Sum of Imbalance Numbers of All Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2763 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Sum of Imbalance Numbers of All Subarrays](https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/) |

## Problem Description

### Goal

For a 0-indexed integer array `arr` of length $m$, let `sarr` be `arr` sorted into non-decreasing order. Its imbalance number is the count of indices $i$ with $0 \leq i < m - 1$ for which the neighboring sorted values have a gap greater than one: `sarr[i + 1] - sarr[i] > 1`.

Given a 0-indexed integer array `nums`, consider every non-empty contiguous subarray independently. Compute the imbalance number of each one using the definition above, then return the sum of those values over all subarrays.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \leq n \leq 1000$ and $1 \leq \texttt{nums[i]} \leq n$.

**Return value**

Return the sum of the imbalance numbers of every non-empty contiguous subarray of `nums`.

### Examples

#### Example 1

- **Input:** `nums = [2,3,1,4]`
- **Output:** `3`
- **Explanation:** Exactly three subarrays have nonzero imbalance: `[3,1]`, `[3,1,4]`, and `[1,4]`. Each contributes one.

#### Example 2

- **Input:** `nums = [1,3,3,3,5]`
- **Output:** `8`
- **Explanation:** Six qualifying subarrays contribute one each, while `[1,3,3,3,5]` contributes two; all remaining subarrays contribute zero.
