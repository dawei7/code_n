# Moving Stones Until Consecutive II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1040 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Math, Sliding Window, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open problem](https://leetcode.com/problems/moving-stones-until-consecutive-ii/) |

## Problem Description

### Goal

Stones occupy distinct integer positions on the X-axis. The array `stones` gives all of their positions.

A stone is an **endpoint stone** when it currently has either the smallest or the largest occupied position. In one move, choose an endpoint stone and place it at an unoccupied integer position where it is no longer an endpoint stone after the move. For example, from `stones = [1,2,5]`, moving the stone at `5` to `0` or `3` is illegal because that moved stone would still be an endpoint stone.

The game finishes when no legal move remains, which occurs when every stone occupies part of one consecutive block. Return a two-element array: its first value is the minimum number of moves that can finish the game, and its second value is the maximum number of moves that can finish it.

### Function Contract

**Inputs**

- `stones`: the $N$ unique stone positions, where $3 \le N \le 10^4$ and $1 \le \texttt{stones[i]} \le 10^9$.

**Return value**

- `[minimum_moves, maximum_moves]`, the minimum and maximum numbers of legal moves that can be played before all stones are consecutive.

### Examples

**Example 1**

- Input: `stones = [7,4,9]`
- Output: `[1,2]`
- Explanation: For the minimum, move `4 -> 8`. For the maximum, move `9 -> 5` and then `4 -> 6`.

**Example 2**

- Input: `stones = [6,5,4,3,10]`
- Output: `[2,3]`
- Explanation: Two moves can finish by moving `3 -> 8` and then `10 -> 7`. A longest play is `3 -> 7`, `4 -> 8`, and `5 -> 9`. Moving `10 -> 2` is not a legal shortcut because the moved stone would remain an endpoint.
