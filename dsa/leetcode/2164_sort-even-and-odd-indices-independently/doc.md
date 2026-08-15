# Sort Even and Odd Indices Independently

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2164 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-even-and-odd-indices-independently/) |

## Problem Description

### Goal

Rearrange a 0-indexed integer array while keeping every value within its
original index-parity group. Values that began at even indices may be permuted
only among even indices, and values that began at odd indices may be permuted
only among odd indices.

Place the even-indexed values in non-decreasing order from left to right.
Independently, place the odd-indexed values in non-increasing order from left
to right. Return the array after both parity-specific orderings have been
applied.

### Function Contract

**Inputs**

- `nums`: an array of between 1 and 100 integers, each between 1 and 100.

Index parity refers to the original zero-based positions.

**Return value**

Return an array whose even-indexed subsequence is the sorted non-decreasing
version of the input's even-indexed values and whose odd-indexed subsequence is
the sorted non-increasing version of the input's odd-indexed values.

### Examples

#### Example 1

- **Input:** `nums = [4, 1, 2, 3]`
- **Output:** `[2, 3, 4, 1]`

The even-indexed values `[4, 2]` become `[2, 4]`, while the odd-indexed values
`[1, 3]` become `[3, 1]`.

#### Example 2

- **Input:** `nums = [2, 1]`
- **Output:** `[2, 1]`

Each parity group contains one value, so neither position changes.

#### Example 3

- **Input:** `nums = [5, 8, 3, 6, 1]`
- **Output:** `[1, 8, 3, 6, 5]`

The three even positions receive `1`, `3`, and `5`; the odd positions already
contain `8` and `6` in non-increasing order.
