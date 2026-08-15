# Minimize Length of Array Using Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3012 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Number Theory |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimize-length-of-array-using-operations/) |

## Problem Description

### Goal

You are given a 0-indexed array `nums` containing positive integers. You may
perform the following operation any number of times, including zero times:

1. Choose two distinct indices `i` and `j` whose current values are both
   positive.
2. Append `nums[i] % nums[j]` to the array.
3. Delete the two selected elements.

The appended remainder may be zero. Because only positive values can be
selected by a later operation, every zero that is created remains in the
array permanently.

Return the minimum length that the array can have after a sequence of legal
operations.

### Function Contract

**Inputs**

- `nums`: the positive integers on which modulo-and-replace operations may be performed

Let $N=\lvert\texttt{nums}\rvert$. The contract guarantees
$1\le N\le10^5$ and $1\le\texttt{nums[i]}\le10^9$.

**Return value**

Return the smallest achievable number of elements remaining in `nums`.

### Examples

#### Example 1

- **Input:** `nums = [1,4,3,1]`
- **Output:** `1`

The values can be reduced until a single zero remains.

#### Example 2

- **Input:** `nums = [5,5,5,10,5]`
- **Output:** `2`

All values are divisible by 5. The four copies of the minimum ultimately
produce two zeros, and those zeros cannot participate in another operation.

#### Example 3

- **Input:** `nums = [2,3,4]`
- **Output:** `1`

Using `3 % 2` creates 1, enabling the array to be consolidated to one element.
