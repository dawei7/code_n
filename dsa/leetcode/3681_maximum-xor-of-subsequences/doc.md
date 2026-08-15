# Maximum XOR of Subsequences

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3681 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Math, Greedy, Bit Manipulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-xor-of-subsequences/) |

## Problem Description

### Goal

Given an array `nums` of non-negative integers, select two subsequences independently. Either subsequence may be empty, they may share indices, and each retains the original relative order of its chosen elements.

Let `X` and `Y` be the bitwise XORs of the first and second subsequences, with an empty subsequence contributing zero. Maximize `X XOR Y` over every allowed pair of subsequences.

### Function Contract

**Inputs**

- `nums`: a list of $n$ non-negative integers, where $2\le n\le10^5$ and every value is at most $10^9$.

Let $B=31$, the number of bit positions needed for every legal value.

**Return value**

Return the maximum possible XOR of the two subsequence XOR values.

### Examples

#### Example 1

- **Input:** `nums = [1, 2, 3]`
- **Output:** `3`

For example, subsequences `[2]` and `[2, 3]` have XORs 2 and 1, whose XOR is 3.

#### Example 2

- **Input:** `nums = [5, 2]`
- **Output:** `7`

Choosing the single values in separate subsequences gives `5 XOR 2 = 7`.

#### Example 3

- **Input:** `nums = [8, 4, 2]`
- **Output:** `14`

The XOR of all three values is larger than any individual value and can be realized by choosing that subset in one subsequence and leaving the other empty.
