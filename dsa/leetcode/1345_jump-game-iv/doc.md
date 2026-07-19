# Jump Game IV

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1345 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Hash Table, Breadth-First Search |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/jump-game-iv/) |

## Problem Description

### Goal

You are given an integer array `arr` and begin at index `0`. From a current index `i`, one jump may move to the adjacent index `i - 1`, to the adjacent index `i + 1`, or to any distinct index `j` for which `arr[i] == arr[j]`. Every destination must remain within the array.

Return the minimum number of jumps required to reach the last index. Repeated values can create long-distance connections, and each permitted jump has the same cost.

### Function Contract

**Inputs**

- `arr`: a nonempty array of integers. Let $n$ be its length.

**Return value**

- Return the minimum number of valid jumps from index `0` to index `n - 1`.

### Examples

**Example 1**

- Input: `arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]`
- Output: `3`
- Explanation: One shortest route uses indices `0 -> 4 -> 3 -> 9`.

**Example 2**

- Input: `arr = [7]`
- Output: `0`

**Example 3**

- Input: `arr = [7, 6, 9, 6, 9, 6, 9, 7]`
- Output: `1`
