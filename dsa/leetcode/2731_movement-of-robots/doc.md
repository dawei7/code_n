# Movement of Robots

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2731 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Brainteaser, Sorting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/movement-of-robots/) |

## Problem Description

### Goal

Robots occupy distinct coordinates on an infinite number line. Robot `i` begins at `nums[i]` and moves one unit per second in the direction described by `s[i]`: `L` toward smaller coordinates and `R` toward larger coordinates.

When two robots meet, each instantly reverses direction without losing time. A collision may occur at an integer coordinate or between two integer coordinates. After exactly `d` seconds, compute the sum of the absolute distances between every unordered pair of robots. Pairs `(i, j)` and `(j, i)` are the same pair. Return the sum modulo $10^9+7$.

### Function Contract

**Inputs**

- `nums`: Distinct initial robot coordinates, with $2 \le n=\lvert\texttt{nums}\rvert \le 10^5$ and $-2\cdot10^9 \le \texttt{nums}[i] \le 2\cdot10^9$.
- `s`: A length-$n$ string containing only `L` and `R`; character `i` gives robot `i`'s initial direction.
- `d`: The elapsed time, with $0 \le d \le 10^9$.

**Return value**

Return the sum of pairwise distances after `d` seconds, reduced modulo $10^9+7$.

### Examples

#### Example 1

- **Input:** `nums = [-2,0,2], s = "RLL", d = 3`
- **Output:** `8`
- **Explanation:** After all movements and collisions, the occupied coordinates are `[-3,-1,1]`; their three pair distances sum to `2 + 4 + 2 = 8`.

#### Example 2

- **Input:** `nums = [1,0], s = "RL", d = 2`
- **Output:** `5`
- **Explanation:** The two final coordinates are `3` and `-2`, whose distance is five.

#### Example 3

- **Input:** `nums = [-5,0,7], s = "LRL", d = 0`
- **Output:** `24`
- **Explanation:** No robot moves, so the distances are `5`, `12`, and `7`.
