## General

**Separate points with no direction**

A point exactly equal to `location` has zero displacement. It has no meaningful viewing angle, but the statement says it is always visible regardless of rotation.

The source counts such points in `same` and excludes them from angular processing. Multiple points may share that coordinate, and each contributes separately.

Every other point has a direction from the observer, calculated by:

`atan2(yi - y, xi - x)`.

`atan2` returns an angle in radians, generally in $[-\pi,\pi]$, and correctly determines the quadrant from signed horizontal and vertical differences. Distance does not matter because points do not block one another and visibility depends only on direction.

**Sort directions around the circle**

All directional angles are stored in `v` and sorted. On a line rather than a circle, the best set within angular width `t` would be a longest sorted interval whose endpoint difference is at most `t`.

The challenge is the wrap near $-\pi$ and $\pi$. Directions just below $\pi$ and just above $-\pi$ are physically close but appear at opposite ends of the sorted list.

**Duplicate one revolution later**

After sorting the original $n$ angles, the source appends a shifted copy:

`v += [deg + 2 * pi for deg in v]`.

Each shifted value represents the same physical direction one full revolution later. The circular sequence is now unwrapped into a sorted span covering two revolutions.

An interval that crosses the original end can be represented normally: it starts at a late original angle and continues into the shifted early angles.

The problem guarantees `angle < 360`, so the window width is less than $2\pi$. A window cannot legitimately include both an original direction and its full-revolution duplicate, preventing double counting.

**Convert the field of view to radians**

`t = angle * pi / 180` converts degrees to radians so it uses the same unit as `atan2`.

For a window starting at `v[i]`, every direction no greater than `v[i] + t` lies within an inclusive angular interval of width `t`.

**Use binary search for each possible left boundary**

For each original index `i` from zero through `n - 1`, the source calculates:

`bisect_right(v, v[i] + t) - i`.

`bisect_right` returns the first index after all values less than or equal to the boundary. Subtracting `i` gives the number of angles from `v[i]` through that inclusive endpoint.

Using the right variant is important because boundary points are visible. A direction exactly `angle` degrees from the left boundary must be included.

The maximum over all starts is stored in `mx`. If there are no directional points, the generator is empty and `max(..., default=0)` safely yields zero.

**Why an optimal view can start at a point**

Consider any non-empty optimal angular interval. If its left boundary does not coincide with its first included direction, rotate the interval counterclockwise or clockwise as appropriate until the left boundary reaches that first direction. No included point is lost before that moment, and the right boundary moves by the same amount, potentially including more points.

Therefore, some optimal interval has its left boundary at one of the observed directions. Testing all original `v[i]` covers every necessary start. Shifted indices do not need to be starts because they duplicate the same circular choices.

**Adding always-visible points**

`mx` counts only points away from the observer. The final return is `mx + same` because all colocated points are visible in addition to any chosen directional window.

Colocated points do not consume angular width or influence the optimal rotation, so separating and adding them is exact.

**A wraparound picture**

Suppose directions are $179^\circ$ and $-179^\circ$ with a $5^\circ$ field. In the original sorted order they are far apart numerically. After duplication, $-179^\circ+360^\circ=181^\circ$ appears beside $179^\circ$. A window from $179^\circ$ through $184^\circ$ counts both.

**Why the answer is correct**

Every binary-search count corresponds to an inclusive field interval of legal width and therefore a visible set. The alignment argument proves an optimal non-empty interval begins at some original point direction, and duplication represents it even when it crosses the angular seam. Taking the maximum finds the largest directional set, while `same` adds exactly all unconditional points.

## Complexity detail

Let $N$ be the total number of points and $D$ the number not equal to `location`.

Computing directions takes $O(N)$ time. Sorting $D$ angles costs $O(D\log D)$. The source performs one `bisect_right` query for each of the $D$ original starts, costing $O(D\log D)$ total. Thus overall time is $O(N\log N)$.

The angle list grows to length $2D$, and scalar counters use constant space. Auxiliary space is $O(N)$.

A two-pointer scan over the doubled list could reduce the post-sort window search to $O(N)$, but sorting remains dominant.

## Alternatives and edge cases

- **Two-pointer window:** Advance one right pointer monotonically across the doubled angles for $O(N)$ work after sorting. The checked-in source uses simpler binary searches.
- **Use `acos` from dot products:** It loses signed circular orientation unless combined with cross products. `atan2` directly supplies a sortable directed angle.
- **Do not duplicate angles:** A linear window would miss optimal views crossing the $-\pi/\pi$ boundary.
- **Include colocated points in `atan2`:** `atan2(0,0)` gives an arbitrary numeric result and would incorrectly make always-visible points depend on rotation.
- **Zero-degree field:** Points with exactly the same direction are all visible; `bisect_right` counts equal angles.
- **Inclusive boundary:** Right-biased binary search includes angles exactly at `v[i] + t`, subject to floating-point representation.
- **Many points on one ray:** Equal angle values are distinct list entries and all count.
- **Points at the observer:** Every occurrence increments `same` and is added regardless of view.
- **Near-circular field:** Since `angle < 360`, shifted duplicates are not double-counted within one window.
- **No directional points:** The `default=0` maximum plus `same` returns all colocated points.
- **One directional point:** Some view can always include it, so `mx` becomes one.
- **Floating-point boundaries:** The exact source relies on standard double-precision `atan2` and radian conversion; extremely close mathematical boundaries can be sensitive to rounding.
- **Input preservation:** Coordinates and location are read-only; only angle values are stored.
