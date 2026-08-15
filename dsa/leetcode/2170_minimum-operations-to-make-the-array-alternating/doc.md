# Minimum Operations to Make the Array Alternating

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2170 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Greedy, Counting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/) |

## Problem Description

### Goal

A 0-indexed array `nums` of positive integers is alternating when every value
equals the value two positions before it, while every adjacent pair contains
different values. Equivalently, all even indices share one value, all odd
indices share another value, and those two values differ.

One operation chooses any index and replaces its element with any positive
integer. Return the minimum number of such replacements needed to make `nums`
alternating. The replacement values need not already occur in the array.

### Function Contract

**Inputs**

- `nums`: an array of $n$ positive integers, where $1\le n\le 10^5$ and
  $1\le\texttt{nums[i]}\le 10^5$.

An index is even or odd according to its 0-based position.

**Return value**

Return the minimum number of element replacements required so that
`nums[i - 2] == nums[i]` for every $2\le i<n$ and
`nums[i - 1] != nums[i]` for every $1\le i<n$.

### Examples

#### Example 1

- **Input:** `nums = [3, 1, 3, 2, 4, 3]`
- **Output:** `3`

Changing the array to `[3, 1, 3, 1, 3, 1]` replaces three elements and is
optimal.

#### Example 2

- **Input:** `nums = [1, 2, 2, 2, 2]`
- **Output:** `2`

Replacing the values at indices 2 and 4 produces `[1, 2, 1, 2, 1]`.
Changing every position to `2` is invalid because adjacent values must differ.

#### Example 3

- **Input:** `nums = [7]`
- **Output:** `0`

A one-element array satisfies both conditions without a replacement.
