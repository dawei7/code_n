# Ways to Split Array Into Three Subarrays

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1712 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Binary Search, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/) |

## Problem Description
### Goal

Split a non-negative integer array into three non-empty contiguous subarrays named `left`, `mid`, and `right`, in that order. A split is good when the sum of `left` is at most the sum of `mid`, and the sum of `mid` is at most the sum of `right`.

Count every distinct pair of cut positions that creates a good split. Because the count may be large, return it modulo $10^9+7$.

### Function Contract
**Inputs**

- `nums`: a list of $n$ non-negative integers
- $3 \le n \le 10^5$
- $0 \le \texttt{nums[i]} \le 10^4$

**Return value**

The number of pairs of cuts producing three non-empty contiguous parts whose sums satisfy $\operatorname{sum}(\texttt{left}) \le \operatorname{sum}(\texttt{mid}) \le \operatorname{sum}(\texttt{right})$, reduced modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `nums = [1, 1, 1]`
- Output: `1`

The only possible split gives three sums equal to one.

**Example 2**

- Input: `nums = [1, 2, 2, 2, 5, 0]`
- Output: `3`

The three good partitions have sums `(1, 2, 9)`, `(1, 4, 7)`, and `(3, 4, 5)`.

**Example 3**

- Input: `nums = [3, 2, 1]`
- Output: `0`

The only split has sums `(3, 2, 1)`, which violate both required inequalities.
