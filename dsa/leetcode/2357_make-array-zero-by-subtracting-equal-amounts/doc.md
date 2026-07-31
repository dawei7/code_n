# Make Array Zero by Subtracting Equal Amounts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2357 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Sorting, Heap (Priority Queue), Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/) |

## Problem Description

### Goal

You receive a non-negative integer array `nums`. In one operation, choose a
positive integer `x` that is no greater than the array's smallest non-zero
element at that moment. Then subtract `x` from every element that is currently
positive; elements already equal to zero remain unchanged.

Determine the minimum number of such operations needed to make every element
zero. The same chosen amount is applied to all positive entries in an
operation, and the upper bound on `x` ensures that no entry becomes negative.

### Function Contract

**Inputs**

- `nums`: A list of $n$ non-negative integers.

The constraints are $1 \le n \le 100$ and
$0 \le \texttt{nums[i]} \le 100$.

**Return value**

Return the minimum number of valid subtraction operations required to turn
every entry into zero.

### Examples

**Example 1**

- Input: `nums = [1,5,0,3,5]`
- Output: `3`

Choosing amounts `1`, `2`, and `2` successively reduces the three distinct
positive levels 1, 3, and 5 to zero.

**Example 2**

- Input: `nums = [0]`
- Output: `0`

The array is already all zero, so no operation is necessary.
