# Minimum Index of a Valid Split

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2780 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-index-of-a-valid-split/) |

## Problem Description

### Goal

An element is dominant in an integer array when it occupies strictly more than half of that array's positions. You are given a 0-indexed integer array `nums` that is guaranteed to have exactly one dominant element.

Choose an index `i` with $0 \le i < n-1$ to split `nums` into the inclusive prefix `nums[0...i]` and suffix `nums[i+1...n-1]`. The split is valid only when both non-empty parts have the same dominant element.

Return the smallest index that produces a valid split. Return `-1` when no valid split exists.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $1 \le n \le 10^5$, $1 \le \texttt{nums[i]} \le 10^9$, and exactly one value occurs more than $n/2$ times.

**Return value**

Return the minimum valid split index `i`, or `-1` if no index before the final element makes the array's dominant value dominant on both sides.

### Examples

**Example 1**

- Input: `nums = [1,2,2,2]`
- Output: `2`
- Explanation: Splitting after index `2` gives `[1,2,2]` and `[2]`; `2` is dominant in both parts. Earlier split points do not satisfy both strict-majority tests.

**Example 2**

- Input: `nums = [2,1,3,1,1,1,7,1,2,1]`
- Output: `4`
- Explanation: Each five-element side contains three copies of `1`, so `1` is dominant on both sides. No smaller index creates two parts with that property.

**Example 3**

- Input: `nums = [3,3,3,3,7,2,2]`
- Output: `-1`
- Explanation: Although `3` dominates the complete array, every possible split leaves at least one side on which `3` does not occur more than half the time.
