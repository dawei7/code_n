# Minimum White Tiles After Covering With Carpets

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2209 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | String, Dynamic Programming, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-white-tiles-after-covering-with-carpets/) |

## Problem Description

### Goal

A 0-indexed binary string `floor` describes a row of tiles: `0` is a black tile and `1` is a white tile. You have `numCarpets` black carpets, and every carpet covers exactly `carpetLen` consecutive tile positions.

Place the carpets to minimize the number of white tiles that remain visible. Carpets may overlap, so several carpets can cover the same positions; covered black tiles have no additional effect. Return the smallest achievable count of uncovered white tiles.

### Function Contract

**Inputs**

- `floor`: a binary string of length $n$, where $1 \le n \le 1000$.
- `numCarpets`: the number $c$ of available carpets, where $1 \le c \le 1000$.
- `carpetLen`: the common carpet length $\ell$, where $1 \le \ell \le n$.

**Return value**

Return the minimum number of white tiles visible after placing the available carpets optimally.

### Examples

**Example 1**

- Input: `floor = "10110101"`, `numCarpets = 2`, `carpetLen = 2`
- Output: `2`
- Explanation: two length-two intervals can cover all but two of the white tiles.

**Example 2**

- Input: `floor = "11111"`, `numCarpets = 2`, `carpetLen = 3`
- Output: `0`
- Explanation: the carpets may overlap while their union covers the entire floor.

**Example 3**

- Input: `floor = "0000"`, `numCarpets = 1`, `carpetLen = 2`
- Output: `0`
- Explanation: no white tile is visible even before a carpet is placed.
