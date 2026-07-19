# Number of Ships in a Rectangle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1274 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Divide and Conquer, Interactive |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/number-of-ships-in-a-rectangle/) |

## Problem Description

### Goal

Ships occupy distinct integer-coordinate points in a Cartesian plane. Their locations are hidden, so they cannot be read or enumerated directly. Instead, the supplied `Sea` interface provides `hasShips(topRight, bottomLeft)`, which reports whether at least one ship lies inside or on the boundary of the inclusive axis-aligned rectangle between those corners.

Given `topRight` and `bottomLeft`, return the exact number of ships in that rectangle. There are at most $10$ ships in the requested region, and a solution that calls `hasShips` more than $400$ times is rejected.

### Function Contract

**Inputs**

- `sea`: a hidden `Sea` object exposing only `hasShips(topRight, bottomLeft)` for rectangular existence queries.
- `top_right`: a `Point` whose `x` and `y` fields give the target rectangle's upper-right coordinate $(x_2,y_2)$.
- `bottom_left`: a `Point` whose fields give the lower-left coordinate $(x_1,y_1)$, where $0 \le x_1 \le x_2 \le 1000$ and $0 \le y_1 \le y_2 \le 1000$.
- At most $s=10$ distinct ships lie in the target rectangle. Let $C=\max(x_2-x_1+1,y_2-y_1+1)$ be its larger side length.

**Return value**

- Return the number of hidden ship points inside the target rectangle, including its boundary.

### Examples

**Example 1**

- Input: `ships = [[1,1],[2,2],[3,3],[5,5]], top_right = [4,4], bottom_left = [0,0]`
- Output: `3`

**Example 2**

- Input: `ships = [[1,1],[2,2],[3,3]], top_right = [1000,1000], bottom_left = [0,0]`
- Output: `3`

**Example 3**

- Input: `ships = [], top_right = [7,9], bottom_left = [2,4]`
- Output: `0`
