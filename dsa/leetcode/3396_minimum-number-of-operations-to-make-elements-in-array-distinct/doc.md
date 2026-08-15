# Minimum Number of Operations to Make Elements in Array Distinct

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3396 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Hash Table |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/) |

## Problem Description

### Goal

Given an integer array `nums`, make all remaining elements distinct using as few operations as possible.

One operation removes the first three elements. If fewer than three elements remain, that operation removes all of them instead. The operation may be repeated any number of times, and the empty array is considered to contain distinct elements.

Return the minimum number of operations after which the remaining suffix has no repeated value.

### Function Contract

**Inputs**

- `nums`: A list of $n$ integers, where $1\le n\le100$ and $1\le\texttt{nums[i]}\le100$.

**Return value**

- The minimum number of three-element prefix-removal operations needed to leave a distinct array.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3, 4, 2, 3, 3, 5, 7]`
- **Output:** `2`

The first operation leaves `[4, 2, 3, 3, 5, 7]`; the second leaves the distinct suffix `[3, 5, 7]`.

#### Example 2

- **Input:** `nums = [4, 5, 6, 4, 4]`
- **Output:** `2`

After removing the first three values, `[4, 4]` is still not distinct. The next operation removes both remaining values, and the empty array is valid.

#### Example 3

- **Input:** `nums = [6, 7, 8, 9]`
- **Output:** `0`

The original array is already distinct.
