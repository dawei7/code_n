# Minimum Moves to Make Array Complementary

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1674 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-moves-to-make-array-complementary/) |

## Problem Description
### Goal
An even-length array is complementary when every mirrored pair has the same sum: for each index $i$, the values at `i` and `n - 1 - i` must add to one common target. Each original value lies between $1$ and `limit`, inclusive.

In one move, replace any single array element with any integer in that same inclusive range. Choose both the common target sum and the replacements, then return the minimum number of moves required to make all mirrored pairs satisfy it.

### Function Contract
**Inputs**

- `nums`: an even-length integer array of size $n$, with every value between $1$ and `limit`.
- `limit`: the largest legal replacement value.

Let $L=\texttt{limit}$.

**Return value**

Return the fewest single-element replacements needed so every mirrored pair in `nums` has one common sum.

### Examples
**Example 1**

- Input: `nums = [1,2,4,3], limit = 4`
- Output: `1`

**Example 2**

- Input: `nums = [1,2,2,1], limit = 2`
- Output: `2`

**Example 3**

- Input: `nums = [1,2,1,2], limit = 2`
- Output: `0`
