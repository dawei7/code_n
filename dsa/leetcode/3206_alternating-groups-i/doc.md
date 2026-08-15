# Alternating Groups I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3206 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Sliding Window |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/alternating-groups-i/) |

## Problem Description

### Goal

`colors` describes a circle of red and blue tiles. A value of `0` represents red, and `1` represents blue. The first and last array positions are adjacent because the arrangement is circular.

Consider every group of three consecutive tiles around the circle. A group is alternating when its middle tile has a different color from both its left and right neighbors.

Return how many of these circular three-tile groups are alternating.

### Function Contract

**Inputs**

- `colors`: An array of binary tile colors with $3 \le \lvert\texttt{colors}\rvert \le 100$.

Let $n=\lvert\texttt{colors}\rvert$.

**Return value**

- The number of circular length-three groups whose middle tile differs from both neighboring tiles.

### Examples

#### Example 1

- **Input:** `colors = [1,1,1]`
- **Output:** `0`
- **Explanation:** Every possible middle tile matches both neighbors.

#### Example 2

- **Input:** `colors = [0,1,0,0,1]`
- **Output:** `3`
- **Explanation:** Three choices of middle tile differ from their two circular neighbors.
