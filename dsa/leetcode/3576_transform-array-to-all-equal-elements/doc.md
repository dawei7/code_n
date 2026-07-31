# Transform Array to All Equal Elements

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3576 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/transform-array-to-all-equal-elements/) |

## Problem Description

### Goal

An integer array `nums` contains only `1` and `-1`. In one operation, choose an adjacent pair and multiply both of its elements by `-1`, reversing both signs. The same adjacent pair may be chosen again in a later operation.

Determine whether at most `k` operations can make every array element equal. The common final sign may be either `1` or `-1`.

### Function Contract

**Inputs**

- `nums`: An array of length $n$ containing only `1` and `-1`, where $1\le n\le10^5$.
- `k`: The maximum number of adjacent-pair operations, where $1\le k\le n$.

**Return value**

Return `true` if all elements can become equal after at most `k` operations; otherwise return `false`.

### Examples

**Example 1**

- Input: `nums = [1,-1,1,-1,1], k = 3`
- Output: `true`
- Explanation: Flipping pairs starting at indices `1` and `2` produces five `1` values in two operations.

**Example 2**

- Input: `nums = [-1,-1,-1,1,1,1], k = 5`
- Output: `false`
- Explanation: No sequence of allowed pair flips can make this even-length array uniform.

---
