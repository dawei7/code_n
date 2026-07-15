# Circle and Rectangle Overlapping

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1401 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Geometry |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/circle-and-rectangle-overlapping/) |

## Problem Description

### Goal

An axis-aligned rectangle is described by its lower-left corner `(x1, y1)` and upper-right corner `(x2, y2)`. A circle is described by its positive `radius` and center `(xCenter, yCenter)`.

Determine whether the circle and rectangle overlap: they overlap when at least one point belongs to both shapes. Their boundaries are included, so touching at exactly one edge or corner point counts as overlap.

### Function Contract

**Inputs**

- `radius`: the circle's positive integer radius.
- `xCenter`, `yCenter`: the integer coordinates of the circle center.
- `x1`, `y1`: the rectangle's lower-left coordinates.
- `x2`, `y2`: the rectangle's upper-right coordinates, with $x_1 < x_2$ and $y_1 < y_2$.

**Return value**

- `true` if the closed circle and closed rectangle share at least one point; otherwise `false`.

### Examples

**Example 1**

- Input: `radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1`
- Output: `true`

**Example 2**

- Input: `radius = 1, xCenter = 0, yCenter = 0, x1 = 2, y1 = 2, x2 = 4, y2 = 4`
- Output: `false`

**Example 3**

- Input: `radius = 2, xCenter = 1, yCenter = 1, x1 = 0, y1 = 0, x2 = 2, y2 = 2`
- Output: `true`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Find the rectangle point nearest the center.** Clamp `xCenter` to the closed interval from `x1` to `x2`, and clamp `yCenter` independently from `y1` to `y2`. The resulting `(closest_x, closest_y)` lies in the rectangle.

For an axis-aligned rectangle, independent clamping minimizes each squared coordinate difference, so this point minimizes Euclidean distance from the circle center to every rectangle point. If the center lies inside the rectangle, clamping leaves it unchanged and the minimum distance is zero.

The shapes overlap exactly when that minimum squared distance is at most `radius * radius`. Using squared values avoids square roots and preserves tangency through the non-strict comparison.

#### Complexity detail

The input has fixed arity. A constant number of comparisons, arithmetic operations, and assignments gives $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Check only rectangle corners:** A circle can cross the middle of an edge while all four corners remain outside, so corner checks alone are insufficient.
- **Horizontal and vertical separation:** Compute the gap from the center to each rectangle interval and compare the squared gap vector. This is algebraically equivalent to clamping.
- **Center inside rectangle:** The minimum distance is zero, so overlap is guaranteed.
- **Edge tangency:** Equality between squared distance and squared radius counts as overlap.
- **Corner tangency:** Both coordinate gaps may be nonzero and must be combined with the Euclidean squared distance.
- **Negative coordinates:** Clamping and subtraction work without any coordinate translation.

</details>
