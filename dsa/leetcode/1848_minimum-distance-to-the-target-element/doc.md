# Minimum Distance to the Target Element

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/minimum-distance-to-the-target-element/) |
| Frontend ID | 1848 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

An integer array `nums` contains at least one occurrence of `target`, and `start` identifies a valid array index. Moving between neighboring indices costs one unit per step, so reaching index $i$ from `start` has distance $\lvert i-\texttt{start}\rvert$.

Consider every index whose value equals `target`. Return the least distance from `start` to any such index. The target may already occupy the starting position, may occur several times on either side, or may appear only at an endpoint.

### Function Contract

**Inputs**

- `nums`: a list of integers with $1 \le \lvert\texttt{nums}\rvert \le 1000$.
- `target`: an integer guaranteed to occur in `nums`.
- `start`: an index satisfying $0 \le \texttt{start}<\lvert\texttt{nums}\rvert$.
- Let $n=\lvert\texttt{nums}\rvert$.

**Return value**

- For every index $i$ where `nums[i] == target`, consider $\lvert i-\texttt{start}\rvert$.
- Return the minimum of those distances.

### Examples

**Example 1**

- Input: `nums = [1, 2, 3, 4, 5]`, `target = 5`, `start = 3`
- Output: `1`

The target is at index 4, one step from index 3.

**Example 2**

- Input: `nums = [1]`, `target = 1`, `start = 0`
- Output: `0`

**Example 3**

- Input: `nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]`, `target = 1`, `start = 0`
- Output: `0`
