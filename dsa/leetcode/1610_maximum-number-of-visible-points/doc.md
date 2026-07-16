# Maximum Number of Visible Points

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1610 |
| Difficulty | Hard |
| Topics | Array, Math, Geometry, Sliding Window, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-visible-points/) |

## Problem Description
### Goal
You remain at the integral coordinate `location` on the plane and may rotate to face any direction. A field of view with width `angle` degrees includes both angular boundaries. After rotating counterclockwise by $d$ degrees from east, it covers every direction from $d-\texttt{angle}/2$ through $d+\texttt{angle}/2$.

Each entry in `points` is an integral coordinate. Coordinates may repeat, points do not block one another, and every point exactly at `location` is visible regardless of rotation. Choose the viewing direction that maximizes the number of visible points and return that maximum.

### Function Contract
**Inputs**

- `points`: an array of $n$ coordinate pairs, where $1 \le n \le 10^5$ and each coordinate is between 0 and 100. Duplicate points are allowed.
- `angle`: the inclusive field-of-view width in degrees, with $0 \le \texttt{angle} < 360$.
- `location`: the fixed observer coordinate, whose two components are also between 0 and 100.

**Return value**

Return the greatest number of points simultaneously visible for some rotation of the field of view.

### Examples
**Example 1**

- Input: `points = [[2, 1], [2, 2], [3, 3]]`, `angle = 90`, `location = [1, 1]`
- Output: `3`
- Explanation: All three directions fit within an inclusive 90-degree sector; collinear points do not obstruct one another.

**Example 2**

- Input: `points = [[2, 1], [2, 2], [3, 4], [1, 1]]`, `angle = 90`, `location = [1, 1]`
- Output: `4`
- Explanation: The point at the observer is always visible in addition to the three directional points.

**Example 3**

- Input: `points = [[1, 0], [2, 1]]`, `angle = 13`, `location = [1, 1]`
- Output: `1`

### Required Complexity
- **Time:** $O(n\log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Separate points without a direction.** Count coordinates equal to `location` before any angular work. They are visible in every orientation and must not be passed to `atan2`, because their zero displacement has no meaningful direction.

**Linearize the circle.** Convert every other displacement `(dx, dy)` to its polar angle with `atan2` and sort the results. A sector may cross the $-\pi$/$\pi$ cut, so append a second copy of the sorted angles after adding $2\pi$ to each. Every circular consecutive group then appears as one ordinary interval in this doubled array.

**Maintain the widest inclusive angular window.** Move a right pointer through the doubled angles and advance the left pointer while their difference exceeds the field width. Equality remains inside because both sector boundaries are inclusive. The current interval contains exactly the directional points visible in one orientation; cap its size at the number of original directions so no point can be counted from both copies. Add the always-visible coincident count to the best window.

Any chosen sector can be rotated clockwise until its lower boundary meets the first contained direction without losing a point, unless it contains only coincident points. Therefore some optimal directional set is represented by a window beginning at a sorted angle. The doubled list represents wraparound sets, and the sliding window examines every such maximal interval, proving the returned count is optimal.

#### Complexity detail

Computing angles takes $O(n)$ time, sorting them costs $O(n\log n)$, and both sliding-window pointers move at most $O(n)$ positions. The angle list and its doubled representation use $O(n)$ space.

#### Alternatives and edge cases

- **Try a sector from every direction and recount all points:** This is correct but takes $O(n^2)$ time because each candidate orientation scans the full point set.
- **Binary search each sorted window endpoint:** After sorting, `bisect_right` can find the inclusive end for every start in $O(n\log n)$ additional time; two pointers reduce that phase to linear time.
- **Compare Cartesian slopes:** Slopes need special handling for vertical rays, quadrants, and circular wraparound; `atan2` supplies a consistent full-circle angle.
- Points at `location` are always visible and should be added after optimizing directional points.
- Duplicate coordinates represent distinct points and all copies count.
- `angle = 0` can still see every point on one exact ray, plus all coincident points.
- A sector crossing the negative/positive angle boundary must be handled as one circular interval.
- Points exactly on either angular boundary count as visible.
- Because `angle < 360`, an original directional point must never be counted from both copies of the doubled list.

</details>
