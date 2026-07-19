# Describe the Painting

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1943 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Sorting, Prefix Sum |
| Official Link | [LeetCode](https://leetcode.com/problems/describe-the-painting/) |

## Problem Description
### Goal
A long, narrow painting is represented by a number line. Each input entry
paints a unique color over a half-open segment `[start, end)`. The left endpoint
belongs to the segment, while the right endpoint does not. Wherever segments
overlap, their colors form a set, represented in the output by the sum of the
distinct color values in that set.

Describe every painted portion using the minimum number of non-overlapping
half-open segments. Each result entry gives a left endpoint, a right endpoint,
and the mixed-color sum throughout that span. Unpainted gaps must be omitted.
A boundary where the underlying color set changes must remain a boundary even
if the sums on its two sides happen to be equal.

### Function Contract
**Inputs**

- `segments`: between 1 and $2\cdot 10^4$ entries of the form
  `[start, end, color]`, where
  $1 \le \textit{start} < \textit{end} \le 10^5$ and
  $1 \le \textit{color} \le 10^9$. Every color value is unique.

**Return value**

- A description `[left, right, mixedColor]` for each nonempty painted span
  `[left, right)`, excluding unpainted regions. The entries may be returned in
  any order.

### Examples
**Example 1**

- Input: `segments = [[1, 4, 5], [4, 7, 7], [1, 7, 9]]`
- Output: `[[1, 4, 14], [4, 7, 16]]`

**Example 2**

- Input: `segments = [[1, 7, 9], [6, 8, 15], [8, 10, 7]]`
- Output: `[[1, 6, 9], [6, 7, 24], [7, 8, 15], [8, 10, 7]]`

**Example 3**

- Input: `segments = [[1, 4, 5], [1, 4, 7], [4, 7, 1], [4, 7, 11]]`
- Output: `[[1, 4, 12], [4, 7, 12]]`
- Explanation: The equal sums cannot be merged because their color sets differ.

### Required Complexity
- **Time:** $O(N\log N)$
- **Space:** $O(N)$

<details>
<summary>Approach</summary>

#### General

**Record only color changes**

For a segment `[start, end, color]`, add `color` to the change stored at
`start` and subtract it from the change stored at `end`. Between consecutive
coordinates that have changes, no segment begins or ends, so the active color
set and its sum remain constant.

**Sweep every recorded boundary**

Visit all change coordinates in increasing order while carrying the current
mixed-color sum. Before applying the change at the current coordinate, the
carried sum describes the half-open span from the previous coordinate to the
current one. Emit that span when the sum is positive; a zero sum identifies an
unpainted gap.

Apply the current net change only after considering the preceding span. This
ordering implements the half-open endpoint rule: colors ending at a coordinate
do not cover what follows, while colors starting there do.

Every emitted span has no internal color-set boundary and is therefore
uniform. Conversely, every input endpoint remains a sweep coordinate, even
when its net numeric change is zero. Thus adjacent regions with different
color sets are kept separate despite equal sums, and all painted points appear
in exactly one result span.

#### Complexity detail

Building the difference map takes $O(N)$ time and stores at most $2N$
coordinates. Sorting those coordinates costs $O(N\log N)$, and the sweep is
linear in their count. The total time is $O(N\log N)$ and the difference map,
sorted coordinates, and result use $O(N)$ space.

#### Alternatives and edge cases

- **Endpoint-by-endpoint rescanning:** Sort every distinct endpoint, then scan
  all input segments to find the colors covering each consecutive span. It is
  correct but can take $O(N^2)$ time.
- **Coordinate array:** Apply differences in an array of size $10^5+1$ and
  sweep the complete coordinate domain. This avoids sorting but ties work and
  storage to the coordinate bound rather than the actual number of endpoints.
- Several segments may start or end at one coordinate; their changes must be
  combined before the next span is evaluated.
- A segment ending where another begins does not overlap the new segment.
- Unpainted gaps have a carried sum of zero and must not appear in the result.
- Equal mixed-color sums on adjacent spans cannot be merged when the active
  color sets differ.
- A single input segment is returned unchanged apart from its result shape.

</details>
