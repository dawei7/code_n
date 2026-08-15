# Steps to Make Array Non-decreasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2289 |
| Difficulty | Medium |
| Topics | Array, Linked List, Dynamic Programming, Stack, Monotonic Stack, Simulation |
| Official Link | [LeetCode](https://leetcode.com/problems/steps-to-make-array-non-decreasing/) |

## Problem Description

### Goal

Begin with a 0-indexed integer array `nums`. During one step, inspect every
adjacent pair in the array as it exists at the start of that step. Remove
every element `nums[i]` with $i>0$ whose left neighbor is strictly greater:
$\texttt{nums}[i-1] > \texttt{nums}[i]$. All qualifying elements are removed
simultaneously.

Repeat this operation until the remaining array is non-decreasing, meaning
each element is at least its predecessor. Return the number of removal steps
that were performed. A non-decreasing input requires zero steps.

### Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $n = \lvert\texttt{nums}\rvert$. The contract guarantees
$1 \le n \le 10^5$ and $1 \le \texttt{nums}[i] \le 10^9$.

**Return value**

The number of simultaneous-deletion rounds needed before `nums` becomes
non-decreasing.

### Examples

#### Example 1

- **Input:** `nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]`
- **Output:** `3`

#### Example 2

- **Input:** `nums = [4, 5, 7, 7, 13]`
- **Output:** `0`
