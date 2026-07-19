# Construct the Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 492 |
| Difficulty | Easy |
| Topics | Math |
| Official Link | [LeetCode](https://leetcode.com/problems/construct-the-rectangle/) |

## Problem Description
### Goal
Given the positive integer area of a rectangular web page, choose positive integer dimensions `L` and `W`. Their product must equal `area`, and the width may not exceed the length, so $L \ge W$.

Among every factor pair meeting those conditions, return `[L, W]` with the smallest possible difference $L - W$. The desired pair is therefore the one closest to a square, not necessarily the first factorization found from the largest length. A prime area returns `[area, 1]`, while a perfect square returns two equal dimensions.

### Function Contract
**Inputs**

- `area`: a positive integer rectangle area

**Return value**

- The closest valid factor pair as `[length, width]`

### Examples
**Example 1**

- Input: `area = 4`
- Output: `[2, 2]`

**Example 2**

- Input: `area = 37`
- Output: `[37, 1]`

**Example 3**

- Input: `area = 122122`
- Output: `[427, 286]`
