# Minimum Number of Taps to Open to Water a Garden

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1326 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Greedy |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/) |

## Problem Description
### Goal
A one-dimensional garden occupies the closed interval from 0 through `n`. One tap stands at every integer point `i` from 0 through `n`; opening it waters the interval from `i - ranges[i]` through `i + ranges[i]`, clipped conceptually to the garden.

Choose the fewest taps whose combined watered intervals cover every point of `[0, n]`. Return that minimum number, or `-1` when some part of the garden cannot be reached by any selection of taps.

Coverage is continuous rather than limited to integer positions. Intervals that meet at an endpoint connect without leaving a gap.

### Function Contract
**Inputs**

- `n`: the garden length, where $1\le n\le10^4$.
- `ranges`: an array of length $n+1$ with $0\le\texttt{ranges[i]}\le100$.

**Return value**

The minimum number of taps required to cover the entire closed interval $[0,n]$, or `-1` if full coverage is impossible.

### Examples
**Example 1**

- Input: `n = 5, ranges = [3,4,1,1,0,0]`
- Output: `1`
- Explanation: The tap at position 1 covers the whole garden.

**Example 2**

- Input: `n = 3, ranges = [0,0,0,0]`
- Output: `-1`
- Explanation: No tap covers any positive-length segment.

**Example 3**

- Input: `n = 7, ranges = [1,2,1,0,2,1,0,1]`
- Output: `3`
- Explanation: Three suitably overlapping tap intervals cover from 0 through 7.

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Compress intervals by their left endpoint**

For every tap, clip its coverage to `[0, n]`. In an array `farthest`, record at each integer left endpoint the greatest right endpoint reached by any tap starting there. Keeping only the greatest endpoint loses no useful choice because a shorter interval with the same start can never improve a cover.

**Advance coverage in greedy layers**

Scan positions from left to right while maintaining `current_end`, the farthest point covered by the taps already committed, and `next_end`, the farthest point reachable by opening one more tap whose interval begins no later than the current scan position.

When the scan reaches `current_end`, the current set cannot progress farther without another tap. Commit the candidate that produced `next_end`, increment the count, and make that endpoint the new boundary. If `next_end` does not move past the scan position, there is an uncovered gap and the answer is `-1`.

At each boundary, every interval eligible to continue the cover has already been examined. Choosing the one reaching farthest cannot use more taps than choosing a shorter eligible interval, because it leaves a superset of the garden available to the remaining choices. Repeating this exchange argument gives a minimum-cardinality cover.

#### Complexity detail

Creating `farthest` scans $n+1$ taps, and the greedy pass scans $n$ positions, for $O(n)$ time. The endpoint array uses $O(n)$ space.

#### Alternatives and edge cases

- **Sort all intervals:** Standard greedy interval covering after sorting by left endpoint takes $O(n\log n)$ time and is correct, but integer endpoints make the linear bucketed form possible.
- **Dynamic programming:** A minimum-tap value for every prefix can be computed, but a direct transition over covering taps may take $O(n^2)$ time.
- **Zero-radius taps:** They cover no positive length and cannot bridge a gap.
- **One tap covers all:** The first greedy commitment reaches `n`, so the answer is 1.
- **Touching endpoints:** Intervals ending and beginning at the same coordinate maintain continuous coverage.
- **Uncovered gap:** Return `-1` as soon as no eligible interval extends the current boundary.

</details>
