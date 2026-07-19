# Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1465 |
| Difficulty | Medium |
| Topics | Array, Greedy, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/) |

## Problem Description
### Goal

A rectangular cake has height `h` and width `w`. Each value in `horizontalCuts` is the distance from the cake's top edge to a horizontal cut, and each value in `verticalCuts` is the distance from the left edge to a vertical cut. All supplied cut positions are strictly inside the cake, and positions within either array are distinct.

Apply every listed horizontal and vertical cut across the cake. These cuts partition the rectangle into smaller rectangular pieces. Determine the greatest area among those pieces. Because the dimensions can make the area very large, return that maximum area modulo $10^9+7$.

### Function Contract
**Inputs**

- `h`: the cake height, with $2 \le h \le 10^9$.
- `w`: the cake width, with $2 \le w \le 10^9$.
- `horizontal_cuts`: the horizontal cut coordinates. Its length $H$ satisfies $1 \le H \le \min(h-1,10^5)$; every coordinate is distinct and lies strictly between `0` and `h`.
- `vertical_cuts`: the vertical cut coordinates. Its length $V$ satisfies $1 \le V \le \min(w-1,10^5)$; every coordinate is distinct and lies strictly between `0` and `w`.

**Return value**

Return the largest rectangular piece area after all cuts, reduced modulo $1{,}000{,}000{,}007$.

### Examples
**Example 1**

- Input: `h = 5, w = 4, horizontal_cuts = [1,2,4], vertical_cuts = [1,3]`
- Output: `4`
- Explanation: The largest height gap is `2` and the largest width gap is `2`, producing area `4`.

**Example 2**

- Input: `h = 5, w = 4, horizontal_cuts = [3,1], vertical_cuts = [1]`
- Output: `6`
- Explanation: The unsorted coordinates create a maximum height gap of `2` and a maximum width gap of `3`.

**Example 3**

- Input: `h = 5, w = 4, horizontal_cuts = [3], vertical_cuts = [3]`
- Output: `9`
- Explanation: The piece between the top edge and height `3`, and between the left edge and width `3`, has area `3 * 3`.
