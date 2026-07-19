# Distinct Numbers in Each Subarray

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/distinct-numbers-in-each-subarray/) |
| Frontend ID | 1852 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An integer array `nums` has length $n$, and `k` specifies a fixed window length. Consider every contiguous subarray containing exactly `k` elements, beginning at indices $0,1,\ldots,n-k$. Values may repeat within a window or across several overlapping windows.

For each window, count how many different integer values occur at least once inside it. Return those counts in left-to-right window order, producing one result for every possible starting index.

### Function Contract

**Inputs**

- `nums`: a list of integers with $1 \le \lvert\texttt{nums}\rvert \le 10^5$.
- Every value satisfies $1 \le \texttt{nums[i]} \le 10^5$.
- `k`: a window length satisfying $1 \le k \le \lvert\texttt{nums}\rvert$.
- Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- Return a list of length $n-k+1$.
- Its entry at index $i$ is the number of distinct values in `nums[i:i + k]`.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 2, 2, 1, 3]`, `k = 3`
- Output: `[3, 2, 2, 2, 3]`

The first window contains 1, 2, and 3, while the second contains only 2 and 3.

**Example 2**

- Input: `nums = [1, 1, 1, 1, 2, 3, 4]`, `k = 4`
- Output: `[1, 2, 3, 4]`

**Example 3**

- Input: `nums = [5, 5, 5]`, `k = 1`
- Output: `[1, 1, 1]`
