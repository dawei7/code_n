# Check if it is Possible to Split Array

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2811 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-it-is-possible-to-split-array/) |

## Problem Description

### Goal

You are given an integer array `nums` and a threshold `m`. Starting with the whole array, repeatedly choose one existing contiguous subarray of length at least two and split it at some boundary into two nonempty contiguous parts. A resulting part is good when it has length one or its element sum is at least `m`.

A split is permitted only when both resulting parts are good. Determine whether some sequence of valid splits can eventually separate the original array into `n` singleton arrays. Parts created earlier may be split again, and the original order and contiguity of elements must be preserved throughout.

### Function Contract

**Inputs**

- `nums`: A list of $n$ positive integers, where $1 \leq n \leq 100$ and $1 \leq \texttt{nums[i]} \leq 100$.
- `m`: The minimum sum for every nonsingleton part, where $1 \leq m \leq 200$.

**Return value**

Return `true` if a sequence of valid contiguous splits can produce all singleton arrays; otherwise return `false`.

### Examples

#### Example 1

- **Input:** `nums = [2, 2, 1]`, `m = 4`
- **Output:** `true`
- **Explanation:** Split off `[1]`; the remaining `[2, 2]` is good and can then split into two singletons.

#### Example 2

- **Input:** `nums = [2, 1, 3]`, `m = 5`
- **Output:** `false`
- **Explanation:** Either first split leaves a length-two part whose sum is below `m`.

#### Example 3

- **Input:** `nums = [2, 3, 3, 2, 3]`, `m = 6`
- **Output:** `true`
- **Explanation:** The adjacent pair `[3, 3]` can be preserved while surrounding singletons are peeled away, then the pair itself is split.
