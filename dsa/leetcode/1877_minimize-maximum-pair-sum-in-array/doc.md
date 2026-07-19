# Minimize Maximum Pair Sum in Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/) |
| Frontend ID | 1877 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

For a pair of values $(a,b)$, its pair sum is $a+b$. Once several pairs have been formed, their maximum pair sum is the largest of those individual sums.

Given an even-length integer array `nums`, divide all $N$ elements into exactly $N/2$ pairs. Every occurrence must belong to exactly one pair, including repeated values. Choose the pairing that makes the largest pair sum as small as possible, and return that minimized maximum.

### Function Contract

**Inputs**

- `nums`: an array of even length $N$, where $2 \le N \le 10^5$ and $1 \le \texttt{nums[i]} \le 10^5$.

**Return value**

- Return the minimum possible maximum pair sum after assigning every array element to exactly one pair.

### Examples

**Example 1**

- Input: `nums = [3,5,2,3]`
- Output: `7`

The pairs `(3,3)` and `(5,2)` have sums $6$ and $7$, so their maximum is $7$.

**Example 2**

- Input: `nums = [3,5,4,2,4,6]`
- Output: `8`

The pairs `(3,5)`, `(4,4)`, and `(6,2)` all have sums at most $8$.

**Example 3**

- Input: `nums = [9,1]`
- Output: `10`

With two elements, the sole pair is forced.
