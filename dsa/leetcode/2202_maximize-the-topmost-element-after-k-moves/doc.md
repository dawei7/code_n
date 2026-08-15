# Maximize the Topmost Element After K Moves

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2202 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-the-topmost-element-after-k-moves/) |

## Problem Description

### Goal

The 0-indexed array `nums` describes a pile from top to bottom, with `nums[0]` currently on top. One move may remove the top element when the pile is nonempty, or place any previously removed element back on top.

Perform exactly `k` moves and maximize the value left at the top. Removed elements may be chosen in any order when restored. If every legal sequence of exactly `k` moves leaves the pile empty, return `-1`.

### Function Contract

**Inputs**

- `nums`: a nonempty list of pile values, with $1 \le n \le 10^5$ and $0 \le \texttt{nums[i]} \le 10^9$.
- `k`: the exact move count, where $0 \le k \le 10^9$.

**Return value**

Return the greatest achievable top value after exactly `k` legal moves, or `-1` if no nonempty final pile is possible.

### Examples

#### Example 1

- **Input:** `nums = [5,2,2,4,0,6]`, `k = 4`
- **Output:** `5`

Remove the first three values, then restore `5` on the fourth move.

#### Example 2

- **Input:** `nums = [2]`, `k = 1`
- **Output:** `-1`

The only legal move removes the sole element, leaving the pile empty.
