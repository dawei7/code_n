# Maximum Frequency of an Element After Performing Operations II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3347 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Binary Search, Sliding Window, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/) |

## Problem Description

### Goal

You are given an integer array `nums`, a non-negative limit `k`, and an operation count `numOperations`. Perform exactly `numOperations` operations. Each operation selects an index that no earlier operation selected and adds one integer from the inclusive interval `[-k, k]` to that element.

Different selected positions may receive different adjustments, including zero. After completing all operations, return the greatest frequency that any single integer can have in the array. Values and adjustments can be as large as $10^9$, so the relevant coordinates may be widely separated even though the array contains at most $10^5$ elements.

### Function Contract

**Inputs**

- `nums`: A non-empty list with $1 \le \lvert\texttt{nums}\rvert \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^9$.
- `k`: The maximum absolute adjustment permitted for one selected element, with $0 \le k \le 10^9$.
- `numOperations`: The exact number of distinct indices to select, with $0 \le \texttt{numOperations} \le \lvert\texttt{nums}\rvert$.

Selecting index `i` replaces `nums[i]` by `nums[i] + delta`, where `-k <= delta <= k`; no index may be selected twice.

**Return value**

Return the maximum attainable count of equal elements after all operations.

### Examples

#### Example 1

- **Input:** `nums = [1, 4, 5], k = 1, numOperations = 2`
- **Output:** `2`
- **Explanation:** Add zero to `4` and add `-1` to `5`; afterward, `4` occurs twice.

#### Example 2

- **Input:** `nums = [5, 11, 20, 20], k = 5, numOperations = 1`
- **Output:** `2`
- **Explanation:** The two copies of `20` already form the best frequency, and adding zero to `11` performs the required operation without changing it.

#### Example 3

- **Input:** `nums = [1, 1000000000], k = 500000000, numOperations = 2`
- **Output:** `2`
- **Explanation:** Both elements can be moved to `500000000`, even though that target is absent from the original array.
