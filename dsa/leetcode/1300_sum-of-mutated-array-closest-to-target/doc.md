# Sum of Mutated Array Closest to Target

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1300 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/) |

## Problem Description
### Goal
Given a positive integer array `arr` and an integer `target`, choose an integer `value`. Form a mutated array by replacing every element greater than `value` with `value`, while leaving every element at most `value` unchanged.

Choose the `value` whose mutated-array sum has the smallest absolute difference from `target`. If two values achieve the same difference, return the smaller one. The answer does not need to be one of the original array elements.

### Function Contract
**Inputs**

- `arr`: a positive integer array of length $n$, where $1 \le n \le 10^4$ and $1 \le \texttt{arr[i]} \le 10^5$.
- `target`: the desired sum, where $1 \le \texttt{target} \le 10^5$.
- Let $M=\max(\texttt{arr})$.

**Return value**

The smallest integer cap minimizing

$$
\left\lvert \sum_{x \in \texttt{arr}} \min(x,\texttt{value})-\texttt{target} \right\rvert.
$$

### Examples
**Example 1**

- Input: `arr = [4,9,3]`, `target = 10`
- Output: `3`
- Explanation: Cap 3 produces sum 9 and cap 4 produces sum 11; both differ by 1, so the smaller cap wins.

**Example 2**

- Input: `arr = [2,3,5]`, `target = 10`
- Output: `5`
- Explanation: No mutation is needed because the original sum already equals the target.

**Example 3**

- Input: `arr = [60864,25176,27249,21296,20204]`, `target = 56803`
- Output: `11361`
