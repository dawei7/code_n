# Maximum Difference Between Adjacent Elements in a Circular Array

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/) |
| Frontend ID | 3423 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Treat the integer array `nums` as circular rather than as a line. Consecutive positions inside the array are adjacent in the usual way, and the element at the final index is also adjacent to the element at index `0`.

Compute the absolute difference for every circularly adjacent pair and return the largest value. The wrap-around pair must be considered even when an internal pair already has a large difference; no non-adjacent pair is eligible.

### Function Contract

**Inputs**

- `nums`: An integer array of length $n$, where $2 \le n \le 100$ and $-100 \le \texttt{nums[i]} \le 100$.

**Return value**

Return the maximum absolute difference between two adjacent elements in the circular ordering.

### Examples

#### Example 1

- **Input:** `nums = [1,2,4]`
- **Output:** `3`
- **Explanation:** The wrap-around pair `4` and `1` has difference `3`, larger than either internal adjacent difference.

#### Example 2

- **Input:** `nums = [-5,-10,-5]`
- **Output:** `5`
- **Explanation:** Both changes involving `-10` have absolute difference `5`.
