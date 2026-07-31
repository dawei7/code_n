# Choose K Elements With Maximum Sum

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3478 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Sorting, Heap (Priority Queue) |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/choose-k-elements-with-maximum-sum/) |

## Problem Description

### Goal

The integer arrays `nums1` and `nums2` have the same length $n$, and values at the same index form a pair. For every index $i$, consider exactly those indices $j$ whose first-array value satisfies the strict inequality `nums1[j] < nums1[i]`.

From the corresponding eligible values `nums2[j]`, choose at most `k` elements so their sum is as large as possible. All `nums2` values are positive, so this means summing the largest `k` eligible values when at least `k` exist, or summing every eligible value when fewer exist. If no index satisfies the strict inequality, the sum is zero.

Return all $n$ maximum sums in original index order. Indices with equal values in `nums1` are not eligible for one another because equality does not satisfy `<`.

### Function Contract

**Inputs**

- `nums1`: A list of $n$ positive integers that determines eligibility by strict comparison.
- `nums2`: A list of $n$ positive integers whose values contribute to sums.
- `k`: A positive integer giving the maximum number of eligible values that may be chosen.

The constraints are $1 \le n \le 10^5$, $1 \le \texttt{nums1[i]},\texttt{nums2[i]} \le 10^6$, and $1 \le k \le n$.

**Return value**

Return an integer list `answer` of length $n$. For each $i$, `answer[i]` is the sum of the largest at most `k` values `nums2[j]` over all indices satisfying `nums1[j] < nums1[i]`.

### Examples

**Example 1**

- Input: `nums1 = [4, 2, 1, 5, 3]`, `nums2 = [10, 20, 30, 40, 50]`, `k = 2`
- Output: `[80, 30, 0, 80, 50]`

For index 0, eligible second-array values are `20`, `30`, and `50`, so the largest two sum to `80`. Index 2 has the smallest first-array value and therefore has no eligible indices.

**Example 2**

- Input: `nums1 = [2, 2, 2, 2]`, `nums2 = [3, 1, 2, 3]`, `k = 1`
- Output: `[0, 0, 0, 0]`

All first-array values are equal, so the strict inequality excludes every possible index for every answer position.
