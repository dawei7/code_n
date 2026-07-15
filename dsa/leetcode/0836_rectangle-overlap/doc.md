# Rectangle Overlap

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 836 |
| Difficulty | Easy |
| Topics | Math, Geometry |
| Official Link | [LeetCode](https://leetcode.com/problems/rectangle-overlap/) |

## Problem Description
### Goal
An axis-aligned rectangle is represented as `[x1, y1, x2, y2]`. The point `(x1, y1)` is its bottom-left corner and `(x2, y2)` is its top-right corner; its horizontal edges are parallel to the x-axis and its vertical edges are parallel to the y-axis.

Two rectangles overlap only when their intersection has positive area. Rectangles that merely share an edge or a corner do not overlap. Given valid nonzero-area rectangles `rec1` and `rec2`, return `true` if they overlap and `false` otherwise.

### Function Contract
**Inputs**

- `rec1`: four integers `[x1, y1, x2, y2]` describing the first axis-aligned rectangle.
- `rec2`: four integers in the same bottom-left/top-right format.
- Every coordinate lies in $[-10^9,10^9]$, and each rectangle has positive width and height.

**Return value**

Return a boolean indicating whether the intersection of the two rectangles has positive area.

### Examples
**Example 1**

- Input: `rec1 = [0, 0, 2, 2], rec2 = [1, 1, 3, 3]`
- Output: `true`

**Example 2**

- Input: `rec1 = [0, 0, 1, 1], rec2 = [1, 0, 2, 1]`
- Output: `false`

The rectangles share an edge but have no positive-area intersection.

**Example 3**

- Input: `rec1 = [0, 0, 1, 1], rec2 = [2, 2, 3, 3]`
- Output: `false`

### Required Complexity
- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

Project each rectangle onto the x-axis. Their horizontal intersection has positive length exactly when the greater left boundary is strictly less than the lesser right boundary:

$$
\max(x_{1}^{(1)},x_{1}^{(2)}) < \min(x_{2}^{(1)},x_{2}^{(2)}).
$$

Apply the same strict comparison to the bottom and top boundaries on the y-axis. An axis-aligned intersection is itself a rectangle whose area is the product of those two intersection lengths. Consequently, its area is positive if and only if both one-dimensional lengths are positive. Returning the conjunction of the two comparisons is therefore exact.

The inequalities must be strict. Equality on either axis gives zero width or zero height, which represents only edge or corner contact and must return `false`.

#### Complexity detail

The method reads eight fixed coordinates and performs a constant number of comparisons, so its time is $O(1)$. It creates no input-dependent storage, giving $O(1)$ space.

#### Alternatives and edge cases

- **Negate four separating conditions:** The rectangles overlap exactly when neither lies entirely left, right, above, or below the other; this is the same constant-time geometry expressed through non-overlap.
- **Enumerate integer unit intervals:** Integer coordinates make it possible to count overlap width and height one unit at a time, but that takes $O(U)$ time for coordinate span $U$ and is infeasible near the coordinate limits.
- **Shared edge:** Equality between a right boundary and the other left boundary gives zero horizontal intersection and is not overlap.
- **Shared corner:** Equality on both axes still gives zero area and must return `false`.
- **Containment:** If one rectangle is wholly inside the other, both projected intersections remain strictly positive.
- **Negative coordinates:** The comparisons depend only on ordering, so crossing or lying below the origin changes nothing.

</details>
