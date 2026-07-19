# Buildings With an Ocean View

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1762 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/buildings-with-an-ocean-view/) |

## Problem Description

### Goal

Buildings stand in a line, and `heights[i]` gives the height of the building at index `i`. The ocean lies beyond the right end of the array. A building has an ocean view only when every building between it and the ocean is strictly shorter.

Return the indices of all buildings with an ocean view in increasing order. A building of equal height to the right blocks the view because the required comparison is strict, while the final building always faces the ocean directly.

### Function Contract

**Inputs**

- `heights`: an array of $n$ positive building heights, with $1 \le n \le 10^5$ and $1 \le \texttt{heights[i]} \le 10^9$.

**Return value**

- Return all indices `i` such that `heights[i] > heights[j]` for every $j>i$.
- List the qualifying indices in increasing order.

### Examples

**Example 1**

- Input: `heights = [4, 2, 3, 1]`
- Output: `[0, 2, 3]`
- Explanation: Height `4` exceeds everything to its right, height `3` exceeds the final `1`, and the last building is unobstructed.

**Example 2**

- Input: `heights = [4, 3, 2, 1]`
- Output: `[0, 1, 2, 3]`
- Explanation: Every building is taller than every later building.

**Example 3**

- Input: `heights = [1, 3, 2, 4]`
- Output: `[3]`
- Explanation: The final height `4` blocks every earlier building.
