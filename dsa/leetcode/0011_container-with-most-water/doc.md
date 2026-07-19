# Container With Most Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 11 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Two Pointers, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/container-with-most-water/) |

## Problem Description
### Goal
The array `height` describes vertical lines drawn at consecutive horizontal positions: line `i` extends from the baseline to `height[i]`. Choose two different lines to act as the sides of a container together with the baseline.

The distance between their indices is the container width, and the shorter selected line limits the water height, giving area `(right - left) * min(height[left], height[right])`. Return the greatest area obtainable from any pair. The lines remain vertical and fixed in their original positions; the container cannot be tilted or rearranged.

### Function Contract
**Inputs**

- `height`: `List[int]` containing at least two non-negative wall heights

**Return value**

An `int` equal to the maximum value of `(right - left) * min(height[left], height[right])`.

### Examples
**Example 1**

- Input: `height = [1, 8, 6, 2, 5, 4, 8, 3, 7]`
- Output: `49`

**Example 2**

- Input: `height = [1, 1]`
- Output: `1`

**Example 3**

- Input: `height = [4, 3, 2, 1, 4]`
- Output: `16`
