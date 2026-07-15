# Minimum Time Visiting All Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1266 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-time-visiting-all-points/) |

## Problem Description

### Goal

An array gives $n$ points with integer coordinates on a 2D plane. Starting at the first point, visit every point in exactly the order in which it appears. Passing through a point scheduled for later does not visit it early; it counts only when its position in the required sequence is reached.

During one second, you may move one unit horizontally, one unit vertically, or one unit in each direction simultaneously. The last option is a diagonal move of Euclidean length $\sqrt{2}$. Return the minimum total number of seconds needed to complete the ordered visit.

### Function Contract

**Inputs**

- `points`: an ordered array of $n$ coordinate pairs `points[i] = [x_i, y_i]`, where $1 \le n \le 100$ and $-1000 \le x_i,y_i \le 1000$.

**Return value**

- Return the minimum time in seconds required to visit all points in their given order.

### Examples

**Example 1**

- Input: `points = [[1,1],[3,4],[-1,0]]`
- Output: `7`

**Example 2**

- Input: `points = [[3,2],[-2,2]]`
- Output: `5`

**Example 3**

- Input: `points = [[0,0],[0,0],[2,1]]`
- Output: `2`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Solve one required leg independently**

For consecutive points, let $\Delta_x$ and $\Delta_y$ be the absolute coordinate differences. One second can reduce both remaining differences by one with a diagonal move. Use diagonals while both differences are positive, then finish the larger unmatched difference with horizontal or vertical moves. This constructs a route of length $\max(\Delta_x,\Delta_y)$.

No route can be shorter: a single move changes either coordinate by at most one, so closing the larger coordinate difference requires at least $\max(\Delta_x,\Delta_y)$ seconds. The constructed route meets this lower bound and is therefore optimal for that leg.

**Add the forced legs**

The visit order partitions the journey into the $n-1$ consecutive legs. Reaching an intermediate point is mandatory before the following leg begins, so choices on one leg cannot reduce the minimum displacement required on another. Sum the Chebyshev distance $\max(\lvert x_i-x_{i-1}\rvert,\lvert y_i-y_{i-1}\rvert)$ over all adjacent pairs.

Passing through a later point causes no special case because it does not satisfy that later visit until all preceding points have been visited.

#### Complexity detail

The algorithm examines each of the $n-1$ adjacent pairs once and performs constant work per pair, giving $O(n)$ time. It keeps only the running total and coordinate differences, so its auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Simulate every second:** Move diagonally and then along one axis for each leg; it is correct, but its running time depends on the coordinate distances rather than only on $n$.
- **Euclidean distance:** Taking a square root models geometric length, not the number of allowed one-second moves, and produces the wrong objective.
- **Manhattan distance:** Adding both coordinate differences ignores that one diagonal move reduces both simultaneously and can overcount.
- **Single point:** No movement is required, so the total is `0`.
- **Repeated consecutive points:** Both coordinate differences are zero and that leg contributes `0`.
- **Negative coordinates:** Absolute differences make the same formula valid in every quadrant.

</details>
