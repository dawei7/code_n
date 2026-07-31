# Count Increasing Quadruplets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2552 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Binary Indexed Tree, Enumeration, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [count-increasing-quadruplets](https://leetcode.com/problems/count-increasing-quadruplets/) |

## Problem Description

### Goal

The 0-indexed integer array `nums` has length $n$ and is a permutation of every integer from 1 through $n$. Count quadruplets of indices `(i, j, k, l)` chosen in strictly increasing index order:

$$
0 \le i < j < k < l < n.
$$

Such a quadruplet is counted only when its values satisfy the crossed strict order $\texttt{nums[i]} < \texttt{nums[k]} < \texttt{nums[j]} < \texttt{nums[l]}$. Return the total number of qualifying index quadruplets.

### Function Contract

**Inputs**

- `nums`: A permutation of the integers from 1 through its length.

The constraint is $4 \le n \le 4000$.

**Return value**

Return the number of quadruplets satisfying both the index order and the required value order.

### Examples

**Example 1**

- Input: `nums = [1,3,2,4,5]`
- Output: `2`
- Explanation: Indices `(0,1,2,3)` and `(0,1,2,4)` both satisfy $1 < 2 < 3$ followed by a larger fourth value.

**Example 2**

- Input: `nums = [1,2,3,4]`
- Output: `0`
- Explanation: Its only index quadruplet has `nums[j] < nums[k]`, contrary to the required crossed order.
