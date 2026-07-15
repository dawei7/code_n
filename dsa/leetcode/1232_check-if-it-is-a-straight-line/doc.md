# Check If It Is a Straight Line

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1232 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/check-if-it-is-a-straight-line/) |

## Problem Description

### Goal

You are given an integer array `coordinates`, where each `coordinates[i] = [x, y]` represents a distinct point with integer coordinates in the XY plane.

Check whether every supplied point lies on one straight line; the order in which the points appear has no geometric significance. Return `true` when the entire set is collinear and `false` when at least one point departs from the line determined by the others.

### Function Contract

**Inputs**

- `coordinates`: A list of $n$ distinct points `[x, y]`, where $2\le n\le1000$ and $-10^4\le x,y\le10^4$.

**Return value**

- `true` if all points make a straight line in the XY plane; otherwise, `false`.

### Examples

**Example 1**

- Input: `coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]`
- Output: `true`

Every step increases both coordinates by one, so all points lie on the same diagonal.

**Example 2**

- Input: `coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]`
- Output: `false`

The point `[3,4]` does not lie on the diagonal through `[1,1]` and `[2,2]`.

**Example 3**

- Input: `coordinates = [[0,0],[0,5],[0,-2]]`
- Output: `true`

All three points have the same $x$-coordinate and form a vertical line.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Fix one direction for the whole set.** The first two distinct points determine the only possible straight line. Let their coordinate differences be `dx = x1 - x0` and `dy = y1 - y0`. Every later point `[x, y]` belongs to that line exactly when its displacement from `[x0, y0]` has the same direction.

**Compare cross products instead of slopes.** Equal slopes would normally require `(y - y0) / (x - x0) == dy / dx`, but division is unsafe for vertical lines and can introduce floating-point error. Cross-multiplication gives the exact integer test `(x - x0) * dy == (y - y0) * dx`. This equation also handles horizontal and vertical directions without special cases.

Check every point after the first two. If any cross product differs, that point is outside the uniquely determined line and the answer is `false`. If every equality holds, every point shares the first pair's direction from the same origin, so all points lie on that line and the answer is `true`.

#### Complexity detail

The algorithm examines each of the $n$ points once and performs a constant number of integer operations per point, giving $O(n)$ time. It stores only the first point, one direction, and the current point, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Floating-point slope:** Computing and comparing quotients is concise but needs a vertical-line special case and risks rounding errors.
- **Reduced direction pairs:** Normalizing every displacement by its greatest common divisor is exact, but it performs unnecessary gcd work when a cross product suffices.
- **Compare every pair:** Verifying that all pairwise direction vectors are parallel is correct but takes $O(n^2)$ time.
- **Exactly two points:** Any two distinct points determine a straight line, so the result is always `true`.
- **Vertical line:** `dx = 0` is handled directly by the cross-product equality without division.
- **Horizontal line:** `dy = 0` similarly reduces the equality to requiring every point to have the same $y$-coordinate.
- **Negative coordinates:** Signs do not alter the determinant test; ordinary integer multiplication preserves the orientation relation.

</details>
