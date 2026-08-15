# Minimum Recolors to Get K Consecutive Black Blocks

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2379 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/) |

## Problem Description

### Goal

A 0-indexed string `blocks` describes a row of blocks: `'W'` is white and `'B'` is black. One operation may recolor one white block so that it becomes black; black blocks never need to be changed.

Given a target length `k`, determine the fewest recoloring operations needed so that the resulting string contains at least one contiguous run of `k` black blocks. Existing black blocks inside the selected run require no operation.

### Function Contract

**Inputs**

- `blocks`: A string of length $n$ containing only `'W'` and `'B'`, where $1 \le n \le 100$.
- `k`: The required consecutive run length, where $1 \le \texttt{k} \le n$.

**Return value**

- Return the minimum number of white blocks that must be recolored to create at least one contiguous run of `k` black blocks.

**Operation semantics**

- Each operation changes exactly one `'W'` to `'B'`.
- Blocks outside the chosen length-`k` run do not affect whether that run is achieved.

### Examples

#### Example 1

- **Input:** `blocks = "WBBWWBBWBW", k = 7`
- **Output:** `3`
- **Explanation:** A length-seven window with three white blocks can be made entirely black in three operations, and no window needs fewer.

#### Example 2

- **Input:** `blocks = "WBWBBBW", k = 2`
- **Output:** `0`
- **Explanation:** The string already contains consecutive black blocks of the required length.
