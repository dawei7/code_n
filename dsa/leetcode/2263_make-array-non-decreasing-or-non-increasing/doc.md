# Make Array Non-decreasing or Non-increasing

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2263 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy, Heap (Priority Queue) |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-non-decreasing-or-non-increasing/) |

## Problem Description

### Goal

You may choose any position in `nums` and increase or decrease its value by
exactly one per operation. Operations can be repeated at any positions, so
changing an original value $x$ into a target value $y$ costs
$\lvert x-y\rvert$ operations.

Choose final integer values that make the whole array either non-decreasing or
non-increasing. Equal adjacent values are allowed in both orders. Return the
minimum total number of unit changes over both possible monotonic directions;
the transformed array itself is not required.

### Function Contract

**Inputs**

- `nums`: An array of $n$ integers, where $1\le n\le1000$ and $0\le\texttt{nums[i]}\le1000$.

**Return value**

Return the minimum value of

$$
\sum_{i=0}^{n-1}\lvert\texttt{nums[i]}-x_i\rvert
$$

over every integer sequence $x$ that is non-decreasing or non-increasing.

### Examples

#### Example 1

- **Input:** `nums = [3,2,4,5,0]`
- **Output:** `4`

#### Example 2

- **Input:** `nums = [2,2,3,4]`
- **Output:** `0`

#### Example 3

- **Input:** `nums = [0]`
- **Output:** `0`
