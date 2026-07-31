# Minimum Reverse Operations

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2612 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search, Union-Find, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-reverse-operations/) |

## Problem Description

### Goal

Consider an array `arr` of length `n` whose entries are all zero except for a single `1` initially located at index `p`. Some indices are listed in `banned`; after every operation, the `1` is forbidden from occupying any of those positions.

An operation reverses any contiguous subarray of exactly `k` elements. The chosen subarray must include the current position of the `1` to move it, and the resulting position of the `1` must not be banned. Other banned indices may lie inside the reversed subarray because only the location of the `1` is restricted.

For every index, determine the minimum number of such reversals needed to move the `1` there. Report `-1` for an index that can never be reached.

### Function Contract

**Inputs**

- `n`: The array length, where $1 \leq n \leq 10^5$.
- `p`: The initial position of the `1`, where $0 \leq p < n$.
- `banned`: A list of distinct forbidden positions; it does not contain `p`.
- `k`: The exact reversal length, where $1 \leq k \leq n$.

**Return value**

Return an integer array `answer` of length `n`. `answer[i]` is the minimum operation count needed to place the `1` at index `i`, or `-1` when index `i` is unreachable.

### Examples

**Example 1**

- Input: `n = 4, p = 0, banned = [1, 2], k = 4`
- Output: `[0, -1, -1, 1]`
- Explanation: Reversing the entire array moves the `1` from index `0` to index `3`; indices `1` and `2` are forbidden destinations.

**Example 2**

- Input: `n = 5, p = 0, banned = [2, 4], k = 3`
- Output: `[0, -1, -1, -1, -1]`
- Explanation: The only initial length-three reversal would place the `1` at banned index `2`, so no move is legal.

**Example 3**

- Input: `n = 4, p = 2, banned = [0, 1, 3], k = 1`
- Output: `[-1, -1, 0, -1]`
- Explanation: A reversal of length one cannot change the position of the `1`.
